from __future__ import annotations

import argparse
import itertools
import re
import sys
from io import BytesIO
from pathlib import Path
from typing import Callable, Iterable, Sequence

from tree_sitter import Node as TSNode, Parser, Tree
from anytree import NodeMixin as AnyNodeMixin
from intervaltree import Interval, IntervalTree

from sneksitter.fray.utils import Range, Position, BufWithCursor

import snoop

snoop.install(columns="")


def get_whitespace_to_position(from_pos: Position, to_pos: Position) -> bytes:
    """
    Calculate the whitespace needed to move from one position to another in a text.

    Args:
    - from_pos (Position): The starting position.
    - to_pos (Position): The ending position.

    Returns:
    - bytes: A sequence of whitespace bytes.
    """
    if from_pos.line == to_pos.line:
        return b" " * (to_pos.column - from_pos.column)
    else:
        return b"\n" * (to_pos.line - from_pos.line) + b" " * to_pos.column


class SNode(AnyNodeMixin):
    """
    A class representing a syntax node in a syntax tree.

    Attributes:
    - type (str): The type of the syntax node.
    - text (bytes): The text content of the node.
    - is_named (bool): Indicates if the node is named.
    - location (Range): The location of the node in the source code.
    - children (list[SNode]): The child nodes.
    - children_idx_to_field (dict[int, str | None]): Maps child indices to field names.
    - parent (SNode | None): The parent node.
    """

    def __init__(
        self,
        type: str,
        text: bytes,
        is_named: bool,
        location: Range,
        start_byte: int,
        end_byte: int,
        children: list[SNode] | None = None,
        children_idx_to_field: dict[int, str | None] | None = None,
        parent: SNode | None = None,
        text_change_callbacks: Sequence[Callable[[SNode, bytes], None]] | None = None,
    ):
        children = children or []
        children_idx_to_field = children_idx_to_field or {}

        super().__init__()
        self.type = type
        self._text = text
        self.is_named = is_named
        self.location = location
        self.children = children
        self.children_idx_to_field = children_idx_to_field
        self.parent = parent
        self._text_change_callbacks = text_change_callbacks or []
        self.start_byte = start_byte
        self.end_byte = end_byte

    def add_text_change_callback(self, callback: Callable[[SNode, bytes], None]) -> None:
        """Add a callback to be called when the text of the node changes."""
        self._text_change_callbacks.append(callback)

    @property
    def text(self) -> bytes:
        """Return the text content of the node."""
        return self._text

    @text.setter
    def text(self, value: bytes) -> None:
        self._text = value
        for callback in self._text_change_callbacks:
            callback(self, value)

    @property
    def is_leaf(self) -> bool:
        """Return True if the node is a leaf node (has no children)."""
        return len(self.children) == 0

    @property
    def is_root(self) -> bool:
        """Return True if the node is the root node (has no parent)."""
        return self.parent is None

    @property
    def fields(self) -> dict[str, SNode]:
        """Return a dictionary mapping field names to child nodes."""
        return {
            field_name: child
            for field_name, child in zip(self.children_idx_to_field.values(), self.children)
            if field_name is not None
        }

    @classmethod
    def from_ts_node(cls, node: TSNode, parent: SNode | None = None) -> SNode:
        """
        Create an SNode instance from a tree_sitter Node.

        Args:
        - node (TSNode): The tree_sitter node.
        - parent (SNode | None): The parent SNode.

        Returns:
        - SNode: The created SNode instance.
        """

        if node.type == "string":
            # todo - figure out why this is different from other cases.
            #  The string node (at least in the Python parser) only has children
            #  nodes for the delimiter (i.e. both `"` characters), and the actual
            #  contents of the string literal are not represented.
            #  If you breakpoint here you'll see the node looks like
            #      >>> node
            #      <Node type=string, start_point=(14, 15), end_point=(14, 25)>
            #      >>> node.children
            #      [<Node type=""", start_point=(14, 15), end_point=(14, 16)>,
            #       <Node type=""", start_point=(14, 24), end_point=(14, 25)>]
            #      >>> node.text, node.child_count
            #      (b'"__main__"', 2)
            #      >>> [(child.type, child.text) for child in node.children]
            #      ...  [('"', b'"'), ('"', b'"')]  # contents missing :(
            #  This is a bit scary because string literals are kind of important. This
            #  is likely due to something like patterns being external, I think. One way
            #  we *could* probably generically handle this case is to check if the range
            #  covered by children is populated with characters in the code contents? Still
            #  tricky as e.g. there may be valid formatting in cases like
            #      a =    1234
            #      b =      12
            #  Further, there may be valid code which does
            #      e = "     "
            #  This could be a bit tricky but for now we stick to explicitly checking for
            #  the "string" node type and handling it separately.
            #  For now, we just return a leaf node with the text of the string literal.
            return cls(
                type=node.type,
                text=node.text,
                is_named=node.is_named,
                location=Range.from_ts_node(node),
                start_byte=node.start_byte,
                end_byte=node.end_byte,
                children=[],
                children_idx_to_field={},
                parent=parent,
            )

        children = [cls.from_ts_node(child) for child in node.children]
        idx_to_field = {}
        for i, (ts_node, s_node) in enumerate(zip(node.children, children)):
            field_name = ts_node.field_name_for_child(i)
            idx_to_field[i] = field_name

        return cls(
            type=node.type,
            text=node.text,
            is_named=node.is_named,
            location=Range.from_ts_node(node),
            children=children,
            children_idx_to_field=idx_to_field,
            parent=parent,
        )

    def render(
        self,
        transform_fn: Callable[[SNode, bytes], bytes] | None = None,
    ) -> bytes:
        """
        Render the syntax node and its children to bytes.

        Args:
        - transform_fn (Callable[[SNode, bytes], bytes] | None): A function to transform the rendered bytes.

        Returns:
        - bytes: The rendered byte sequence.
        """
        if transform_fn is None:
            transform_fn = lambda node, rendered_raw: rendered_raw

        # Base case
        if self.is_leaf:
            rendered_raw = self.text
            return transform_fn(self, rendered_raw)

        rendered_els = []
        # get whitespace to first child
        first_child = self.children[0]
        rendered_els.append(
            get_whitespace_to_position(self.location.start, first_child.location.start)
        )
        for a, b in itertools.pairwise(self.children):
            rendered_els.append(a.render(transform_fn))
            rendered_els.append(get_whitespace_to_position(a.location.end, b.location.start))
        rendered_els.append(self.children[-1].render(transform_fn))
        raw_text = b"".join(rendered_els)
        return transform_fn(self, raw_text)

    def __repr__(self) -> str:
        return f"<SNode {self.type} {self.location}>"

    __str__ = __repr__


