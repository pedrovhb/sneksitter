from __future__ import annotations

from dataclasses import dataclass
from numbers import Number
from typing import Generic, TypeVar, Protocol, runtime_checkable

from intervaltree import IntervalTree

_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)
_T_contra = TypeVar("_T_contra", contravariant=True)


# fmt: off
class _PositionProtocol(Protocol[_T]):
    def __eq__(self, __other: _T) -> bool: ...
    def __ge__(self, __other: _T) -> bool: ...
    def __gt__(self, __other: _T) -> bool: ...
    def __le__(self, __other: _T) -> bool: ...
    def __lt__(self, __other: _T) -> bool: ...
    def __add__(self, __other: _T) -> _T: ...
    def __sub__(self, __other: _T) -> _T: ...


@runtime_checkable
class SupportsLtGt(Protocol[_T_contra]):
    def __lt__(self, other: _T_contra) -> bool: ...
    def __gt__(self, other: _T_contra) -> bool: ...

# fmt: on

_PositionT = TypeVar("_PositionT", bound=_PositionProtocol)
_DataT = TypeVar("_DataT")


# noinspection PyBroadException
@dataclass(frozen=True, order=True)
class TInterval(Generic[_PositionT, _DataT]):
    begin: _PositionT
    end: _PositionT
    data: _DataT

    def overlaps(
        self,
        begin: _PositionT | TInterval[_PositionT, object],
        end: _PositionT | TInterval[_PositionT, object] | None = None,
    ) -> bool:
        """
        Whether the interval overlaps the given point, range or Interval.
        :param begin: beginning point of the range, or the point, or an Interval
        :param end: end point of the range. Optional if not testing ranges.
        :return: True or False
        :rtype: bool
        """
        if end is not None:
            # An overlap means that some C exists that is inside both ranges:
            #   begin <= C < end
            # and
            #   self.begin <= C < self.end
            # See https://stackoverflow.com/questions/3269434/whats-the-most-efficient-way-to-test-two-integer-ranges-for-overlap/3269471#3269471
            return begin < self.end and end > self.begin
        if isinstance(begin, TInterval):
            return self.overlaps(begin.begin, begin.end)
        else:
            return self.contains_point(begin)

    def overlap_size(
        self, begin: _PositionT | TInterval[_PositionT, object], end: _PositionT | None = None
    ) -> _PositionT:
        """
        Return the overlap size between two intervals or a point
        :param begin: beginning point of the range, or the point, or an Interval
        :param end: end point of the range. Optional if not testing ranges.
        :return: Return the overlap size, None if not overlap is found
        :rtype: depends on the given input (e.g., int will be returned for int interval and timedelta for
        datetime intervals)
        """
        overlaps = self.overlaps(begin, end)
        if not overlaps:
            return type(self.begin)()

        if end is not None:
            # case end is given
            i0 = max(self.begin, begin)
            i1 = min(self.end, end)
            return i1 - i0
        if isinstance(begin, TInterval):
            i0 = max(self.begin, begin.begin)
            i1 = min(self.end, begin.end)
            return i1 - i0
        raise ValueError("end must be given if begin is not an interval")

    def contains_point(self, p: _PositionT) -> bool:
        """
        Whether the Interval contains p.
        :param p: a point
        :return: True or False
        :rtype: bool
        """
        return self.begin <= p < self.end

    def range_matches(self, other: TInterval[_PositionT, object]) -> bool:
        """
        Whether the begins equal and the ends equal. Compare __eq__().
        :param other: Interval
        :return: True or False
        :rtype: bool
        """
        return self.begin == other.begin and self.end == other.end

    def contains_interval(self, other: TInterval[_PositionT, object]) -> bool:
        """
        Whether other is contained in this Interval.
        :param other: Interval
        :return: True or False
        :rtype: bool
        """
        return self.begin <= other.begin and self.end >= other.end

    def distance_to(self, other: TInterval[_PositionT, object] | _PositionT) -> _PositionT:
        """
        Returns the size of the gap between intervals, or 0
        if they touch or overlap.
        :param other: Interval or point
        :return: distance
        :rtype: Number
        """
        if self.overlaps(other):
            return type(self.begin)()
        if isinstance(other, TInterval):
            if self.begin < other.begin:
                return other.begin - self.end
            else:
                return self.begin - other.end
        else:
            if self.end <= other:
                return other - self.end
            else:
                return self.begin - other

    def is_null(self):
        """
        Whether this equals the null interval.
        :return: True if end <= begin else False
        :rtype: bool
        """
        return self.begin >= self.end

    def length(self):
        """
        The distance covered by this Interval.
        :return: length
        :type: Number
        """
        if self.is_null():
            return 0
        return self.end - self.begin

    def __hash__(self):
        """
        Depends on begin and end only.
        :return: hash
        :rtype: Number
        """
        return hash((self.begin, self.end))

    def __eq__(self, other):
        """
        Whether the begins equal, the ends equal, and the data fields
        equal. Compare range_matches().
        :param other: Interval
        :return: True or False
        :rtype: bool
        """
        return self.begin == other.begin and self.end == other.end and self.data == other.data

    def __cmp__(self, other: TInterval[_PositionT, object]) -> int:
        """
        Tells whether other sorts before, after or equal to this
        Interval.

        Sorting is by begins, then by ends, then by data fields.

        If data fields are not both sortable types, data fields are
        compared alphabetically by type name.
        :param other: Interval
        :return: -1, 0, 1
        :rtype: int
        """
        if self.begin < other.begin:
            return -1
        elif self.begin > other.begin:
            return 1
        elif self.end < other.end:
            return -1
        elif self.end > other.end:
            return 1
        elif self.data is None and other.data is None:
            return 0
        elif self.data is None:
            return -1
        elif other.data is None:
            return 1

        # If data allows comparison, compare it
        if isinstance(self.data, SupportsLtGt):
            if self.data < other.data:
                return -1
            elif self.data > other.data:
                return 1
        return 0

    def _raise_if_null(self, other: TInterval[_PositionT, object]) -> None:
        """
        :raises ValueError: if either self or other is a null Interval
        """
        if self.is_null():
            raise ValueError("Cannot compare null Intervals!")
        if hasattr(other, "is_null") and other.is_null():
            raise ValueError("Cannot compare null Intervals!")

    def _get_fields(self):
        """
        Used by str, unicode, repr and __reduce__.

        Returns only the fields necessary to reconstruct the Interval.
        :return: reconstruction info
        :rtype: tuple
        """
        if self.data is not None:
            return self.begin, self.end, self.data
        else:
            return self.begin, self.end

    def __repr__(self):
        """
        Executable string representation of this Interval.
        :return: string representation
        :rtype: str
        """
        if isinstance(self.begin, Number):
            s_begin = str(self.begin)
            s_end = str(self.end)
        else:
            s_begin = repr(self.begin)
            s_end = repr(self.end)

        cls_name = self.__class__.__name__
        if self.data is None:
            return f"{cls_name}({s_begin}, {s_end})"
        else:
            return f"{cls_name}({s_begin}, {s_end}, {self.data!r})"

    __str__ = __repr__

    def copy(self) -> TInterval[_PositionT, _DataT]:
        """
        Shallow copy.
        :return: copy of self
        :rtype: Interval
        """
        return TInterval(self.begin, self.end, self.data)


_IntervalT = TypeVar("_IntervalT", bound=TInterval)

if __name__ == "__main__":
    tree = IntervalTree()
    tree.add(TInterval(0, 10, "foo"))
    tree.add(TInterval(5, 15, "bar"))
    print(5 in tree)
    print(tree)
