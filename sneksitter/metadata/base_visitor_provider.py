from __future__ import annotations

from abc import ABC
from typing import TypeVar

from tree_sitter import Tree

from sneksitter.metadata import MetadataProvider
from sneksitter.visitor import BaseVisitor

_T = TypeVar("_T")


class VisitorBasedMetadataProvider(MetadataProvider[_T], BaseVisitor, ABC):
    """A provider provider that uses a visitor to resolve provider.

    Classes should inherit from this class and implement the `visit` and `leave` methods
    as in a normal visitor. The `visit` and `leave` methods should call `self.set_metadata_for_node`
    to set the provider for any given root_node.
    """

    def resolve(self, tree: Tree) -> dict[int, _T]:
        self.traverse(tree)
        return self.metadata

    def metadata_for_node(self, node_id: int) -> _T:
        return self.metadata.get(node_id)