class CodeFile:
    """
    A class representing a code file and its syntax tree.

    Attributes:
    - text (bytes): The content of the code file.
    - path (Path | None): The path of the code file.
    - parser (Parser): The tree_sitter parser.
    """

    def __init__(self, text: bytes, parser: Parser, path: Path | None = None):
        self.text = text
        self.path = path
        self.parser = parser

        self.s_tree = SNode.from_ts_node(self.ts_tree.root_node)
        self._interval_tree = self._build_interval_tree(self.s_tree)

    def replace(self, s_node: SNode, replacement: bytes) -> None:
        """
        Replace a range of bytes in the code file.

        Args:
        - s_node (SNode): The syntax node to replace.
        - replacement (bytes): The replacement bytes.
        """
        # Find the corresponding SNode in the syntax tree
        intervals = self._interval_tree[s_node.location.start : s_node.location.end]
        if not intervals:
            raise ValueError("The specified node does not exist in the syntax tree.")

        # Replace the text of the found SNode
        for interval in intervals:
            if interval.data == s_node:
                interval.data.text = replacement
                break
        else:
            raise ValueError("The specified node does not exist in the syntax tree.")

        # Rebuild the interval tree
        self._interval_tree = IntervalTree()
        self._build_interval_tree(self.s_tree)

    def _build_interval_tree(self, s_tree: SNode, _tree: IntervalTree = None) -> IntervalTree:
        """
        Build the interval tree for the syntax tree.

        Args:
        - s_tree (SNode): The root node of the syntax tree.
        """
        i_tree = _tree or IntervalTree()
        i_tree.addi(s_tree.location.start, s_tree.location.end, s_tree)
        for child in s_tree.children:
            self._build_interval_tree(child, i_tree)
        return i_tree

    def nodes_at(self, pos: Position) -> tuple[SNode, ...]:
        """
        Get the syntax node(s) at a given position.

        Args:
        - pos (Position): The position in the code file.

        Returns:
        - tuple[SNode, ...]: The node(s) at the given position.
        """
        intervals = self._interval_tree.at(pos)
        if not intervals:
            return ()
        return tuple(iv.data for iv in intervals)

    @property
    def ts_tree(self) -> Tree:
        """Return the tree_sitter Tree for the code file."""
        return self.parser.parse(self.text)

    def render(self, transform_fn: Callable[[SNode, bytes], bytes] | None = None) -> bytes:
        """
        Render the entire syntax tree to bytes.

        Args:
        - transform_fn (Callable[[SNode, bytes], bytes] | None): A function to transform the rendered bytes.

        Returns:
        - bytes: The rendered byte sequence.
        """
        return self.s_tree.render(transform_fn)

    def node_for_range(self, range: Range) -> SNode:
        """
        Get the syntax node for a given range.

        Args:
        - range (Range): The range in the code file.

        Returns:
        - SNode: The node for the given range.
        """
        intervals = self._interval_tree[range.start : range.end]
        if not intervals:
            raise ValueError("The specified range does not exist in the syntax tree.")
        for interval in intervals:
            if interval.data.location == range:
                return interval.data
        else:
            raise ValueError("The specified range does not exist in the syntax tree.")


