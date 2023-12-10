from __future__ import annotations

import operator
import re
import textwrap
import tree_sitter
from collections import deque
from functools import partial, wraps
from pathlib import Path
from typing import Callable, ParamSpec, TypeVar, Iterator
from collections import deque

from tree_sitter import Tree, Node, TreeCursor
from tree_sitter_languages import get_parser

_P = ParamSpec("_P")
_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)
_T_contra = TypeVar("_T_contra", contravariant=True)

CodeT = str | bytes | Tree | Node | Path


def normalize_code(code: CodeT) -> bytes:
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


class _MissingAttributeT:
    """Sentinel value for when  an attribute is missing from a target_node."""

    def __repr__(self) -> str:
        return "MISSING"


MissingAttribute = _MissingAttributeT()


def ts_traverse_bfs(
    target: Node | Tree,
    yield_filter: Callable[[Node], bool] | None = None,
) -> Iterator[tuple[Node, int]]:
    """
    Breadth-first traversal of a tree_sitter root_node.

    This generator function yields (target_node, depth) tuples in breadth-first order.
    A deque data structure is used for the traversal, thus the traversal is performed in a non-recursive way.
    Depth is reckoned as the count of edges from the root_node's root to the target_node.

    Args:
        target: The cursor to use for traversing the root_node.
        yield_filter: A function that takes a target_node and returns True if the target_node should be yielded.

    Yields:
        A tuple that contains the target_node and its respective depth from the root.
    """
    cursor = target.walk()
    # (cursor_position, depth)
    queue = deque[tuple[TreeCursor, int]]([(cursor.copy(), 0)])

    while queue:
        cursor, depth = queue.popleft()
        if yield_filter is None or yield_filter(cursor.node):
            yield cursor.node, depth

        if cursor.goto_first_child():
            queue.append((cursor.copy(), depth + 1))

            while cursor.goto_next_sibling():
                queue.append((cursor.copy(), depth + 1))

            cursor.goto_parent()


def _add_predicate_attributes(
    *predicates: Callable[_P, _T_co],
    attr_name: str,
    **attr_predicates: Callable[_P, _T_co] | re.Pattern | _T_co,
) -> Callable[[Callable[_P, _T_co]], Callable[_P, _T_co]]:
    """Decorator to add predicate attributes to a method, used for @on_leave and @on_visit.

    This can be added to BaseVisitor and BaseTransformer subclass methods in order to register
    a function to be called when a target_node matches a given predicate. The decorated method will be
    called when the target_node is left, and the return value of the decorated method will be used
    to replace the target_node in the root_node, if a string or bytes is returned.

    The predicates are added as attributes of the replaced function, and the classes will
    register them when the class is defined via __init_subclass__.

    Args:
        *predicates: The predicates to match.
        attr_name: The name of the attribute to add to the function.
        **attr_predicates: kwargs of attr_name: attr_predicate which will be
            checked against attributes of the target object.
    """

    def decorator(func: Callable[_P, _T_co]) -> Callable[_P, _T_co]:
        @wraps(func)
        def wrapper(*args: _P.args, **kwargs: _P.kwargs) -> _T_co:
            return func(*args, **kwargs)

        # Handle kwarg predicate specifications, e.g. @on_leave(type="foo") or
        # @on_leave(text=bytes.isupper)
        attr_predicate_callables = []
        for target_attr, attr_predicate in attr_predicates.items():

            def attr_getter(obj):
                """Get an attribute from an object, traversing dotted attributes."""
                sentinel = object()
                for attr in target_attr.split("__"):
                    obj = getattr(obj, attr, sentinel)
                    if obj is sentinel:
                        return MissingAttribute
                return obj

            if isinstance(attr_predicate, re.Pattern):
                # If the value of the kwarg is a regex, use it to match against the
                # target attribute
                pred = lambda node: bool(attr_predicate.match(attr_getter(node)))
            elif callable(attr_predicate):
                # If the value of the kwarg is a callable, use it as-is - the return
                # value will be truthy or falsy
                pred = lambda node: attr_predicate(attr_getter(node))
            else:
                # If it's not a callable, use it as a value to compare against
                pred = lambda node: attr_getter(node) == attr_predicate

            attr_predicate_callables.append(pred)

        all_predicates = predicates + tuple(attr_predicate_callables)

        if existing_attr := getattr(wrapper, attr_name, None):
            existing_attr.append(all_predicates)
        else:
            setattr(wrapper, attr_name, [all_predicates])

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


