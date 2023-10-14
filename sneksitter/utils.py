from __future__ import annotations

import textwrap
from functools import partial, wraps
from typing import Callable, ParamSpec, TypeVar

_P = ParamSpec("_P")
_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)
_T_contra = TypeVar("_T_contra", contravariant=True)


def _add_predicate_attributes(
    *predicates: Callable[_P, _T_co],
    attr_name: str,
) -> Callable[[Callable[_P, _T_co]], Callable[_P, _T_co]]:
    """Decorator to add predicate attributes to a method, used for @on_leave and @on_visit.

    This can be added to BaseVisitor and BaseTransformer subclass methods in order to register
    a function to be called when a node matches a given predicate. The decorated method will be
    called when the node is left, and the return value of the decorated method will be used
    to replace the node in the tree, if a string or bytes is returned.

    The predicates are added as attributes of the replaced function, and the classes will
    register them when the class is defined via __init_subclass__.

    Args:
        *predicates: The predicates to match.
    """

    def decorator(func: Callable[_P, _T_co]) -> Callable[_P, _T_co]:
        @wraps(func)
        def wrapper(*args: _P.args, **kwargs: _P.kwargs) -> _T_co:
            return func(*args, **kwargs)

        if existing_attr := getattr(wrapper, attr_name, None):
            existing_attr.append(predicates)
        else:
            setattr(wrapper, attr_name, [predicates])

        return wrapper

    return decorator


on_leave = partial(_add_predicate_attributes, attr_name="_leave_predicates")
on_visit = partial(_add_predicate_attributes, attr_name="_visit_predicates")


def get_indentation_from_node(tree, node, code: str):
    statement_node_types = {
        "future_import_statement",
        "import_statement",
        "import_from_statement",
        "print_statement",
        "assert_statement",
        "expression_statement",
        "return_statement",
        "delete_statement",
        "raise_statement",
        "pass_statement",
        "break_statement",
        "continue_statement",
        "global_statement",
        "nonlocal_statement",
        "exec_statement",
        "type_alias_statement",
        "if_statement",
        "for_statement",
        "while_statement",
        "try_statement",
        "with_statement",
        "function_definition",
        "class_definition",
        "decorated_definition",
        "match_statement",
    }

    analyzed_node = node
    nearest_statement_node = None
    while analyzed_node.parent:
        analyzed_node = analyzed_node.parent
        if analyzed_node.type in statement_node_types:
            nearest_statement_node = analyzed_node
            break
    if not nearest_statement_node:
        return code

    line_number = node.start_point[0]
    lines = tree.text.split(b"\n")
    statement_line = lines[line_number - 1]
    indentation = len(statement_line) - len(statement_line.lstrip())
    return textwrap.indent(code, " " * indentation)
