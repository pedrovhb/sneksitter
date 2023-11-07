from __future__ import annotations

import operator
from dataclasses import dataclass, field
from typing import Generic, Callable, TypeVar, Iterator

_T_co = TypeVar("_T_co", covariant=True)
_PredT = Callable[[_T_co], bool]


class _LookupChain(Generic[_T_co], Callable[[_T_co], bool]):
    """A lookup chain for a root_node root_node."""

    __slots__ = ("attribute_path", "predicate")

    attribute_path: tuple[str, ...]
    predicate: _PredT[_T_co]

    def __init__(
        self,
        attribute_or_path: tuple[str, ...] | str,
        predicate: _PredT[_T_co],
    ) -> None:
        # Split attribute or path
        if isinstance(attribute_or_path, str):
            attribute_path = attribute_or_path.split("__")
        else:
            attribute_path = attribute_or_path

        self.predicate = predicate
        self.attribute_path = attribute_path

    def __call__(self, obj: _T_co) -> bool:
        """Call the lookup chain on an object."""
        for attribute in self.attribute_path:
            obj = getattr(obj, attribute)
        return self.predicate(obj)


class Q(Generic[_T_co]):
    def __init__(
        self,
        *callable_predicates: _PredT[_T_co],
        **attribute_lookup_predicates: _PredT[_T_co] | object,
    ) -> None:
        self._callable_predicates = list(callable_predicates)
        for key, value in attribute_lookup_predicates.items():
            lookup_path = key.split("__")

            def _attr_lookup_predicate(obj: _T_co) -> bool:
                for attribute in lookup_path[:-1]:
                    obj = getattr(obj, attribute)
                last_part = lookup_path[-1]
                operators = {
                    "gt": operator.gt,
                    "lt": operator.lt,
                    "ge": operator.ge,
                    "gte": operator.ge,
                    "le": operator.le,
                    "lte": operator.le,
                    "eq": operator.eq,
                    "ne": operator.ne,
                    "contains": operator.contains,
                    "startswith": str.startswith,
                    "endswith": str.endswith,
                    "in": lambda x, y: x in y,
                    "not_in": lambda x, y: x not in y,
                    "is": operator.is_,
                    "is_not": operator.is_not,
                    "isinstance": isinstance,
                    "is_not_instance": lambda x, y: not isinstance(x, y),
                    "call": lambda x, y: y(x),
                    "check_pred": lambda x, y: y(x),
                }
                if last_part in operators:
                    return operators[last_part](obj, value)
                else:
                    obj = getattr(obj, last_part)

                if callable(value):
                    return value(obj)
                return obj == value

            _attr_lookup_predicate.__name__ = f"_lookup_{key}"

            self._callable_predicates.append(_attr_lookup_predicate)

    def __call__(self, obj: _T_co) -> bool:
        """Call the Q object on an object."""
        return all(func(obj) for func in self._callable_predicates)

    def __and__(self, other: _PredT[_T_co]) -> Q[_T_co]:
        return Q(self, other)

    def __or__(self, other: _PredT[_T_co]) -> Q[_T_co]:
        def _or(obj: _T_co) -> bool:
            return self(obj) or other(obj)

        return Q(_or)

    def __xor__(self, other: _PredT[_T_co]) -> Q[_T_co]:
        def _xor(obj: _T_co) -> bool:
            return self(obj) ^ other(obj)

        return Q(_xor)

    def __invert__(self) -> Q[_T_co]:
        def _invert(obj: _T_co) -> bool:
            return not self(obj)

        return Q(_invert)

    def find(self, *objects: _T_co) -> Iterator[_T_co]:
        for obj in objects:
            if self(obj):
                yield obj


if __name__ == "__main__":
    q10 = Q(lambda x: x > 5, lambda x: x % 5 == 0)
    assert (q10(10), q10(11)) == (True, False)

    @dataclass
    class Person:
        name: str
        age: int
        job: str
        friends: list[Person] = field(default_factory=list)

        def __str__(self) -> str:
            friends = ", ".join(repr(f.name) for f in self.friends)
            return f"<Person {self.name=}, {self.age=}, {self.job=}, {friends=}]>"

        __repr__ = __str__

    people = [
        a := Person("Alice", 20, "Developer"),
        b := Person("Bob", 30, "Developer"),
        c := Person("Charlie", 40, "Manager"),
        d := Person("Dave", 23, "Manager"),
        e := Person("Eve", 60, "CEO"),
    ]
    a.friends.extend([b, c, d, e])
    b.friends.extend([a, c])
    c.friends.extend([a, b, d])
    d.friends.extend([a, c])
    e.friends.extend([a])

    group_0 = Q(age__gt=25) & Q(job="Developer")
    print(list(group_0.find(*people)))
    assert list(group_0.find(*people)) == [b]

    group_1 = (Q(age__gt=25) & Q(job="Developer")) | Q(job="Manager")
    print(list(group_1.find(*people)))
    assert list(group_1.find(*people)) == [b, c, d]
