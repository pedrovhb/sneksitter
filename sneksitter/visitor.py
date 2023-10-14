from __future__ import annotations

from abc import ABC
from functools import cache
from typing import (
    Callable,
    ParamSpec,
    ClassVar,
    Tuple,
    Type,
    Any,
    TypeVar,
)

from tree_sitter import Node, Tree, TreeCursor
from typing_extensions import Self

from sneksitter.metadata import MetadataProvider

NotRunSentinel = object()

_P = ParamSpec("_P")
_T = TypeVar("_T")
_R = TypeVar("_R")
_T_co = TypeVar("_T_co", covariant=True)
_T_contra = TypeVar("_T_contra", contravariant=True)


MetadataForNodeT = dict[Type[MetadataProvider[_T]], _T | None]
NodePredicateFnT = Callable[[Node, MetadataForNodeT], bool]
NodeVisitorFnT = Callable[["BaseVisitor", Node, MetadataForNodeT], _R | None]


class BaseVisitor(ABC):
    """Base class for a visitor that traverses a tree and calls methods on each node."""

    named_only = False
    _leave_predicates: list[tuple[tuple[NodePredicateFnT], NodeVisitorFnT]] = []
    _visit_predicates: list[tuple[tuple[NodePredicateFnT], NodeVisitorFnT]] = []

    _metadata_providers: dict[Type[MetadataProvider[_T]], MetadataProvider[_T]]
    _metadata: dict[Type[MetadataProvider[_T]], dict[int, _T]]

    # Metadata providers for the visitor, to be defined by derived classes
    METADATA_PROVIDERS: ClassVar[Tuple[Type[MetadataProvider[Any]], ...]] = ()

    def __init__(self, *args, **kwargs) -> None:
        self._metadata_providers = {}
        self._metadata = {}

    @cache
    def _metadata_for_node_id(self, node_id: int) -> MetadataForNodeT[_T]:
        return {cls: metadata.get(node_id) for cls, metadata in self._metadata.items()}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        for method in cls.__dict__.values():
            if ps := getattr(method, "_visit_predicates", None):
                cls._visit_predicates.extend((predicates, method) for predicates in ps)
            if ps := getattr(method, "_leave_predicates", None):
                cls._leave_predicates.extend((predicates, method) for predicates in ps)

    def _handle_leave_return_value(
        self,
        original_node: Node,
        return_value: Any,
    ) -> None:
        """Handle the return value of a leave method."""
        pass

    def _traverse(self, cursor: TreeCursor) -> None:
        """Traverse the tree and call the visitor's methods."""
        if self.named_only and not cursor.node.is_named:
            return

        metadata = self._metadata_for_node_id(cursor.node.id)
        should_traverse_children = self._visit(cursor.node, metadata)

        if should_traverse_children is not False:
            # Traverse the cursor.node's children
            if cursor.goto_first_child():
                self._traverse(cursor)
                while cursor.goto_next_sibling():
                    self._traverse(cursor)
                cursor.goto_parent()

        # Call the visitor's leave methods
        leave_result = self._leave(cursor.node, metadata)
        self._handle_leave_return_value(cursor.node, leave_result)

    def _visit(self, node: Node, metadata: dict[Type[MetadataProvider[_T]], _T]) -> Any:
        """Call the visitor's visit methods."""

        # Check if there are any sets of predicates that match the node
        # and call the corresponding method if so.
        for predicates, method in self._visit_predicates:
            if all(predicate(node, metadata) for predicate in predicates):
                return method(self, node, metadata)

        method_name = f"visit_{node.type.replace('-', '_')}"
        if specific_method := getattr(self, method_name, None):
            return specific_method(node, metadata)
        elif visit_method := getattr(self, "visit", None):
            return visit_method(node, metadata)
        return NotRunSentinel

    def _leave(
        self,
        node: Node,
        metadata: dict[Type[MetadataProvider[_T]], _T],
    ) -> Any:
        """Call the visitor's leave methods."""
        # Check if there are any sets of predicates that match the node
        # and call the corresponding method if so.
        for predicates, method in self._leave_predicates:
            if all(predicate(node, metadata) for predicate in predicates):
                return method(self, node, metadata)

        method_name = f"leave_{node.type.replace('-', '_')}"
        if specific_method := getattr(self, method_name, None):
            return specific_method(node, metadata)
        elif leave_method := getattr(self, "leave", None):
            return leave_method(node, metadata)
        return NotRunSentinel

    def resolve_metadata(self, tree: Tree) -> None:
        for provider_cls in self.METADATA_PROVIDERS:
            provider_instance = provider_cls()
            self._metadata_providers[provider_cls] = provider_instance
            self._metadata[provider_cls] = provider_instance.resolve(tree)

    @classmethod
    def traverse_tree(
        cls,
        tree: Tree,
        named_only: bool | None = None,
        *args,
        **kwargs,
    ) -> Self:
        """Class method to traverse the tree and call the visitor's methods."""
        cursor = tree.walk()
        visitor = cls(*args, **kwargs)
        if named_only is not None:
            visitor.named_only = named_only
        visitor.resolve_metadata(tree)
        visitor._traverse(cursor)
        return visitor