NodeKey = tuple[str, bool]
_BaseTypeStructureInternal = dict[NodeKey, set[NodeKey]]
BaseTypeStructure = dict[NodeKey, frozenset[NodeKey]]


def construct_base_type_structure(node_types: List[Dict]) -> BaseTypeStructure:
    """
    Constructs a structure mapping each node type to its direct base types.

    Args:
        node_types (List[Dict]): A list of dictionaries describing node types and their subtypes.

    Returns:
        BaseTypeStructure: A dictionary mapping each node type (identified by a tuple of type and named status)
                           to its set of direct base types.
    """
    base_types: _BaseTypeStructureInternal = {}

    for node in node_types:
        if "subtypes" in node:
            for subtype in node["subtypes"]:
                key: NodeKey = (subtype["type"], subtype.get("named", False))
                base_type_key: NodeKey = (node["type"], node.get("named", False))
                if key not in base_types:
                    base_types[key] = set()
                base_types[key].add(base_type_key)

    base_types_frozen: BaseTypeStructure = {
        node_key: frozenset(base_type_keys) for node_key, base_type_keys in base_types.items()
    }
    return base_types_frozen


def position_for_offset(input_bytes: bytes, offset: int) -> tuple[int, int]:
    """


    Notes:
        Adapted from:

            pub fn position_for_offset(input: &[u8], offset: usize) -> Result<Point> {
                if offset > input.len() {
                    return Err(anyhow!("Failed to address an offset: {offset}"));
                }
                let mut result = Point { row: 0, column: 0 };
                let mut last = 0;
                for pos in memchr::memchr_iter(b'\n', &input[..offset]) {
                    result.row += 1;
                    last = pos;
                }
                result.column = if result.row > 0 {
                    offset - last - 1
                } else {
                    offset
                };
                Ok(result)
            }
    """
    if offset > len(input_bytes):
        raise ValueError()


def edit_node(tree: Tree, node: Node, new_code: bytes) -> Tree:
    """

    Args:
        tree:
        node:
        new_code:

    Returns:

    Notes:
        Adapted from the following tree-sitter code:

            pub fn perform_edit(tree: &mut Tree, input: &mut Vec<u8>, edit: &Edit) -> Result<InputEdit> {
                let start_byte = edit.position;
                let old_end_byte = edit.position + edit.deleted_length;
                let new_end_byte = edit.position + edit.inserted_text.len();
                let start_position = position_for_offset(input, start_byte)?;
                let old_end_position = position_for_offset(input, old_end_byte)?;
                input.splice(start_byte..old_end_byte, edit.inserted_text.iter().cloned());
                let new_end_position = position_for_offset(input, new_end_byte)?;
                let edit = InputEdit {
                    start_byte,
                    old_end_byte,
                    new_end_byte,
                    start_position,
                    old_end_position,
                    new_end_position,
                };
                tree.edit(&edit);
                Ok(edit)
            }

    """


def position_for_offset(input_bytes: bytes, offset: int) -> tuple[int, int]:
    if offset > len(input_bytes):
        raise ValueError("Offset is greater than input length.")
    row = 0
    last_newline_position = 0
    for i, b in enumerate(input_bytes[:offset]):
        if b == ord("\n"):
            row += 1
            last_newline_position = i
    column = offset - (last_newline_position + 1)
    return row, column


def edit_node(tree: Tree, node: Node, new_code: bytes) -> Tree:
    start_byte = node.start_byte
    old_end_byte = node.end_byte
    new_end_byte = start_byte + len(new_code)

    start_position = position_for_offset(tree.root_node.text, start_byte)
    old_end_position = position_for_offset(tree.root_node.text, old_end_byte)
    new_end_position = position_for_offset(tree.root_node.text, new_end_byte)

    tree.edit(
        start_byte=start_byte,
        old_end_byte=old_end_byte,
        new_end_byte=new_end_byte,
        start_point=start_position,
        old_end_point=old_end_position,
        new_end_point=new_end_position,
    )

    # tree.edit(edit)
    return tree
