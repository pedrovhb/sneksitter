from __future__ import annotations

from pathlib import Path
from typing import Any, NamedTuple

from tree_sitter import Node, Tree, Parser

from sneksitter.utils import CodeT, normalize_code
from sneksitter.visitor import BaseVisitor


class BaseTransformer(BaseVisitor):
    def __init__(self, parser: Parser) -> None:
        super().__init__()
        self._parser = parser
        self._replacements = dict[int, NodeReplacement]()

    def add_replacement(self, node: Node, replacement_code: CodeT) -> None:
        if node.id in self._replacements:
            raise ValueError(f"Node {node} already has a replacement")

        replacement_code = normalize_code(replacement_code)
        replacement = NodeReplacement(node=node, replacement=replacement_code)
        self._replacements[node.id] = replacement

    def _handle_leave_return_value(
        self,
        original_node: Node,
        return_value: CodeT,
    ) -> None:
        """Handle the return value of a leave method."""
        if return_value:
            self.add_replacement(original_node, return_value)

    # def transform(self, root_node: Tree, parser: Parser) -> Tree:
    #     """Class method to traverse the root_node and call the visitor's methods."""

    def transform(
        self,
        tree: Tree | str | bytes | Path,
        do_traverse: bool = True,
    ) -> Tree:
        """Transform the root_node."""

        if isinstance(tree, str):
            tree = tree.encode()
        elif isinstance(tree, Path):
            tree = tree.read_bytes()

        if isinstance(tree, bytes):
            tree = self._parser.parse(tree)

        if do_traverse:
            self.traverse(tree)
        source = tree.text
        replacements = sorted(
            self._replacements.values(),
            key=lambda r: (r.root_node.start_byte, -r.root_node.end_byte),
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
