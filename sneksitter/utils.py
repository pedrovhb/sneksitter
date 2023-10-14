from __future__ import annotations

import textwrap
from collections import deque
from functools import partial, wraps
from pathlib import Path
from typing import Callable, ParamSpec, TypeVar, Iterator
from collections import deque

from tree_sitter import Tree, Node, TreeCursor

_P = ParamSpec("_P")
_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)
_T_contra = TypeVar("_T_contra", contravariant=True)

CodeT = str | bytes | Tree | Node | Path


def _normalize_code(code: CodeT) -> bytes:
    """Normalize code to bytes.

    This function takes any shape of code representation and returns it as bytes.

    Args:
        code: The code-representing object to normalize.

    Returns:
        The normalized code as bytes.

    Raises:
        TypeError: If the code is not a valid type.
    """
    if isinstance(code, str):
        return code.encode()
    if isinstance(code, Path):
        return code.read_bytes()
    if isinstance(code, (Tree, Node)):
        return code.text
    if isinstance(code, bytes):
        return code
    raise TypeError(f"Invalid type for code: {type(code)}")


def ts_traverse_bfs(target: Node | Tree) -> Iterator[tuple[Node, int]]:
    """
    Breadth-first traversal of a tree_sitter tree.

    This generator function yields (node, depth) tuples in breadth-first order.
    A deque data structure is used for the traversal, thus the traversal is performed in a non-recursive way.
    Depth is reckoned as the count of edges from the tree's root to the node.

    Args:
        target: The cursor to use for traversing the tree.

    Yields:
        A tuple that contains the node and its respective depth from the root.
    """
    cursor = target.walk()
    # (cursor_position, depth)
    queue = deque[tuple[TreeCursor, int]]([(cursor.copy(), 0)])

    while queue:
        cursor, depth = queue.popleft()
        yield cursor.node, depth

        if cursor.goto_first_child():
            queue.append((cursor.copy(), depth + 1))

            while cursor.goto_next_sibling():
                queue.append((cursor.copy(), depth + 1))

            cursor.goto_parent()


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
