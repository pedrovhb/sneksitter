from __future__ import annotations

from pathlib import Path
from typing import TypeVar, Type

import tree_sitter_languages
from tree_sitter import Node, Tree

from sneksitter.metadata import FieldNameMetadataProvider, MetadataProvider
from sneksitter.visitor import BaseVisitor

try:
    from rich.tree import Tree as RichTree
except ImportError:
    raise ImportError(
        "The `rich` package is required to use the RichTreeBuilder. "
        "Please install it with `pip install rich`."
    )

_T = TypeVar("_T")


class RichTreeBuilder(BaseVisitor):
    named_only = False
    METADATA_PROVIDERS = (FieldNameMetadataProvider,)

    def __init__(self) -> None:
        super().__init__()
        self._tree: RichTree = RichTree("root")
        self._stack: list[RichTree] = [self._tree]

    show_node_text_types = {"identifier", "string", "number", "attribute"}

    def _add_node(self, node_text: str) -> None:
        prev = self._stack[-1]
        new = prev.add(node_text)
        self._stack.append(new)

    def _format_node_display(
        self,
        node: Node,
        metadata: dict[Type[MetadataProvider[_T]], _T],
    ) -> str:
        parts = [f"[bold blue]{node.type}[/]"]
        if node.type in self.show_node_text_types:
            parts.append(f"`[yellow]{node.text.decode()}[/]`")
        if (field_name := metadata.get(FieldNameMetadataProvider)) is not None:
            parts.append(f"[darkgrey]\\[field: {field_name}][/]")
        return " ".join(parts)

    def visit(self, node: Node, metadata: dict[Type[MetadataProvider[_T]], _T]) -> None:
        self._add_node(self._format_node_display(node, metadata))

    def leave(self, node: Node, metadata: dict[Type[MetadataProvider[_T]], _T]) -> None:
        self._stack.pop()

    @classmethod
    def get_tree(cls, tree: Tree, named_only: bool = False) -> RichTree:
        """Class method to traverse the tree and call the visitor's methods."""
        return cls.traverse_tree(tree, named_only=named_only)._tree


if __name__ == "__main__":
    import rich

    parser = tree_sitter_languages.get_parser("python")

    source = Path(__file__).read_bytes()
    tree = parser.parse(source)
    rich_tree = RichTreeBuilder.get_tree(tree)

    console = rich.get_console()
    console.print(rich_tree)

    # root
    # └── module
    #     ├── future_import_statement
    #     │   ├── from
    #     │   ├── __future__
    #     │   ├── import
    #     │   └── dotted_name [field: name]
    #     │       └── identifier `annotations`
    #     ├── import_from_statement
    #     │   ├── from
    #     │   ├── dotted_name [field: module_name]
    #     │   │   └── identifier `pathlib`
    #     │   ├── import
    #     │   └── dotted_name [field: name]
    #     │       └── identifier `Path`
    #     ├── import_from_statement
    #     │   ├── from
    # ...
