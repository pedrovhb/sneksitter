from typing import Callable, Literal, Generic, TypeVar, ParamSpec

from tree_sitter import Node

from sneksitter.visitor import NodePredicateFn

_P = ParamSpec("_P")
_T_co = TypeVar("_T_co", covariant=True)


class PredicateWrapper(Generic[_P, _T_co]):
    def __init__(
        self,
        func: Callable[_P, _T_co],
        predicates: tuple[NodePredicateFn, ...],
        event_type: Literal["visit", "leave"],
    ) -> None:
        self.func = func
        self.predicate_sets = [predicates]
        self.event_type = event_type

    def add_predicate_set(self, *predicates: NodePredicateFn) -> None:
        """Add a set of predicates for which, if all match, the function will be called."""
        self.predicate_sets.append(predicates)

    def node_matches(self, node: Node) -> bool:
        return any(all(pred(node) for pred in preds) for preds in self.predicate_sets)


def on_visit(
    *predicates: NodePredicateFn,
) -> Callable[[Callable[_P, _T_co]], PredicateWrapper[_P, _T_co]]:
    def decorator(__method: Callable[_P, _T_co]) -> PredicateWrapper[_P, _T_co]:
        if isinstance(__method, PredicateWrapper):
            __method.add_predicate_set(*predicates)
            return __method
        else:
            return PredicateWrapper(__method, predicates, event_type="visit")

    return decorator  # type: ignore


def on_leave(
    *predicates: NodePredicateFn,
) -> Callable[[Callable[_P, _T_co]], PredicateWrapper[_P, _T_co]]:
    def decorator(__method: Callable[_P, _T_co]) -> PredicateWrapper[_P, _T_co]:
        if isinstance(__method, PredicateWrapper):
            __method.add_predicate_set(*predicates)
            return __method
        else:
            return PredicateWrapper(__method, predicates, event_type="leave")

    return decorator  # type: ignore
