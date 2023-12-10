from __future__ import annotations

import textwrap
from typing import Iterable, NamedTuple, Callable, Sequence

import tree_sitter_languages
from intervaltree import IntervalTree, Interval
from tree_sitter import Node, Parser

i_tree = IntervalTree()

sample_code = b"""\
def add(one, other):
    return one + other
"""

i_tree[0 : len(sample_code)] = sample_code

parser = tree_sitter_languages.get_parser("python")
ts_tree = parser.parse(sample_code)


def iter_leaf_nodes(node: Node) -> Iterable[Node]:
    if not node.children:
        yield node
    for child in node.children:
        yield from iter_leaf_nodes(child)


# Get the function name node
function_name_node = ts_tree.root_node.children[0].child_by_field_name("name")
print(function_name_node)
print(function_name_node.start_byte, function_name_node.end_byte)

i2 = IntervalTree()
for node in iter_leaf_nodes(ts_tree.root_node):
    print(node.text.decode(), end=" ")
    i2[node.start_point : node.end_point] = node.text


def node_interval_repr(interval: Interval | set[Interval]) -> list[str]:
    reprs = []
    if isinstance(interval, Interval):
        interval = {interval}
    for interval in sorted(interval, key=lambda x: x.begin):
        node_text = interval.data
        text_snippet = textwrap.shorten(node_text.decode(), width=20, placeholder="...")
        start_point, end_point = interval.begin, interval.end
        start_point_repr = f"[{start_point[0]}, {start_point[1]}]"
        end_point_repr = f"[{end_point[0]}, {end_point[1]}]"
        range_repr = f"{start_point_repr} - {end_point_repr}"
        reprs.append(f"<NodeInterval {range_repr} {text_snippet!r}>")

    return reprs


print(node_interval_repr(i2[(0, 4):(0, 7)]))  # {Interval((0, 4), (0, 7), b'add')}
print()  # {Interval((0, 11), (0, 12), b','), Interval((0, 7), (0, 8), b'('), Interval((0, 13), (0, 18), b'other'), Interval((0, 18), (0, 19), b')'), Interval((0, 8), (0, 11), b'one')}

for i in node_interval_repr(i2[(0, 7):(0, 19)]):
    print(i)
    # <NodeInterval [0, 7] - [0, 8] '('>
    # <NodeInterval [0, 8] - [0, 11] 'one'>
    # <NodeInterval [0, 11] - [0, 12] ','>
    # <NodeInterval [0, 13] - [0, 18] 'other'>
    # <NodeInterval [0, 18] - [0, 19] ')'>


# Replace "one" with "a"
i2.remove_envelop((0, 8), (0, 11))
i2[(0, 8):(0, 9)] = b"a"


for i in node_interval_repr(i2[(0, 7):(0, 19)]):
    print(i)
    # <NodeInterval [0, 7] - [0, 8] '('>
    # <NodeInterval [0, 11] - [0, 12] ','>
    # <NodeInterval [0, 13] - [0, 18] 'other'>
    # <NodeInterval [0, 18] - [0, 19] ')'>


class CompositeTree:
    def __init__(self, code: bytes, parser: Parser) -> None:
        self.code = code
        self.parser = parser
        self.ts_tree = parser.parse(code)
        self.intervals = IntervalTree()
        self.intervals[0 : len(code)] = code

        # but applying transformations doesn't really happen in-place though, does it?
        # it's a new tree, built from pieces of the original tree, plus changes.

        ######################
        # Sample code
        # a = b + c
        #   a
        #   b + c
        #     b
        #     c

        ######################
        # Replacing `c` with `d`:
        # a = b + d
        #   a
        #   b + d
        #     b
        #     d
        #
        # The minimal change is to swap out the `c` node for the `d` node.

        ######################
        # Replacing `+` with `-`:
        # a = b - c
        #   a
        #   b - c
        #     b
        #     c
        #
        # The minimal change is to swap out the full `b + c`
        # node for the `b - c` node, as the +/- are an anonymous, unnamed node.
        # However, the b and c nodes are the same, so we'd have to track
        # children to keep their identities unchanged.
        #
        # So maybe
        #   for node in compared node's children:
        #     check children. if they're the same, keep them.
        #


from difflib import SequenceMatcher

# Demonstration using lists of integers
list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 4, 5, 6]
matcher_list = SequenceMatcher(None, list1, list2)
ratio_list = matcher_list.ratio()

# Demonstration using tuples
tuple1 = (1, "apple", 3, "banana")
tuple2 = (1, "apple", 4, "orange")
matcher_tuple = SequenceMatcher(None, tuple1, tuple2)
ratio_tuple = matcher_tuple.ratio()

# Demonstration using nodes
node_a = ts_tree.root_node
sample_code_b = b"""\
def add(some, other):
    return some + other
"""

ts_tree_b = parser.parse(sample_code_b)
node_b = ts_tree_b.root_node

node_a = node_a.children[0]
node_b = node_b.children[0]

for a, b in zip(node_a.children, node_b.children):
    print(a.text == b.text, a.text, b.text)
    print(a == b)

import wrapt


