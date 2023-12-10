from abc import abstractmethod
from collections import defaultdict
from difflib import SequenceMatcher
from pathlib import Path
from typing import Iterable, Sequence, overload, TypeVar

from sneksitter.fray.buf import CodeFile, tag_fn, SNode
import sneksitter.fray.buf

import tree_sitter_languages

_T_co = TypeVar("_T_co", covariant=True)

parser = tree_sitter_languages.get_parser("python")


class DiffableSNode(SNode, Sequence[SNode]):
    @overload
    @abstractmethod
    def __getitem__(self, index: int) -> _T_co:
        ...

    @overload
    @abstractmethod
    def __getitem__(self, index: slice) -> Sequence[_T_co]:
        ...

    def __getitem__(self, index):
        return self.children[index]

    def __len__(self):
        return len(self.children)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SNode):
            return False
        if self.type != other.type:
            return False
        if self.text != other.text:
            return False
        if len(self.children) != len(other.children):
            return False
        for i, (a_child, b_child) in enumerate(zip(self.children, other.children)):
            if not a_child == b_child:
                return False
            if not self.children_idx_to_field[i] == other.children_idx_to_field[i]:
                return False
        return True

    def __iter__(self) -> Iterable[SNode]:
        for child in self.children:
            yield child

    def __hash__(self) -> int:
        return hash(
            (
                self.type,
                self.text,
                self.is_named,
                self.location,
                tuple(self.children_idx_to_field),
                tuple(self.children),
            )
        )


sneksitter.fray.buf.SNode = SNode = DiffableSNode

code = Path("single_sample.py").read_bytes()
code_file = CodeFile(code, parser)
result = code_file.s_tree.render().decode()
print(result)
# from math import sqrt
#
#
# class Calculator:
#     def __init__(self, x: int) -> None:
#         self.x = x
#
#     def square_root(self) -> float:
#         return sqrt(self.x)
#
#     def cube(self) -> int:
#         return self.x**3
#
#
# if __name__ == "__main__":
#     calc = Calculator(144)
#     print(calc.square_root())


code_file_b = CodeFile(Path("single_sample_b.py").read_bytes(), parser)


def compare_snodes(a: SNode, b: SNode):
    if a.type != b.type:
        return False
    if a.text != b.text:
        return False
    if len(a.children) != len(b.children):
        return False
    for a_child, b_child in zip(a.children, b.children):
        if not compare_snodes(a_child, b_child):
            return False
    return True


def copy_snode(node: SNode) -> SNode:
    return SNode(
        type=node.type,
        text=node.text,
        is_named=node.is_named,
        location=node.location,
        children_idx_to_field=node.children_idx_to_field,
        children=[copy_snode(child) for child in node.children],
    )


tree_a = code_file.s_tree
tree_b = code_file_b.s_tree

print(compare_snodes(tree_a, tree_b))
print(tree_a == tree_b)

# Edit the tree
# foo_fn = tree_a.children[0].children[-1]
# print(foo_fn, foo_fn.text)  # sqrt
# foo_fn.text = b"cube"
# #
# fn = tree_a.children[1].children[3].children[1]
# print(fn, fn.text)  # function_definition
# fn.text = b"def minus_one(self): return self.x - 1"

print(compare_snodes(tree_a, tree_b))
print(tree_a == tree_b)


def find_diffs(a: SNode, b: SNode) -> dict[SNode, list[tuple[str, SNode | None]]]:
    matcher = SequenceMatcher(a=a, b=b)
    diffs = defaultdict(list)
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        # print(f"{tag=} {i1=} {i2=} {j1=} {j2=}")
        if tag == "insert":
            print("insert", tree_b.children[j1:j2])
        elif tag == "delete":
            print("delete", tree_a.children[i1:i2])

        elif tag == "replace":
            #             print("replace", tree_a.children[i1:i2], tree_b.children[j1:j2])
            # and recurse
            diffs[a].append(("replace", b))
            sub_diffs = find_diffs(a.children[i1], b.children[j1])
            for node, ds in sub_diffs.items():
                diffs[node].extend(ds)

        elif tag == "equal":
            for aa, bb in zip(a.children[i1:i2], b.children[j1:j2]):
                sub_diffs = find_diffs(aa, bb)
                for node, ds in sub_diffs.items():
                    diffs[node].extend(ds)
        #             print("equal", tree_a.children[i1:i2], tree_b.children[j1:j2])
        else:
            raise ValueError(f"Unknown tag: {tag}")
    return diffs


print("-------")
diffs = find_diffs(tree_a, tree_b)
for node, ds in diffs.items():
    for tag, obj in ds:
        if tag == "equal":
            continue
        # print(tag, obj)

        print(node, tag, obj, f"{node.text} -> {obj.text}")

# print(tree_a.render().decode())
# print("-------")
# print(tree_b.render().decode())
