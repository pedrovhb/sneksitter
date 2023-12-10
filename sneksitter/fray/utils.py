from __future__ import annotations

from io import BytesIO
from typing import NamedTuple

from intervaltree import Interval
from tree_sitter import Node


class Position(NamedTuple):
    """A class representing a position in a text file.

    Attributes:
        line: The line number.
        column: The column number.

    Examples:
        >>> pos = Position(1, 2)
        >>> pos
        Position(line=1, column=2)
        >>> pos > Position(4, 4)
        False
    """

    line: int
    column: int

    def moved_by(self, lines: int = 0, columns: int = 0) -> Position:
        """Returns a new position moved by the specified amount from the current position.

        Args:
        lines: The number of lines to move. Defaults to 0.
        columns: The number of columns to move. Defaults to 0.

        Returns:
        New Position object that specifies the moved position.

        Examples:
        >>> pos = Position(0, 0)
        >>> pos.moved_by(2, 2)
        Position(line=2, column=2)
        """
        return Position(line=self.line + lines, column=self.column + columns)

    def with_line(self, line: int) -> Position:
        return Position(line=line, column=self.column)

    def with_column(self, column: int) -> Position:
        return Position(line=self.line, column=column)

    #
    # def __add__(self, other: Position) -> Position:
    #     new_line = self.line + other.line
    #     new_column = self.column + other.column if self.line == other.line else other.column
    #     return Position(line=new_line, column=new_column)
    #
    # def __sub__(self, other: Position) -> Position:
    #     new_line = self.line - other.line
    #     new_column = self.column - other.column if self.line == other.line else self.column
    #     return Position(line=new_line, column=new_column)

    def __eq__(self, other: tuple[int, int] | Position) -> bool:
        return tuple(self) == tuple(other)

    def __add__(self, other: tuple[int, int] | Position) -> Position:
        # If the other is a tuple, we assume it's a (line, column) tuple
        if isinstance(other, tuple):
            other = Position(*other)

        # Since we're working with cursor-like positions, logic is a bit
        # more involved than simply adding the two positions. For example,
        # say we have a position indicated by `|` in some text contents below:
        #
        # Position: (1, 15)
        #
        #     import math
        #     for i in range|(10):
        #         print(math.sqrt(i))
        #
        # If we want to add a position to this one, we need to take into account
        # the fact that the position we're adding might be on a different line.
        # Let's see the cases possible here:
        #
        # 1. The position we're adding is on the same line as the current position.
        #
        #     Position: (1, 15) + (0, 4) = (1, 19)
        #
        #         import math
        #         for i in range(10)|:
        #             print(math.sqrt(i))
        #
        #     In this case, we simply add the column numbers.
        #
        # 2. The position we're adding is on a different line than the current position.
        #
        #     Position: (1, 15) + (1, 4) = (2, 4)
        #
        #         import math
        #         for i in range(10):
        #         |    print(math.sqrt(i))
        #
        #     In this case, we add the line numbers and set the column number to the
        #     column number of the position we're adding.

    def __lt__(self, other: tuple[int, int] | Position) -> bool:
        if self.line < other[0]:
            return True
        if self.line > other[0]:
            return False
        if self.column < other.column:
            return True
        if self.column > other.column:
            return False
        return False

    def __str__(self) -> str:
        return f"{self.line}:{self.column}"

    def __repr__(self) -> str:
        return f"Position(line={self.line}, column={self.column})"

    def offset_for_text(self, text: bytes) -> int:
        return offset_for_position(text, self)

    @classmethod
    def from_text_offset(
        cls,
        text: bytes,
        offset: int = -1,
        initial_position: Position | None = None,
    ) -> Position:
        initial_position = initial_position or Position(0, 0)
        if offset < 0:
            offset = len(text) + offset + 1
        return position_for_offset(text=text, offset=offset, initial_position=initial_position)


