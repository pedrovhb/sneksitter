from collections.abc import Mapping
from typing import TypeVar, Iterator, final

from tree_sitter import Node
from typing_extensions import Self

from sneksitter.visitor import TSVisitor

MetadataT = TypeVar("MetadataT", covariant=True)


class MetadataProvider(Mapping[Node, MetadataT]):
    def __init__(self) -> None:
        self._metadata: dict[Node, MetadataT] = {}

    def _set_metadata(self, node: Node, metadata: MetadataT) -> None:
        self._metadata[node] = metadata

    def _finalize_metadata(self) -> None:
        """Finalize the metadata for this provider.

        This is provided as a hook for subclasses to finalize the metadata after all nodes have
        been visited. It is called as the last thing .resolve() does.
        """
        pass

    def _resolve(self) -> None:
        """Compute and store provider for nodes in `self.provider` dictionary."""
        raise NotImplementedError

    def get_metadata(self, node: Node) -> MetadataT:
        return self._metadata[node]

    @final
    def resolve(self) -> Self:
        self._resolve()
        self._finalize_metadata()
        return self

    def __getitem__(self, __key: Node) -> MetadataT:
        return self._metadata[__key]

    def __len__(self) -> int:
        return len(self._metadata)

    def __iter__(self) -> Iterator[Node]:
        return iter(self._metadata)

    def __contains__(self, __key: Node) -> bool:
        return __key in self._metadata

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._metadata})"

    def __str__(self) -> str:
        return repr(self)


class VisitorBasedMetadataProvider(TSVisitor, MetadataProvider[MetadataT]):
    def __init__(self, root_node: Node) -> None:
        super().__init__(root_node)
        self._metadata: dict[Node, MetadataT] = {}

    def _resolve(self) -> Self:
        self.traverse()
        return self
