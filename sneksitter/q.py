from __future__ import annotations

from __future__ import annotations
from copy import deepcopy
import re
from typing import List, Callable, Union, Iterator, TypeVar, Pattern

T = TypeVar("T", bound="Q")


class Node:
    def __init__(self, type: str, text: str, parent: Node | None = None):
        self.type: str = type
        self.parent: Node | None = parent
        self.text: str = text
        self.children: List[Node] = []
        if parent:
            parent.children.append(self)

    @classmethod
    def from_dict(cls, data: dict, parent: Node | None = None) -> Node:
        node = cls(data["type"], data["text"], parent)
        for child in data.get("children", []):
            cls.from_dict(child, node)
        return node

    def walk(self) -> Iterator[Node]:
        yield self
        for child in self.children:
            yield from child.walk()

    def __str__(self) -> str:
        return f"Node(type='{self.type}', text='{self.text}')"


class Q:
    def __init__(self, *args: Callable[[Node], bool], **kwargs):
        self.custom_funcs = args
        self.query_attributes = kwargs
        self.negate = False
        self.ancestor = 0
        self.descendant = 0
        self.has_prev_sibling = None
        self.has_next_sibling = None
        self.has_any_prev_sibling = None
        self.has_any_next_sibling = None

    def _simple_match(self, target_node: Node, key: str, value: Union[str, Pattern]) -> bool:
        attr_value = getattr(target_node, key, None)
        if isinstance(value, Pattern):
            return bool(value.match(attr_value))
        else:
            return attr_value == value

    def matches(self, target_node: Node) -> bool:
        base_match = all(func(target_node) for func in self.custom_funcs) and all(
            self._simple_match(target_node, key, value)
            for key, value in self.query_attributes.items()
        )

        if self.negate:
            base_match = not base_match

        return base_match

    def __and__(self, other: Q) -> Q:
        return self._combine(other, "and")

    def __or__(self, other: Q) -> Q:
        return self._combine(other, "or")

    def __invert__(self) -> Q:
        new_q = deepcopy(self)
        new_q.negate = not new_q.negate
        return new_q

    def __pos__(self) -> Q:
        new_q = deepcopy(self)
        new_q.ancestor += 1
        return new_q

    def __neg__(self) -> Q:
        new_q = deepcopy(self)
        new_q.descendant += 1
        return new_q

    def __lshift__(self, other: Q) -> Q:
        new_q = deepcopy(self)
        new_q.has_any_prev_sibling = other
        return new_q

    def __rshift__(self, other: Q) -> Q:
        new_q = deepcopy(self)
        new_q.has_any_next_sibling = other
        return new_q

    def __gt__(self, other: Q) -> Q:
        new_q = deepcopy(self)
        new_q.has_prev_sibling = other
        return new_q

    def __lt__(self, other: Q) -> Q:
        new_q = deepcopy(self)
        new_q.has_next_sibling = other
        return new_q

    def __str__(self) -> str:
        return f"Q({self.custom_funcs}, {self.query_attributes})"

    def __repr__(self) -> str:
        return self.__str__()

    __call__ = matches

    def _match_sibling_constraints(self, target_node: Node) -> bool:
        parent = target_node.parent
        if parent:
            siblings = parent.children
            index = siblings.index(target_node)
            return all(
                [
                    self._match_immediate_prev_sibling(index, siblings),
                    self._match_immediate_next_sibling(index, siblings),
                    self._match_any_prev_sibling(index, siblings),
                    self._match_any_next_sibling(index, siblings),
                ]
            )
        return True

    def _match_immediate_prev_sibling(self, index: int, siblings: List[Node]) -> bool:
        if self.has_prev_sibling and index > 0:
            prev_sibling = siblings[index - 1]
            return self.has_prev_sibling.matches(prev_sibling)
        return True

    def _match_immediate_next_sibling(self, index: int, siblings: List[Node]) -> bool:
        if self.has_next_sibling and index < len(siblings) - 1:
            next_sibling = siblings[index + 1]
            return self.has_next_sibling.matches(next_sibling)
        return True

    def _match_any_prev_sibling(self, index: int, siblings: List[Node]) -> bool:
        if self.has_any_prev_sibling:
            for prev_sibling in siblings[:index]:
                if self.has_any_prev_sibling.matches(prev_sibling):
                    return True
            return False
        return True

    def _match_any_next_sibling(self, index: int, siblings: List[Node]) -> bool:
        if self.has_any_next_sibling:
            for next_sibling in siblings[index + 1 :]:
                if self.has_any_next_sibling.matches(next_sibling):
                    return True
            return False
        return True

    def matches(self, target_node: Node) -> bool:
        if not all(func(target_node) for func in self.custom_funcs):
            return False

        if not all(
            self._simple_match(target_node, key, value)
            for key, value in self.query_attributes.items()
        ):
            return False

        if not self._match_sibling_constraints(target_node):
            return False

        return True

    def _combine(self, other: T, op: str) -> T:
        new_q = deepcopy(self)

        if op == "and":
            new_q.custom_funcs += other.custom_funcs
            new_q.query_attributes.update(other.query_attributes)
            new_custom_func = lambda node: self.matches(node) and other.matches(node)
            new_q.custom_funcs += (new_custom_func,)

        elif op == "or":
            new_custom_func = lambda node: self.matches(node) or other.matches(node)
            new_q.custom_funcs += (new_custom_func,)

        elif op == "xor":
            new_custom_func = lambda node: bool(self.matches(node)) ^ bool(other.matches(node))
            new_q.custom_funcs += (new_custom_func,)

        return new_q

    def __xor__(self, other: T) -> T:
        return self._combine(other, "xor")


