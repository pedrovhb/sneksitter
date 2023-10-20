from abc import ABC
from typing import TypeVar, Generic

from tree_sitter import Tree, Node

_T = TypeVar("_T")


class MetadataProvider(ABC, Generic[_T]):
    metadata: dict[int, _T] = {}

    def resolve(self, tree: Tree) -> dict[int, _T]:
        """
        Compute and store provider for nodes in `self.provider` dictionary.
        """
        raise NotImplementedError

    def metadata_for_node(self, node_id: int) -> _T:
        return self.metadata.get(node_id)

    def set_metadata_for_node(self, node: Node, metadata: _T) -> None:
        node_id = node.id
        if node_id in self.metadata and self.metadata.get(node_id) != metadata:
            raise ValueError(f"Metadata for node {node_id} already set")
        self.metadata[node_id] = metadata