class NodeWrapper(wrapt.ObjectProxy):
    def __eq__(self, other: NodeWrapper | Node | bytes | object) -> bool:
        compare = other
        if isinstance(other, NodeWrapper):
            compare = other.__wrapped__.text
        elif isinstance(other, Node):
            compare = other.text
        elif isinstance(other, bytes):
            compare = other

        return self.__wrapped__.text == compare

    @property
    def children(self) -> list[NodeWrapper]:
        return [NodeWrapper(child) for child in self.__wrapped__.children]

    def __hash__(self) -> int:
        return hash(self.__wrapped__)


print(hash(node_a))
node_a = NodeWrapper(node_a)
node_b = NodeWrapper(node_b)
matcher_node = SequenceMatcher(None, node_a.children, node_b.children)
ratio_node = matcher_node.ratio()

matching_blocks = matcher_node.get_matching_blocks()
opcodes = matcher_node.get_opcodes()

from anytree import Node as AnyNode, NodeMixin as AnyNodeMixin, Resolver


class IntervalNode(AnyNodeMixin, Sequence["IntervalNode"]):
    def __len__(self) -> int:
        return len(self.children)

    def __getitem__(self, idx: int) -> MyNode:
        return self.children[idx]

    def __init__(
        self,
        start_point: tuple[int, int],
        end_point: tuple[int, int],
        start_byte: int,
        end_byte: int,
        text: bytes,
        type: str,
        field_name: str | None = None,
        children_field_indexes: dict[str, int] | None = None,
        children: list[MyNode] | None = None,
        parent: MyNode | None = None,
    ) -> None:
        self.start_point = start_point
        self.end_point = end_point
        self.start_byte = start_byte
        self.end_byte = end_byte
        self.text = text
        self.type = type
        self.field_name = field_name
        self.children_field_indexes = children_field_indexes

        self.children = children
        self.parent = parent

    @classmethod
    def from_ts_node(cls, node: Node, __field_name: str | None = None) -> MyNode:
        children_field_indexes = {}
        field_names = []
        for i, child in enumerate(node.children):
            field_name = node.field_name_for_child(i)
            if field_name is not None:
                children_field_indexes[field_name] = i
            field_names.append(field_name)

        return cls(
            start_point=node.start_point,
            end_point=node.end_point,
            start_byte=node.start_byte,
            end_byte=node.end_byte,
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
        range_str = f"[{self.start_point[0]}, {self.start_point[1]}] - [{self.end_point[0]}, {self.end_point[1]}]"
        snippet = textwrap.shorten(self.text.decode(), width=20, placeholder="...")
        return f"<IntervalNode {self.type} {range_str} {snippet=}>"

    __str__ = __repr__

    def __iter__(self) -> Iterable[MyNode]:
        for child in self.children:
            yield from child
        yield self

    def __eq__(self, other: MyNode | object) -> bool:
        if not isinstance(other, MyNode):
            return NotImplemented
        if self.children:
            return self.type == other.type and self.children == other.children
        return self.type == other.type and self.text == other.text

    def __hash__(self) -> int:
        if self.children:
            return hash((self.type, tuple(self.children)))
        return hash((self.type, self.text))

    def get_leaf_nodes(self) -> Iterable[IntervalNode]:
        if not self.children:
            yield self
        for child in self.children:
            yield from child.iter_leaf_nodes()


def transform_wrapped_tree(a, b, opcodes):
    for tag, i1, i2, j1, j2 in opcodes:
        print(tag, i1, i2, j1, j2)


transform_wrapped_tree(node_a, node_b, opcodes)

my_node = MyNode.from_ts_node(node_a)
my_node_b = MyNode.from_ts_node(node_b)
print(my_node)


for child in my_node:
    print(child)

for a, b in zip(my_node, my_node_b):
    print(a == b, a, b)


matcher_my_node = SequenceMatcher(
    None, list(my_node.iter_leaf_nodes()), list(my_node_b.iter_leaf_nodes())
)
ratio_my_node = matcher_my_node.ratio()

matching_blocks = matcher_my_node.get_matching_blocks()

opcodes = matcher_my_node.get_opcodes()

merged_tree = MyNode.from_ts_node(node_a)

for tag, i1, i2, j1, j2 in opcodes:
    print(tag, i1, i2, j1, j2)

    if tag == "equal":
        continue
    elif tag == "delete":
        for child in node_a[i1:i2]:
            print("delete", child)
            child.parent = None
    # elif tag == "insert":
    #     for child in my_node_b[j1:j2]:
    #         print("insert", child)
    #         child.parent = merged_tree
    # elif tag == "replace":
    #     for child in my_node[i1:i2]:
    #         print("replace", child)
    #         child.parent = None
    # for child in my_node_b[j1:j2]:
    #     print("replace", child)
    #     child.parent = merged_tree


class NodeEditScriptAnnotation(NamedTuple):
    a: MyNode
    b: MyNode


def get_matching_blocks(a: Sequence[MyNode], b: Sequence[MyNode]) -> list[tuple[int, int, int]]:
    matcher = SequenceMatcher(None, a, b)
    matching_blocks = matcher.get_matching_blocks()
    return [(i, j, n) for i, j, n in matching_blocks if n]


print(get_matching_blocks(my_node, my_node_b))