class Range(Interval):
    """A class representing a range in a text file.

    Attributes:
        start: The start position of the range.
        end: The end position of the range.

    Examples:
        >>> start = Position(1, 2)
        >>> end = Position(3, 4)
        >>> my_range = Range(start, end)
        >>> my_range
        Range(start=1:2, end=3:4)
        >>> str(my_range)
        '1:2..3:4'
        >>> Position(2, 3) in my_range
        True
        >>> ((2, 2), (3, 3)) in my_range
        True
    """

    start: Position
    end: Position

    def __contains__(
        self,
        other: Range | Position | tuple[int, int] | tuple[tuple[int, int], tuple[int, int]],
    ) -> bool:
        match other:
            case (int(post_line), int(pos_col)):
                return self.start <= (post_line, pos_col) <= self.end
            case ((int(start_line), int(start_col)), (int(end_line), int(end_col))):
                return self.start <= (start_line, start_col) <= (end_line, end_col) <= self.end
            case _:
                raise TypeError(f"Invalid type for Range.__contains__: {type(other)}")

    def shifted_by(self, lines: int = 0, columns: int = 0) -> Range:
        return Range(
            start=self.start.moved_by(lines, columns), end=self.end.moved_by(lines, columns)
        )

    def __str__(self) -> str:
        return f"{self.start}..{self.end}"

    def __repr__(self) -> str:
        return f"Range(start={self.start}, end={self.end})"

    @classmethod
    def from_ts_node(cls, node: Node) -> Range:
        start = Position(*node.start_point)
        end = Position(*node.end_point)
        return cls(start=start, end=end)


class Block:
    """Contains information about a block of text, i.e. bytes contents, and
    start and end positions.
    """

    contents: bytes
    span: Interval

    def __contains__(self, other: Range | Position) -> bool:
        return self.start <= other <= self.end

    def __str__(self) -> str:
        return f"{self.start}..{self.end}"

    def __repr__(self) -> str:
        return f"Block(start={self.start}, end={self.end})"


def offset_for_position(text: bytes, position: Position) -> int:
    """Returns the offset for a given position in the text.

    Args:
        text: The text to find the offset in.
        position: The position to find the offset for.

    Returns:
        The offset for the given position.

    Raises:
        ValueError: If the position is out of bounds.

    Examples:
        >>> text = b"Hello\\nWorld"
        >>> position = Position(1, 1)
        >>> offset_for_position(text, position)
        7
    """

    row = 0
    offset = 0
    new_line_indices = [i for i, b in enumerate(text) if b == ord(b"\n")]

    for pos in new_line_indices:
        if row < position.line:
            row += 1
            offset = pos + 1
        else:
            break

    if position.line - row > 0:
        raise ValueError(f"Failed to find offset for position: {position} (line out of bounds)")

    if len(new_line_indices) > row:
        if (new_line_indices[row] - offset < position.column) or (
            text[offset] == ord("\n") and position.column > 0
        ):
            raise ValueError(
                f"Failed to find offset for position: {position} (column out of bounds)"
            )
    elif len(text) - offset < position.column:
        raise ValueError(f"Failed to find offset for position: {position} (column out of bounds)")

    return offset + position.column


def position_for_offset(text: bytes, offset: int, initial_position=Position(0, 0)) -> Position:
    """Returns the position for a given offset in the text.

    Args:
        text: The text to find the position in.
        offset: The offset to find the position for.
        initial_position: The initial position to start from. Defaults to (0, 0).

    Returns:
        The position for the given offset.

    Raises:
        ValueError: If the offset is out of bounds.

    Examples:
        >>> text = b"Hello\\nWorld"
        >>> offset = 7
        >>> position_for_offset(text, offset)
        Position(line=1, column=1)
    """
    if offset > len(text):
        raise ValueError(f"Failed to address an offset: {offset} (out of bounds)")
    result_line = 0
    last = 0
    for pos in range(offset):
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


