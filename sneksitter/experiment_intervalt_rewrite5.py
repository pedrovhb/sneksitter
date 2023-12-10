from __future__ import annotations

import io
import textwrap
from typing import Iterable, NamedTuple, Sequence

import tree_sitter_languages
from anytree import NodeMixin as AnyNodeMixin
from tree_sitter import Node


def offset_for_position(text: bytes, position: Position) -> int:
    row = 0
    offset = 0
    new_line_indices = [i for i, b in enumerate(text) if b == ord("\n")]

    for pos in new_line_indices:
        if row < position.line:
            row += 1
            offset = pos + 1
        else:
            break

    if position.line - row > 0:
        raise Exception(f"Failed to address a row: {position.line}")

    if len(new_line_indices) > row:
        if (new_line_indices[row] - offset < position.column) or (
            text[offset] == ord("\n") and position.column > 0
        ):
            raise Exception(f"Failed to address a column: {position.column}")
    elif len(text) - offset < position.column:
        raise Exception("Failed to address a column over the end")

    return offset + position.column


def position_for_offset(text: bytes, offset: int, initial_position=Position(0, 0)) -> Position:
    if offset > len(text):
        raise Exception(f"Failed to address an offset: {offset}")
    result_line = 0
    last = 0
    for pos in range(offset):
        print(text[pos])
        if text[pos] == ord(b"\n"):
            result_line += 1
            last = pos
    if result_line > 0:
        result_column = offset - last - 1
    else:
        result_column = offset
    return Position(
        line=result_line + initial_position.line,
        column=result_column + initial_position.column,
    )


class Position(NamedTuple):
    line: int
    column: int

    def move_lines(self, lines: int) -> Position:
        return Position(line=self.line + lines, column=self.column)

    def move_columns(self, columns: int) -> Position:
        return Position(line=self.line, column=self.column + columns)

    def set_line(self, line: int) -> Position:
        return Position(line=line, column=self.column)

    def set_column(self, column: int) -> Position:
        return Position(line=self.line, column=column)

    def __str__(self) -> str:
        return f"{self.line}:{self.column}"

    def __repr__(self) -> str:
        return f"Position(line={self.line}, column={self.column})"

    def __add__(self, other: Position) -> Position:
        new_line = self.line + other.line
        new_column = self.column + other.column if self.line == other.line else other.column
        return Position(line=new_line, column=new_column)

    def __sub__(self, other: Position) -> Position:
        new_line = self.line - other.line
        new_column = self.column - other.column if self.line == other.line else self.column
        return Position(line=new_line, column=new_column)


class Range(NamedTuple):
    start: Position
    end: Position

    def __contains__(self, other: Range) -> bool:
        return self.start <= other.start and self.end >= other.end

    def __str__(self) -> str:
        return f"{self.start}..{self.end}"

    def __repr__(self) -> str:
        return f"Range(start={self.start}, end={self.end})"

    @classmethod
    def from_ts_node(cls, node: Node) -> Range:
        return cls(
            start=Position(line=node.start_point[0], column=node.start_point[1]),
            end=Position(line=node.end_point[0], column=node.end_point[1]),
        )


def indent_to_column(text: bytes, column: int) -> bytes:
    """Add indentation to the given text to match the given column"""
    indentation = b" " * column
    return indentation + text.replace(b"\n", b"\n" + indentation)


def dedent_bytes(text: bytes) -> bytes:
    """Transform similarly to textwrap.dedent, but with bytes."""
    lines = text.split(b"\n")
    min_indent = min(len(line) - len(line.lstrip()) for line in lines if line.strip())
    return b"\n".join(line[min_indent:] for line in lines)


