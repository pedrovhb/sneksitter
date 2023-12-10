from __future__ import annotations

from typing import Iterable, NamedTuple, Callable

import tree_sitter_languages
from tree_sitter import Node


class NodeChild(NamedTuple):
    node: Node
    child_field_name: str | None
    child_index: int

    @property
    def child(self) -> Node:
        if self.child_field_name is not None:
            return self.node.child_by_field_name(self.child_field_name)
        return self.node.child(self.child_index)


class NodePath(NamedTuple):
    path: tuple[NodeChild, ...]

    @property
    def head(self) -> Node:
        return self.path[-1].child

    @property
    def tail(self) -> NodePath:
        return NodePath(self.path[:-1])

    @property
    def depth(self) -> int:
        return len(self.path)

    def append(self, child: NodeChild) -> NodePath:
        return NodePath(self.path + (child,))

    @classmethod
    def from_node_dfs(cls, node: Node) -> Iterable[NodePath]:
        yield NodePath((NodeChild(node, None, 0),))
        for child_index, child in enumerate(node.children):
            yield from (
                path.append(NodeChild(node, None, child_index)) for path in cls.from_node_dfs(child)
            )

    @classmethod
    def from_node_bfs(cls, node: Node) -> Iterable[NodePath]:
        yield NodePath((NodeChild(node, None, 0),))
        for child_index, child in enumerate(node.children):
            yield from (
                path.append(NodeChild(node, None, child_index)) for path in cls.from_node_bfs(child)
            )

    @classmethod
    def from_node_postorder(cls, node: Node) -> Iterable[NodePath]:
        for child_index, child in enumerate(node.children):
            yield from (
                path.append(NodeChild(node, None, child_index))
                for path in cls.from_node_postorder(child)
            )
        yield NodePath((NodeChild(node, None, 0),))

    @staticmethod
    def _default_node_repr(node_path: NodePath) -> str:
        return node_path.head.type

    def _ascii_tree(self, node_repr: Callable[[NodePath], str]) -> Iterable[str]:
        yield node_repr(self)
        for child_index, child in enumerate(self.head.children):
            yield from (
                "├─ " + line if i == 0 else "│  " + line
                for i, line in enumerate(
                    NodePath(self.path + (NodeChild(self.head, None, child_index),))._ascii_tree(
                        node_repr
                    )
                )
            )

    def ascii_tree(self, node_repr: Callable[[NodePath], str] | None = None) -> str:
        if node_repr is None:
            node_repr = self._default_node_repr
        return "\n".join(self._ascii_tree(node_repr))


if __name__ == "__main__" or __name__ == "__live_coding__":
    parser = tree_sitter_languages.get_parser("python")

    sample_code_bytes = b"""\
    def foo(x: list[str | int]) -> str:
        x = 1
        y = 4
        return str(y + x)[::-1]
    """
    tree = parser.parse(sample_code_bytes)

    for node_path in NodePath.from_node_dfs(tree.root_node):
        print(node_path.head.text)