class BufWithCursor:
    def __init__(self, initial_contents: bytes = b"") -> None:
        self._buf = BytesIO(initial_contents)
        self._cursor_position = Position.from_text_offset(initial_contents, offset=0)
        self._cursor_offset = self._cursor_position.offset_for_text(initial_contents)

    # def insert(self, text: bytes) -> None:
    #     self._buf.write(text)
    #     self._cursor_offset += len(text)
    #     self._cursor_position = Position.from_text_offset(self._buf.getvalue(), offset=self._cursor_offset)

    def insert(self, text: bytes, pos: Position | None = None) -> None:
        if pos is None:
            pos = self._cursor_position

        self._cursor_position = pos
        displacement = location.end.offset_for_text(
            self._buf.getvalue()
        ) - location.start.offset_for_text(self._buf.getvalue())

        line_diff = pos.line - self._cursor_position.line
        crt_column = self._cursor_position.column
        if line_diff > 0:
            self._buf.write(b"\n" * line_diff)
            self._cursor_offset += line_diff
            self._cursor_position = self._cursor_position.moved_by(line_diff, 0)
            crt_column = 0

        indentation = pos.column - crt_column
        lines = text.split(b"\n")
        self._buf.write(b" " * indentation)
        self._buf.write(lines[0])
        self._cursor_offset += indentation + len(lines[0])
        self._cursor_position = self._cursor_position.moved_by(0, indentation + len(lines[0]))
        for line in lines[1:]:
            self._buf.write(b"\n")
            self._buf.write(b" " * indentation)
            self._buf.write(line)
            self._cursor_offset += 1 + indentation + len(line)
            self._cursor_position = self._cursor_position.moved_by(1, indentation + len(line))

        # After inserting the text, we need to move the cursor to the end of the inserted text
        if self._cursor_position > location.end:
            raise ValueError("Cursor position is out of bounds")

        # Insert additional newlines and spaces if needed
        line_diff = location.end.line - self._cursor_position.line
        if line_diff > 0:
            self._buf.write(b"\n" * line_diff)
            self._cursor_offset += line_diff
            self._cursor_position = self._cursor_position.moved_by(line_diff, 0)
            crt_column = 0

        indentation = location.end.column - self._cursor_position.column
        if indentation > 0:
            self._buf.write(b" " * indentation)
            self._cursor_offset += indentation
            self._cursor_position = self._cursor_position.moved_by(0, indentation)

    def delete(self, start: Position, end: Position) -> None:
        start_offset = start.offset_for_text(self._buf.getvalue())
        end_offset = end.offset_for_text(self._buf.getvalue())
        self._buf.seek(start_offset)
        self._buf.truncate(end_offset - start_offset)
        self._cursor_offset = start_offset
        self._cursor_position = start

    def replace(self, start: Position, end: Position, text: bytes) -> None:
        self.delete(start, end)
        self.insert(text, Range(start, end))

    def move_cursor(self, position: Position) -> None:
        self._cursor_position = position
        self._cursor_offset = position.offset_for_text(self._buf.getvalue())

    def render(self) -> bytes:
        return self._buf.getvalue()


if __name__ in ("__main__", "__live_coding__"):
    pos = Position.from_text_offset(b"hello")
    print(pos)  # Position(line=0, column=5)
    print(pos.offset_for_text(b"hello"))  # 5

    pos_2 = Position.from_text_offset(b"hello", offset=-2)
    print(pos_2)  # Position(line=0, column=4)
    print(pos_2.offset_for_text(b"hello"))  # 4

    sample = b"import math\n\nfor i in range(10):\n    print(math.sqrt(i))\n"
    #       0     5      10      15      20      25      30      35      40
    #   0   import math
    #   1
    #   2   for i in range(10):
    #   3       print(math.sqrt(i))
    #   4

    pos_sample = Position.from_text_offset(sample)
    print(pos_sample)  # Position(line=4, column=0)
    print(pos_sample.offset_for_text(sample))  # 57
    pos_sample_2 = Position.from_text_offset(sample, offset=-2)
    print(pos_sample_2)  # Position(line=3, column=23)
    print(pos_sample_2.offset_for_text(sample))  # 56
    print(sample[:56])

    pos = Position.from_text_offset(b"123\n567\n89")
    print(pos)  # Position(line=2, column=2)
    print(pos.offset_for_text(b"123\n567\n89"))  # 10
    pos = pos.moved_by(lines=-1)
