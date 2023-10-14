from abc import ABC
from typing import TypeVar, Generic

from tree_sitter import Tree

_T = TypeVar("_T")


class MetadataProvider(ABC, Generic[_T]):
    def __init__(self) -> None:
        self.metadata: dict[int, _T] = {}

    def resolve(self, tree: Tree) -> dict[int, _T]:
        """
        Compute and store metadata for nodes in `self.metadata` dictionary.
        """
        raise NotImplementedError
