import pytest
from sneksitter.fray.utils import Position, Range, offset_for_position, position_for_offset


# Test cases for Position class
def test_position_initialization():
    # Creating position object and verifying its attributes
    pos = Position(1, 2)
    assert pos.line == 1
    assert pos.column == 2


def test_position_moved_by():
    # Verifying the moved position produced correctly
    pos = Position(1, 2)
    new_pos = pos.moved_by(1, 2)
    assert new_pos.line == 2
    assert new_pos.column == 4


def test_equality():
    # Ensuring the equality operator functions properly
    pos1 = Position(1, 2)
    pos2 = Position(1, 2)
    assert pos1 == pos2


def test_less_than():
    # Ensuring the less than operator works correctly between Position objects
    pos1 = Position(1, 2)
    pos2 = Position(2, 3)
    assert pos1 < pos2


# Test cases for Range class
def test_range_contains():
    # Defining a range and confirming if it includes a given position
    start = Position(1, 2)
    end = Position(3, 4)
    my_range = Range(start, end)
    pos = Position(2, 3)
    assert pos in my_range


def test_range_contains_not():
    # Confirming a range does not include a given position
    start = Position(1, 2)
    end = Position(3, 4)
    my_range = Range(start, end)
    pos = Position(4, 5)
    assert pos not in my_range


# Test cases for offset and position conversion functions
def test_offset_for_position():
    # Verifying offset value produced is correct for a given position
    text = b"Hello\nWorld"
    position = Position(1, 1)
    assert offset_for_position(text, position) == 7


def test_position_for_offset():
    # Verifying position is correctly identified from offset
    text = b"Hello\nWorld"
    offset = 7
    assert position_for_offset(text, offset) == Position(1, 1)


# Handle edge cases -may result in Raised Exceptions
def test_position_for_offset_out_of_bounds():
    # Out of bounds case - offset exceeds text length
    text = b"Hello\nWorld"
    offset = 20
    with pytest.raises(ValueError):
        position_for_offset(text, offset)


def test_offset_for_position_out_of_bounds():
    # Out of bounds case - line number exceeds text lines
    text = b"Hello\nWorld"
    position = Position(5, 5)
    with pytest.raises(ValueError):
        offset_for_position(text, position)


# Additional test cases for Position class
def test_position_with_line():
    # Changing the line number of Position object
    pos = Position(1, 2)
    new_pos = pos.with_line(3)
    assert new_pos.line == 3
    assert new_pos.column == 2


def test_position_with_column():
    # Changing the column number of Position object
    pos = Position(1, 2)
    new_pos = pos.with_column(3)
    assert new_pos.line == 1
    assert new_pos.column == 3


# def test_position_addition():
#     # Addition of two Position objects
#     pos1 = Position(1, 2)
#     pos2 = Position(2, 3)
#     pos3 = pos1 + pos2
#     assert pos3.line == 3
#     assert pos3.column == 5
#
#
# def test_position_subtraction():
#     # Subtraction between two Position objects
#     pos1 = Position(3, 5)
#     pos2 = Position(1, 2)
#     pos3 = pos1 - pos2
#     assert pos3.line == 2
#     assert pos3.column == 3


def test_position_to_string():
    pos = Position(1, 2)
    assert str(pos) == "1:2"


# Additional test case for Range class
def test_range_to_string():
    start = Position(1, 2)
    end = Position(3, 4)
    my_range = Range(start, end)
    assert str(my_range) == "1:2..3:4"
