from __future__ import annotations

import inspect
from abc import ABC
from typing import (
    Callable,
    ParamSpec,
    ClassVar,
    Tuple,
    Type,
    Any,
    TypeVar,
    MutableMapping,
    Generic,
)

from tree_sitter import Node, Tree, TreeCursor

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


class BaseVisitor(ABC, Generic[_T]):
    """Base class for a visitor that traverses a root_node and calls methods on each target_node."""

    _leave_predicates: list[tuple[tuple[NodePredicateFnT], NodeVisitorFnT]] = []
    _visit_predicates: list[tuple[tuple[NodePredicateFnT], NodeVisitorFnT]] = []

    _metadata_providers: _MetadataProviderDictT
    _metadata: _MetadataDictT

    # Metadata providers for the visitor, to be defined by derived classes
    METADATA_PROVIDERS: ClassVar[Tuple[Type[MetadataProvider[Any]], ...]] = ()

    def __init__(self) -> None:
        self._metadata_providers = {}
        self._metadata = {}

    def __getitem__(
        self,
        item: Type[MetadataProviderT]
        | Node
        | tuple[Type[MetadataProviderT], Node]
        | tuple[Node, Type[MetadataProviderT]],
    ) -> _T:
        """Get the provider for a target_node by its ID.

        Args:
            item: The target_node to get the provider for.

        Returns: The provider for the target_node, for the given provider type.
        """
        if isinstance(item, tuple):
            provider_type, node = item
            if isinstance(provider_type, Node):
                provider_type, node = node, provider_type
            return self.metadata_for_node(provider_type, node)

        elif isinstance(item, Node):
            return self.all_metadata_for_node(item)
        elif issubclass(item, MetadataProvider):
            return self.all_metadata_for_provider(item)
        else:
            raise TypeError(f"Expected Node or MetadataProvider subclass, got {type(item)}")

    # @cache
    def metadata_for_node(self, provider_type, node: Node) -> _NodeMetadataDictT[_T]:
        """Get the provider for a target_node by its ID.

        Args:
            provider_type: Metadata provider class
            node: The target_node to get the provider for.

        Returns: The provider for the target_node, for the given provider type.
        """
        return self._metadata.get(provider_type).get(node.id)

    def all_metadata_for_node(self, node: Node) -> dict[Type[MetadataProvider[_T]], _T | None]:
        """Get all metadata for a target_node by its ID.

        Args:
            node: The target_node to get the provider for.

        Returns: The provider for the target_node, for the given provider type.
        """
        return {
            provider_type: provider.get(node.id)
            for provider_type, provider in self._metadata.items()
        }

    def all_metadata_for_provider(
        self, provider_type: Type[MetadataProvider[_T]]
    ) -> dict[int, _T | None]:
        """Get all metadata for a provider type.

        Args:
            provider_type: Metadata provider class

        Returns: The provider for the target_node, for the given provider type.
        """
        return self._metadata.get(provider_type)

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

    def traverse(self, *args: object, **kwargs: object) -> _T:
        """Traverse the root_node and call the visitor's methods."""
        self.resolve_metadata()
        self._traverse(self._tree.walk())
        return self

    def _traverse(self, cursor: TreeCursor) -> None:
        """Traverse the target_node and call the visitor's methods."""
        visit_result = self._visit(cursor.node)
        should_traverse_children = visit_result is True or visit_result is None

        if should_traverse_children is not False:
            # Traverse the cursor.target_node's children
            if cursor.goto_first_child():
                self._traverse(cursor)
                while cursor.goto_next_sibling():
                    self._traverse(cursor)
                cursor.goto_parent()

        # Call the visitor's leave methods.
        # We discard the return value of the leave methods here,
        # but subclasses can override _handle_leave_return_value to
        # handle it. It's mainly intended to make integration easier
        # for the BaseTransformer while still having a consistent
        # leave interface for the visitor.
        leave_result = self._leave(cursor.node)
        self._handle_leave_return_value(cursor.node, leave_result)

    def _visit(self, node: Node) -> bool | None:
        """Call the visitor's visit methods.

        Parameters:
            node: The target_node to visit.

        Returns:
            Whether to traverse the target_node's children. If None, the default
                behavior is to traverse the target_node's children.

        This method is *not* meant to be overriden by subclasses as the `visit`
        method is, to act on a visited node. Instead, subclasses should override
        the `visit` method to act on a visited node.

        This method performs the logic for deciding which, if any, of the
        visitor's visit methods to call for the given node. As of now, only
        the first matched method is called; this is the most specific matching
        method, as per the criteria:

        - If there's an @on_visit method that matches the target_node, it is called.
        - If there's multiple, the first registered one will be called.
        - If there's a method called `visit_<node.type>` in the visitor subclass, that is called.
        - If there's a method called `visit` in the visitor subclass, that is called.
        """

        # Check if there are any sets of predicates that match the target_node
        # and call the corresponding method if so
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
        """Call the visitor's leave methods.

        This method is *not* meant to be overriden by subclasses as the `leave`
        method is, to act on a left node. Instead, subclasses should override
        the `leave` method to act on a node when leaving it.

        See the docstring for `_visit` for more information on the logic for
        deciding which, if any, of the visitor's leave methods to call for the
        given node.
        """

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

    def resolve_metadata(self) -> None:
        for provider_cls in self.METADATA_PROVIDERS:
            provider_instance = provider_cls()
            self._metadata_providers[provider_cls] = provider_instance
            self._metadata[provider_cls] = provider_instance.resolve(self._tree)