def find_matching_nodes(root: Node, query: Q, first=False, last=False, nth=None) -> List[Node]:
    matches = [node for node in root.walk() if query.matches(node)]
    if first:
        return matches[:1]
    if last:
        return matches[-1:]
    if nth is not None:
        return matches[nth : nth + 1]
    return matches


if __name__ == "__main__":
    sample_data = {
        "type": "root",
        "text": "root",
        "children": [
            {"type": "import_statement", "text": "import os", "children": []},
            {
                "type": "import_from_statement",
                "text": "from sys import path",
                "children": [],
            },
            {
                "type": "function_definition",
                "text": "def func():",
                "children": [
                    {"type": "import_statement", "text": "import re", "children": []},
                    {"type": "expression", "text": "print('Hello')", "children": []},
                ],
            },
        ],
    }

    # Create the root root_node using the sample data
    root_node = Node.from_dict(sample_data)

    # Display the root root_node and its descendants
    print("Root Node:")
    print(root_node)
    for n in root_node.walk():
        print(n)

    # Testing any sibling constraints
    any_prev_sibling_q = Q(type="import_statement") << Q(type="import_from_statement")
    any_next_sibling_q = Q(type="import_statement") >> Q(type="import_from_statement")
    immediate_prev_sibling_q = Q(type="import_statement") > Q(type="import_from_statement")
    immediate_next_sibling_q = Q(type="import_statement") < Q(type="import_from_statement")

    print("Nodes matching any previous sibling Q object:")
    print(find_matching_nodes(root_node, any_prev_sibling_q))

    print("Nodes matching any next sibling Q object:")
    print(find_matching_nodes(root_node, any_next_sibling_q))

    print("Nodes matching immediate previous sibling Q object:")
    print(find_matching_nodes(root_node, immediate_prev_sibling_q))

    print("Nodes matching immediate next sibling Q object:")
    print(find_matching_nodes(root_node, immediate_next_sibling_q))

    # Test &
    print("Nodes matching Q object with & operator:")
    Q(type="import_statement") & +Q(type="import_from_statement")
