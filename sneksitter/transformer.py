from __future__ import annotations

from typing import Any, NamedTuple

from tree_sitter import Node, Tree, Parser

from sneksitter.visitor import (
    BaseVisitor,
    NotRunSentinel,
)


class BaseTransformer(BaseVisitor):
    def __init__(self, parser: Parser) -> None:
        super().__init__()
        self._parser = parser
        self._replacements: set[NodeReplacement] = set()

    def add_replacement(
        self,
        node: Node,
        replacement: str | bytes,
    ) -> None:
        if isinstance(replacement, str):
            replacement = replacement.encode()
        if node.id in self._replacements:
            raise ValueError(f"Node {node} already has a replacement")
        # We'll add the replacement to the dictionary with order - order is
        # determined by the start byte of the node, and if two nodes have the
        # same start byte, we'll use the end byte to determine order.

        self._replacements.add(NodeReplacement(node=node, replacement=replacement))

    def _handle_leave_return_value(
        self,
        original_node: Node,
        return_value: Any,
    ) -> None:
        """Handle the return value of a leave method."""
        if return_value is not NotRunSentinel and return_value is not None:
            self.add_replacement(original_node, return_value)

    @classmethod
    def transform(cls, tree: Tree, parser: Parser) -> Tree:
        """Class method to traverse the tree and call the visitor's methods."""
        transformer = cls.traverse_tree(tree, parser=parser)
        return transformer._transform(tree)

    def _transform(self, tree: Tree) -> Tree:
        """Transform the tree."""
        source = tree.text
        replacements = sorted(
            self._replacements,
            key=lambda r: (r.node.start_byte, -r.node.end_byte),
            reverse=True,
        )
        for node, replacement in replacements:
            code = replacement
            if isinstance(code, str):
                code = code.encode()
            source = source[: node.start_byte] + code + source[node.end_byte :]

            tree.edit(
                start_byte=node.start_byte,
                old_end_byte=node.end_byte,
                new_end_byte=node.start_byte + len(code),
                start_point=node.start_point,
                old_end_point=node.end_point,
                new_end_point=node.end_point,
            )

        return self._parser.parse(source, tree)


class NodeReplacement(NamedTuple):
    node: Node
    replacement: bytes

    def __hash__(self) -> int:
        return hash(self.node.id) ^ hash(self.replacement)
