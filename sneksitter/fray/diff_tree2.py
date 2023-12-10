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
