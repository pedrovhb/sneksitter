from tree_sitter import Node

from sneksitter.metadata.base_visitor_provider import VisitorBasedMetadataProvider
from intervaltree import IntervalTree, Interval


class IntervalTreeMetadataProvider(VisitorBasedMetadataProvider[Interval]):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._interval_tree = IntervalTree()
        self._node_id_to_node: dict[int, Node] = {}

    def visit(self, node: Node) -> None:
        self._node_id_to_node[node.id] = node
        interval = Interval(
            begin=node.start_byte,
            end=node.end_byte,
            data=node.id,
        )
        self._interval_tree.add(interval)
        self.set_metadata_for_node(node, interval)

    def nodes_containing_byte(self, byte_idx: int) -> tuple[Node]:
        """Returns the set of all nodes containing the byte at `byte_idx`."""
        return tuple(
            self._node_id_to_node[interval.data]
            for interval in self._interval_tree.at(byte_idx)
        )

    def nodes_overlapping_range(
        self,
        start_byte: int,
        end_byte: int,
    ) -> tuple[Node]:
        """Returns the set of all nodes overlapping the range [start_byte, end_byte)."""
        return tuple(
            self._node_id_to_node[interval.data]
            for interval in self._interval_tree.overlap(start_byte, end_byte)
        )

    def nodes_containing_range(
        self,
        start_byte: int,
        end_byte: int,
    ) -> tuple[Node]:
        """Returns the set of all nodes fully contained in the range [start_byte, end_byte)."""
        return tuple(
            self._node_id_to_node[interval.data]
            for interval in self._interval_tree.envelop(start_byte, end_byte)
        )


if __name__ == "__main__":
    from tree_sitter_languages import get_parser

    parser = get_parser("python")
    tree = parser.parse(b"def foo(a: int=4):\n    pass\n\nfoo()")

    provider = IntervalTreeMetadataProvider()
    provider.resolve(tree)

    print(
        {
            node_id: interval_data
            for node_id, interval_data in provider.metadata.items()
            if interval_data
        }
    )

    # Show all nodes containing byte 5 (the second 'o' in 'foo')
    for node in provider.nodes_containing_byte(6):
        print(node)
    # Result:
    # <Node type=identifier, start_point=(0, 4), end_point=(0, 7)>
    # <Node type=function_definition, start_point=(0, 0), end_point=(1, 8)>
    # <Node type=module, start_point=(0, 0), end_point=(3, 5)>
