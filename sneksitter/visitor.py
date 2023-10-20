from __future__ import annotations

import inspect
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
    TypedDict,
    Mapping,
    MutableMapping,
)

from tree_sitter import Node, Tree, TreeCursor
from typing_extensions import Self

from sneksitter.metadata import MetadataProvider
from sneksitter.utils import CodeT

_P = ParamSpec("_P")
_T = TypeVar("_T")
_R = TypeVar("_R")
_T_co = TypeVar("_T_co", covariant=True)
_T_contra = TypeVar("_T_contra", contravariant=True)


_MetadataProviderDictT = MutableMapping[
    Type[MetadataProvider[_T]],
    MetadataProvider[_T],
]
_MetadataDictT = MutableMapping[
    Type[MetadataProvider[_T]],
    MutableMapping[int, _T | None],
]
_NodeMetadataDictT = MutableMapping[Type[MetadataProvider[_T]], _T | None]


MetadataProviderT = TypeVar("MetadataProviderT", bound=MetadataProvider[Any])
NodePredicateFnT = Callable[[Node, "BaseVisitor"], bool] | Callable[[Node], bool]
NodeVisitorFnT = Callable[["BaseVisitor", Node], _R | None]


class BaseVisitor(ABC):
    """Base class for a visitor that traverses a tree and calls methods on each target_node."""

    named_only = False
    _leave_predicates: list[tuple[tuple[NodePredicateFnT], NodeVisitorFnT]] = []
    _visit_predicates: list[tuple[tuple[NodePredicateFnT], NodeVisitorFnT]] = []

    _metadata_providers: _MetadataProviderDictT
    _metadata: _MetadataDictT

    # Metadata providers for the visitor, to be defined by derived classes
    METADATA_PROVIDERS: ClassVar[Tuple[Type[MetadataProvider[Any]], ...]] = ()

    def __init__(self, *args, **kwargs) -> None:
        self._metadata_providers = {}
        self._metadata = {}

    # @cache
    def metadata_for_node(self, provider_type, node: Node) -> _NodeMetadataDictT[_T]:
        """Get the provider for a target_node by its ID.

        Args:
            provider_type: Metadata provider class
            node: The target_node to get the provider for.

        Returns: The provider for the target_node, for the given provider type.
        """
        return self._metadata.get(provider_type).get(node.id)

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

    def traverse(self, tree: TreeCursor | Tree) -> None:
        """Traverse the tree and call the visitor's methods."""
        cursor = tree.walk() if isinstance(tree, Tree) else tree
        if self.named_only and not cursor.node.is_named:
            return

        should_traverse_children = self._visit(cursor.node)

        if should_traverse_children is not False:
            # Traverse the cursor.target_node's children
            if cursor.goto_first_child():
                self.traverse(cursor)
                while cursor.goto_next_sibling():
                    self.traverse(cursor)
                cursor.goto_parent()

        # Call the visitor's leave methods
        leave_result = self._leave(cursor.node)
        self._handle_leave_return_value(cursor.node, leave_result)

    def _visit(self, node: Node) -> bool | None:
        """Call the visitor's visit methods."""

        # Check if there are any sets of predicates that match the target_node
        # and call the corresponding method if so.
        for predicates, method in self._visit_predicates:
            all_matched = True
            for predicate in predicates:
                # Detect whether we should provide the visitor instance as an
                # argument to the predicate function. No need to worry about
                # bound self/cls/partial arguments, inspect handles that for us
                sig = inspect.signature(predicate)
                args = (node, self) if len(sig.parameters) == 2 else (node,)
                if not predicate(*args):
                    all_matched = False
                    break
            if all_matched:
                return method(self, node)

        method_name = f"visit_{node.type.replace('-', '_')}"
        if specific_method := getattr(self, method_name, None):
            return specific_method(node)
        elif visit_method := getattr(self, "visit", None):
            return visit_method(node)

    def _leave(self, node: Node) -> CodeT | None:
        """Call the visitor's leave methods."""

        # Check if there are any sets of predicates that match the target_node
        # and call the corresponding method if so.
        for predicates, method in self._leave_predicates:
            all_matched = True
            for predicate in predicates:
                # Detect whether we should provide the visitor instance as an
                # argument to the predicate function.
                sig = inspect.signature(predicate)
                args = (node, self) if len(sig.parameters) == 2 else (node,)
                if not predicate(*args):
                    all_matched = False
                    break
            if all_matched:
                return method(self, node)

        method_name = f"leave_{node.type.replace('-', '_')}"
        if specific_method := getattr(self, method_name, None):
            return specific_method(node)
        elif leave_method := getattr(self, "leave", None):
            return leave_method(node)

    def resolve_metadata(self, tree: Tree) -> None:
        for provider_cls in self.METADATA_PROVIDERS:
            provider_instance = provider_cls()
            self._metadata_providers[provider_cls] = provider_instance
            self._metadata[provider_cls] = provider_instance.resolve(tree)