def tag_fn(node: SNode, rendered_raw: bytes) -> bytes:
    """
    Custom function to tag certain types of nodes in the syntax tree.

    Args:
    - node (SNode): The syntax node.
    - rendered_raw (bytes): The raw rendered bytes of the node.

    Returns:
    - bytes: The tagged byte sequence.
    """
    is_tagged_type = node.type in {
        "function_definition",
        "class_definition",
        "except_clause",
        "pass_statement",
        "raise_statement",
        "decorated_definition",
        "nonlocal_statement",
        "for_statement",
        "delete_statement",
        "finally_clause",
        "while_statement",
        "type_alias_statement",
        "case_clause",
        "if_statement",
        "decorator",
        "print_statement",
        "comment",
        "assert_statement",
        "for_in_clause",
        "import_statement",
        "elif_clause",
        "return_statement",
        "expression_statement",
        "else_clause",
        "break_statement",
        "global_statement",
        "import_from_statement",
        "exec_statement",
        "match_statement",
        "parameters",
        "except_group_clause",
        "with_statement",
        "future_import_statement",
        "continue_statement",
        "try_statement",
    }
    has_named_children = any(child.is_named for child in node.children)
    if is_tagged_type and has_named_children:
        loc_str = str(node.location).replace("..", "–")
        return b"".join((f"»{loc_str}【".encode(), rendered_raw, "】".encode()))
    return rendered_raw


def demo() -> None:
    sample_code_file = Path("/home/pedro/projs/sneksitter/sneksitter/fray/sample_code.py")
    sample_code_contents = sample_code_file.read_bytes()
    samples = {}
    for sample in sample_code_contents.split(b"\n# "):
        sample_name, sample_code = sample.split(b"\n", 1)
        samples[sample_name.decode()] = sample_code

    for sample_name, code in samples.items():
        code_file = CodeFile(code, parser)
        print(f"# Sample {sample_name}")
        # print(n := code_file.get_node_at(Position(0, 0)), [nn.text for nn in n])
        # print(n := code_file.get_node_at(Position(1, 5)), [nn.text for nn in n])
        # print(code_file.s_tree.render().decode())
        print(code_file.s_tree.render(tag_fn).decode())


if __name__ in ("__main__", "__live_coding__"):
    import tree_sitter_languages

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "file", type=argparse.FileType("rb"), nargs="?", help="The file to parse"
    )
    arg_parser.add_argument("--demo", action="store_true", help="Run the demo")
    arg_parser.add_argument("-l", "--language", default="python", help="The language to parse")
    arg_parser.add_argument(
        "-C", "--copy", action="store_true", help="Store the result to clipboard"
    )

    args = arg_parser.parse_args()

    parser = tree_sitter_languages.get_parser(args.language)
    if args.demo:
        demo()
        exit()

    code_file = CodeFile(args.file.read(), parser)
    result = code_file.s_tree.render(tag_fn).decode()

    if args.copy:
        try:
            import pyperclip

            pyperclip.copy(result)
            print("<copied to clipboard>", file=sys.stderr)
        except ImportError:
            print("pyperclip not installed", file=sys.stderr)
    print(result)

    fut_ann_identifier_node = code_file.s_tree.children[0].children[-1].children[-1]
    print(fut_ann_identifier_node)
    code_file.replace(fut_ann_identifier_node, b"str")
    print(code_file.s_tree.render().decode())