class IntervalNode(AnyNodeMixin, Sequence["IntervalNode"]):
    def __len__(self) -> int:
        if not self.children:
            return 1
        return 1 + len(self.children)

    def __getitem__(self, idx: int) -> IntervalNode:
        return list(self)[idx]

    def __init__(
        self,
        range: Range,
        text: bytes,
        type: str,
        field_name: str | None = None,
        children_field_indexes: dict[str, int] | None = None,
        children: list[IntervalNode] | None = None,
        parent: IntervalNode | None = None,
    ) -> None:
        self.range = range
        self.text = text
        self.type = type
        self.field_name = field_name
        self.children_field_indexes = children_field_indexes

        self.children = children
        self.parent = parent

    @classmethod
    def from_ts_node(cls, node: Node, __field_name: str | None = None) -> IntervalNode:
        children_field_indexes = {}
        field_names = []
        for i, child in enumerate(node.children):
            field_name = node.field_name_for_child(i)
            if field_name is not None:
                children_field_indexes[field_name] = i
            field_names.append(field_name)

        return cls(
            range=Range(
                start=Position(line=node.start_point[0], column=node.start_point[1]),
                end=Position(line=node.end_point[0], column=node.end_point[1]),
            ),
            text=node.text,
            type=node.type,
            field_name=__field_name,
            children_field_indexes=children_field_indexes,
            children=[
                cls.from_ts_node(child, field_name)
                for child, field_name in zip(node.children, field_names)
            ],
        )

    def __repr__(self) -> str:
        snippet = textwrap.shorten(self.text.decode(), width=20, placeholder="...")
        cls_name = self.__class__.__name__
        return f"<{cls_name} {self.type} [{self.range}] {snippet}>"

    __str__ = __repr__

    def replace(self, replacement: bytes) -> None:
        replacement_indented = indent_to_column(replacement, self.range.start.column)
        end = position_for_offset(
            replacement_indented,
            len(replacement_indented),
            initial_position=self.range.start,
        )

        # self.end_byte = self.start_byte + len(replacement_indented)
        self.text = replacement
        self.range = Range(
            start=self.range.start,
            end=end,
        )
        # if self.parent is not None:
        #     self.parent.update(self, prev_text, prev_range)
        # raise NotImplementedError("TODO: Replace children?")

    def replace_range(self, replacement: bytes, range: Range) -> None:
        """Replace the given range with the given replacement text"""
        child_start = None
        child_end = None
        is_removing = False
        # for child in self:
        #     if child.range.start >= range.start and not is_removing:
        #         child.replace(replacement)
        #         is_removing = True
        #         continue
        #     if child.range.start > range.end and is_removing:
        #         break
        #     if is_removing:
        #         # child.parent = None
        #         child.replace(b"")

        for child in self:
            if child.range in range:
                child.replace(b"")
                print("fooo!", child)

    def render(self) -> bytes:
        """Return a rendered view of the node, adjusting for whitespace as necessary
        to provide correct indentation and whitespace between nodes.

        As an example:

            <IntervalNode def [0..6] [0:0..0:3] snippet='def'>
            <IntervalNode identifier [4..14] [0:4..0:7] snippet='add'>
            <IntervalNode ( [7..16] [0:7..0:8] snippet='('>
            <IntervalNode identifier [8..25] [0:8..0:25] snippet='something'>
            <IntervalNode , [11..24] [0:11..0:12] snippet=','>
            <IntervalNode identifier [13..36] [0:13..0:18] snippet='other'>
            <IntervalNode ) [18..38] [0:18..0:19] snippet=')'>
            <IntervalNode : [19..40] [0:19..0:20] snippet=':'>
            <IntervalNode return [25..41] [1:4..1:10] snippet='return'>
            <IntervalNode identifier [32..49] [1:11..1:14] snippet='one'>
            <IntervalNode + [36..53] [1:15..1:16] snippet='+'>
            <IntervalNode identifier [38..65] [1:17..1:22] snippet='other'>

        Becomes:

                def add(something, other):
                    return one + other
        """
        with io.BytesIO() as buffer:
            crt_line = 0
            crt_column = 0

            for child in self:
                line_diff = child.range.start.line - crt_line
                if line_diff > 0:
                    buffer.write(b"\n" * line_diff)
                    crt_line = child.range.start.line
                    crt_column = 0

                space_diff = child.range.start.column - crt_column
                if space_diff > 0:
                    buffer.write(b" " * space_diff)
                    crt_column = child.range.start.column

                buffer.write(child.text)
                crt_column = child.range.end.column
                crt_line = child.range.end.line

            return buffer.getvalue()
        #
        # rendered_children = []
        # crt_line = 0
        # crt_column = 0
        #
        # for child in self:
        #     while crt_line < child.range.start.line:
        #         crt_line += 1
        #         crt_column = 0
        #         rendered_children.append(b"\n")
        #
        #     while crt_column < child.range.start.column:
        #         crt_column += 1
        #         rendered_children.append(b" ")
        #
        #     text = child.text
        #
        #     rendered_children.append(text)
        #     crt_column = child.range.end.column
        #     crt_line = child.range.end.line
        #
        # return b"".join(rendered_children)


# todo - maybe divide into abstract nodes and concrete (leaf) nodes

code_a = b"""\
class Foo:
    def add(self, one, other):
        one = something - 1
        return one + other
"""

replace = ((0, 8), (0, 11), b"something")
replace = (Position(1, 18), Position(1, 21), b"something,\nelse_entirely,\na_third_one")
replace_range = Range(*replace[:2])
print(pos_a := offset_for_position(code_a, replace_range.start))
print(pos_b := offset_for_position(code_a, replace_range.end))
crt_text = code_a[pos_a:pos_b].decode()
replace_text = replace[2]

parser = tree_sitter_languages.get_parser("python")
ts_tree_a = parser.parse(code_a)

tree_a = IntervalNode.from_ts_node(ts_tree_a.root_node)
fn_def = ts_tree_a.root_node.children[0].children[-1].children[0]
fn_def_range = Range.from_ts_node(fn_def)

replace_range = fn_def_range
replace_text = b"""\
def multiply(self, a, b) -> int:
    return a * b
"""
print(tree_a)

tree_a.replace_range(replace_text, replace_range)

# for child in tree_a:
#     if child.range in replace_range:
#         print(f"!! Replacing: {child}")
#         child.replace(replace_text)
#         print(f"!! Replaced:  {child}")
#     else:
#         print(f"              {child}")
# print("---")
# for child in tree_a:
#     # print(child.text.decode(), end="")
#     print(child)

print()
print(tree_a.render().decode())


from difflib import SequenceMatcher

tree_b = IntervalNode.from_ts_node(parser.parse(code_a).root_node)
matcher = SequenceMatcher(a=tree_a, b=tree_b)
print(matcher.get_matching_blocks())
