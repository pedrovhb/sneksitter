import inspect
from dataclasses import fields
from tree_sitter import Node as TS_Node
from typing import Generic, TypeVar, Callable, Union, TypeAlias

from sneksitter._node_codegen.base_generic_node import BaseGenericNode


_T = TypeVar("_T")
_LanguageNodeT = TypeVar("_LanguageNodeT", bound="BaseGenericNode")
CodeT: TypeAlias = Union[str, bytes, TS_Node, "BaseGenericNode"]
NodePredicateFnT = Callable[[TS_Node, "BaseVisitor"], bool] | Callable[[TS_Node], bool]
NodeVisitorFnT = Callable[["BaseVisitor", TS_Node], _T | None]


class BaseGenericVisitor(Generic[_LanguageNodeT]):
    _leave_predicates: list[tuple[tuple[NodePredicateFnT], NodeVisitorFnT]] = []
    _visit_predicates: list[tuple[tuple[NodePredicateFnT], NodeVisitorFnT]] = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        for method in cls.__dict__.values():
            if ps := getattr(method, "_visit_predicates", None):
                cls._visit_predicates.extend((predicates, method) for predicates in ps)
            if ps := getattr(method, "_leave_predicates", None):
                cls._leave_predicates.extend((predicates, method) for predicates in ps)

    def traverse(self, target_node: _LanguageNodeT) -> None:
        print(f"traverse {target_node}")
        self._traverse(target_node)

    def _traverse(self, node: _LanguageNodeT) -> None:
        """Traverse the target_node and call the visitor's methods."""
        # ic("_traverse", node)
        visit_result = self._visit(node)
        should_traverse_children = visit_result is True or visit_result is None

        if should_traverse_children is not False:
            for child in node.named_children:
                self._traverse(child)

        # Call the visitor's leave methods.
        # We discard the return value of the leave methods here,
        # but subclasses can override _handle_leave_return_value to
        # handle it. It's mainly intended to make integration easier
        # for the BaseTransformer while still having a consistent
        # leave interface for the visitor.
        leave_result = self._leave(node)
        self._handle_leave_return_value(node, leave_result)

    def _visit(self, node: _LanguageNodeT) -> bool | None:
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

        method_name = f"visit_{node.__class__.__name__}"
        if self.is_method_overridden(method_name):
            specific_method = getattr(self, method_name)
            return specific_method(node)
        else:
            print(
                f"Generic visit to {node}; {method_name=}, {self.is_method_overridden(method_name)=}"
            )
            return self.visit(node)

    def _leave(self, node: _LanguageNodeT) -> CodeT | None:
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

        method_name = f"leave_{node.__class__.__name__}"
        if self.is_method_overridden(method_name):
            specific_method = getattr(self, method_name)
            return specific_method(node)
        else:
            return self.leave(node)

    def leave(self, node: _LanguageNodeT) -> CodeT | None:
        pass

    def visit(self, node: _LanguageNodeT) -> CodeT | None:
        pass

    def is_method_overridden(self, method_name):
        """Check if 'method_name' is overridden in the current class."""
        # Try to get the attribute from the current instance
        current_class_method = getattr(self, method_name, None)
        # If the method does not exist at all, it's not overridden
        if current_class_method is None:
            return False

        # Get the base class for the current instance
        for base_class in self.__class__.__mro__[2:]:
            # Try to get the attribute from the base class
            base_class_method = getattr(base_class, method_name, None)
            if base_class_method:
                # If a base class method is found, compare the methods
                if isinstance(base_class_method, (staticmethod, classmethod)):
                    # For static and class methods, compare the function objects directly
                    return current_class_method.__func__ is not base_class_method.__func__
                else:
                    # For instance methods, use __func__ to access the original function object
                    return current_class_method.__func__ is not getattr(
                        base_class_method, "__func__", None
                    )
        return False  # If no base class has the method, it cannot be overridden

    def _handle_leave_return_value(
        self, node: _LanguageNodeT, leave_result: CodeT | None = None
    ) -> None:
        pass
