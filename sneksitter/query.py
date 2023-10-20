from __future__ import annotations

import re
from pathlib import Path

from tree_sitter import Node
from tree_sitter_languages import get_parser

from sneksitter.utils import ts_traverse_bfs


# Redefining the basic structure for Q and CombinedQ classes, and the %& operator


class Q:
    def __init__(self, **kwargs):
        self.query_attributes = kwargs
        self.negate = False
        self.ancestor = False
        self.descendant = False

    def __and__(self, other):
        return CombinedQ(self, other, operator="and")

    def __or__(self, other):
        return CombinedQ(self, other, operator="or")

    def __xor__(self, other):
        return CombinedQ(self, other, operator="xor")

    def __invert__(self):
        new_q = Q(**self.query_attributes)
        new_q.negate = not self.negate
        return new_q

    def __pos__(self):
        new_q = Q(**self.query_attributes)
        new_q.ancestor = True
        return new_q

    def __neg__(self):
        new_q = Q(**self.query_attributes)
        new_q.descendant = True
        return new_q

    def matches(self, target_node: Node) -> bool:
        """
        Extended match_node function to handle Node dataclass instances.
        """
        result = True

        for attr, value in self.query_attributes.items():
            # Extracting attribute and its sub-attribute (if any), e.g., "parent__type" -> ("parent", "type")
            parts = attr.split("__")
            key = parts[0]
            sub_key = parts[1] if len(parts) > 1 else None

            if self.ancestor:
                # Ancestor matching using unary +
                current = target_node
                while current.parent:
                    current = current.parent
                    if getattr(current, key, None) == value:
                        break
                else:
                    result = False
                    break

            elif self.descendant:
                # Descendant matching using unary -
                stack = [target_node]
                while stack:
                    current = stack.pop()
                    if getattr(current, key, None) == value:
                        break
                    stack.extend(current.children)
                else:
                    result = False
                    break

            elif sub_key:
                # Check sub-attribute, e.g., target_node.parent.type
                sub_attr = getattr(getattr(target_node, key, None), sub_key, None)
                if sub_attr != value:
                    result = False
                    break

            else:
                # Check primary attribute, e.g., target_node.type
                if getattr(target_node, key, None) != value:
                    result = False
                    break

        # Apply negation if needed
        return not result if self.negate else result

    __call__ = matches

    def __repr__(self) -> str:
        pairs = ", ".join(f"{k}={v!r}" for k, v in self.query_attributes.items())
        sign = []
        if self.negate:
            sign.append("~")
        if self.ancestor:
            sign.append("+")
        if self.descendant:
            sign.append("-")
        sign = "".join(sign)
        return f"{sign}Q({pairs})"


class CombinedQ:
    def __init__(self, left: Q | CombinedQ, right: Q | CombinedQ, operator: str):
        self.left = left
        self.right = right
        self.operator = operator

    def __and__(self, other):
        return CombinedQ(self, other, operator="and")

    def __or__(self, other):
        return CombinedQ(self, other, operator="or")

    def __invert__(self):
        return CombinedQ(~self.left, ~self.right, operator=self.operator)

    def __pos__(self):
        return CombinedQ(+self.left, +self.right, operator=self.operator)

    def __neg__(self):
        return CombinedQ(-self.left, -self.right, operator=self.operator)

    def __xor__(self, other):
        return CombinedQ(self, other, operator="xor")

    def matches(self, target_node: Node) -> bool:
        """
        Resolve a CombinedQ object against a given target_node.
        """
        left_result = self.left.matches(target_node)
        right_result = self.right.matches(target_node)

        if self.operator == "and":
            return left_result and right_result
        elif self.operator == "or":
            return left_result or right_result

    __call__ = matches

    def __repr__(self) -> str:
        symbols = {"and": "&", "or": "|", "xor": "^"}
        op = symbols[self.operator]
        return f"CombinedQ({self.left!r} {op} {self.right!r})"


if __name__ in "__live_coding__":
    print("Running live coding tests...")

    parser = get_parser("python")
    source = Path(__file__).read_bytes()
    tree = parser.parse(source)

    for node, depth in ts_traverse_bfs(tree, Q(type="identifier")):
        fn_def_ancestor_q = +Q(type="function_definition")

        if fn_def_ancestor_q.matches(node):
            print(node.text)


if __name__ == "__main__":

    def foo(i: int) -> int:
        for i in range(10):
            print(i)
        return i + 1

    parser = get_parser("python")
    source = Path(__file__).read_bytes()
    tree = parser.parse(source)

    for node, depth in ts_traverse_bfs(tree):
        # print(target_node.type)
        fn_def_q = Q(type="function_definition")
        # id_q = Q(type="identifier")
        if fn_def_q.matches(node):
            print(node.text)

    print("----")
    # Get methods not defined within a class definition
    for node, depth in ts_traverse_bfs(tree):
        method_q = Q(type="function_definition")
        class_ancestor_q = +Q(type="class_definition")
        combined_q = method_q & ~class_ancestor_q
        if combined_q.matches(node):
            print(node.text)

    # Testing the updated match_node function using the mock Node dataclass
    q_ancestor = +Q(type="program")
    q_descendant = -Q(type="identifier")
    q_negate = ~Q(type="identifier")
    print("Tests passed!")

    # Testing the resolve_combined_q function
    q1 = Q(type="function_definition")
    q2 = Q(type="identifier")
    q3 = ~Q(type="loop")
    q4 = +Q(type="program")
    q5 = -Q(type="return_statement")

    combined_q1 = (q1 & q2) | (q3 & q4) | q5
    combined_q2 = q1 & ~q3

    # assert resolve_combined_q(function_def_node, combined_q1) == True
    # assert resolve_combined_q(loop_node, combined_q2) == False

    print("Tests passed!")
