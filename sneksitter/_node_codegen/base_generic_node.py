from __future__ import annotations

import inspect
from functools import cached_property
from itertools import chain

from tree_sitter import Node as TS_Node
from typing import Generic, TypeVar, TypeAlias, Union, Callable, ClassVar, Type, Tuple, Dict

_T = TypeVar("_T")
_LanguageNodeT = TypeVar("_LanguageNodeT", bound="BaseGenericNode")
_LanguageNodeTypeT = TypeVar("_LanguageNodeTypeT", bound="Type[BaseGenericNode]")
CodeT: TypeAlias = Union[str, bytes, TS_Node, "BaseGenericNode"]
NodePredicateFnT = Callable[[TS_Node, "BaseVisitor"], bool] | Callable[[TS_Node], bool]
NodeVisitorFnT = Callable[["BaseVisitor", TS_Node], _T | None]


class BaseGenericNode(Generic[_LanguageNodeT]):
    language: ClassVar[str] = "python"
    original_node: TS_Node

    def __init__(self, original_node: TS_Node) -> None:
        self.original_node = original_node

    def _process_children(self, children: tuple[TS_Node, ...]) -> tuple[TS_Node, ...]:
        for i, child in enumerate(children):
            self.original_node.field_name_for_child(i)

    @classmethod
    def _own_fields(cls) -> tuple[str, ...]:
        base_members = inspect.getmembers(BaseGenericNode, lambda m: not inspect.isroutine(m))
        sub_members = inspect.getmembers(cls, lambda m: not inspect.isroutine(m))

        base_members = {name for name, value in base_members if not name.startswith("__")}
        sub_members = {name for name, value in sub_members if not name.startswith("__")}

        subclass_own_members = sub_members - base_members - {"NODE_MAPPING", "_key"}
        return tuple(subclass_own_members)

    @classmethod
    def from_node(cls, node: TS_Node) -> _LanguageNodeT:
        node_cls = cls.NODE_MAPPING.get((node.type, node.is_named))
        if node_cls is None:
            raise ValueError(f"No node class found for type {node.type} and named {node.is_named}")

        field_values = {}
        for field_name in inspect.get_annotations(node_cls).keys():
            if field_name == "_key":
                continue
            if field_name == "named_children":
                field_values[field_name] = tuple(cls.from_node(child) for child in node.children)
            else:
                ts_node = node.child_by_field_name(field_name)
                if ts_node is not None:
                    field_values[field_name] = cls.from_node(ts_node)

        return node_cls(**field_values, original_node=node)

    def code(self) -> str:
        return self.original_node.text.decode()

    # @property
    # def named_children(self) -> Tuple[_LanguageNodeT, ...]:
    #     return tuple(child for child in self.all_children if child.original_node.is_named)

    def __repr__(self) -> str:
        start_point_str = ", ".join(str(i) for i in self.original_node.start_point)
        end_point_str = ", ".join(str(i) for i in self.original_node.end_point)
        return f"<{self.__class__.__name__} [{start_point_str}] - [{end_point_str}]>"

    __str__ = __repr__

    NODE_MAPPING: ClassVar[Dict[Tuple[str, bool], Type[BaseGenericNode]]]
