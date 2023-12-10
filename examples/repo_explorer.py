from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Iterator, TypeVar, Generic, Union, ClassVar, Type

from tree_sitter import Node, Parser
from tree_sitter_languages import get_parser

from sneksitter.visitor import TSVisitor, TraversalReturnT

_T = TypeVar("_T")
_ChildrenT = TypeVar("_ChildrenT", bound="ProjectNode")
_ProjectNodeT = TypeVar("_ProjectNodeT", bound="ProjectNode")


@dataclass
class ProjectNode(Generic[_T, _ChildrenT]):
    node: _T

    @property
    def children(self) -> list[_ChildrenT]:
        return self._get_children()

    def _get_children(self) -> list[_ChildrenT]:
        raise NotImplementedError

    @property
    def text(self) -> str:
        return self._get_text()

    def _get_text(self) -> str:
        raise NotImplementedError

    def _ascii(self, depth: int) -> Iterator[str]:
        yield " " * depth + self.text
        for child in self.children:
            yield from child._ascii(depth + 1)

    @property
    def ascii(self) -> str:
        return "\n".join("".join(line) for line in self._ascii(0))

    def __bool__(self) -> bool:
        if isinstance(self.node, Node):
            return True
        return any(self.children)


@dataclass
class FileNode(ProjectNode[Path, ProjectNode]):
    node: Path

    def _get_text(self) -> str:
        return f"[file] {self.node.name}"

    def _get_children(self) -> list[PythonDefinitionNode]:
        if self.node.is_file():
            return get_node_for_file(self.node) or []
        else:
            return []


@dataclass
class DirectoryNode(ProjectNode[Path, Union[FileNode, "DirectoryNode"]]):
    node: Path

    IGNORED: ClassVar[set[str]] = {
        "venv",
        ".git",
        ".idea",
        "__pycache__",
        "node_modules",
        ".vscode",
    }

    def _get_text(self) -> str:
        return f"[dir] {self.node.name}"

    def _get_children(self) -> list[Union[FileNode, "DirectoryNode"]]:
        children = []
        for child in self.node.iterdir():
            if child.name.startswith(".") or child.name in self.IGNORED:
                continue
            if child.is_dir():
                children.append(DirectoryNode(child))
            else:
                children.append(FileNode(child))
        return children


class _ModuleExplorerBase(TSVisitor):
    definition_node_cls: ClassVar[Type[ProjectNode]]

    def __init__(self, root_node: Node):
        super().__init__(root_node)
        self._definitions = []
        self._definition_stack = []

    def _add_definition(self, node: Node) -> None:
        definition = self.definition_node_cls(node)
        if self._definition_stack:
            self._definition_stack[-1]._children.append(definition)
        else:
            self._definitions.append(definition)

        self._definition_stack.append(definition)

    def _pop_definition(self, node: Node) -> None:
        if self._definition_stack:
            self._definition_stack.pop()

    def get_traversal_result(self) -> TraversalReturnT:
        return tuple(self._definitions)


@dataclass
class PythonDefinitionNode(ProjectNode[Node, "PythonDefinitionNode"]):
    node: Node
    _children: list[PythonDefinitionNode] = field(init=False, default_factory=list)

    def _get_text(self) -> str:
        if self.node.type in ("function_definition", "class_definition"):
            text_parts = []
            for child in self.node.children:
                if child.type == "block":
                    text_parts.append("...")
                elif child.type == "comment":
                    pass
                else:
                    text_parts.append(child.text.decode())
            return " ".join(" ".join(p.strip() for p in part.splitlines()) for part in text_parts)

    def _get_children(self) -> list[PythonDefinitionNode]:
        return self._children[:]


@dataclass
class MarkdownDefinitionNode(ProjectNode[Node, "MarkdownDefinitionNode"]):
    node: Node
    _children: list[MarkdownDefinitionNode] = field(init=False, default_factory=list)

    def _get_text(self) -> str:
        return self.node.text.decode()

    def _get_children(self) -> list[MarkdownDefinitionNode]:
        return self._children[:]


class _ModuleExplorerPython(_ModuleExplorerBase):
    definition_node_cls = PythonDefinitionNode
    visit_function_definition = visit_class_definition = _ModuleExplorerBase._add_definition
    leave_function_definition = leave_class_definition = _ModuleExplorerBase._pop_definition


class _ModuleExplorerMarkdown(_ModuleExplorerBase):
    definition_node_cls = MarkdownDefinitionNode
    visit_atx_heading = _ModuleExplorerBase._add_definition
    leave_atx_heading = _ModuleExplorerBase._pop_definition


get_parser = lru_cache(get_parser)


def get_node_for_file(file: Path) -> Parser | None:
    if file.suffix.lower() == ".py":
        parser = get_parser("python")
        explorer = _ModuleExplorerPython
    elif file.suffix.lower() == ".md":
        parser = get_parser("markdown")
        explorer = _ModuleExplorerMarkdown
    else:
        return None
    explorer_instance = explorer(parser.parse(file.read_bytes()).root_node)
    return explorer_instance.traverse()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument("--language", default="python")
    parser.add_argument("-o", "--output", type=argparse.FileType("w"), default="-")
    args = parser.parse_args()

    tree = DirectoryNode(args.path) if args.path.is_dir() else FileNode(args.path)
    args.output.write(tree.ascii)
