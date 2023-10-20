from __future__ import annotations

import textwrap
from functools import lru_cache
from typing import NamedTuple

from tree_sitter import Node

from sneksitter.visitor import BaseVisitor


original_docstring = """Takes a node of type `parameter` and returns a Param.

Recursively searches for type, default, vararg, and kwarg.

Args:
    node: The node to parse.
    something_else: another test.

Returns:
    The parsed parameter.

Raises:
    YouGotUnluckyException: If the function feels like it. This is a bit of a longer one
        so that we can test the reindenting.
"""


def reindent_complex_docstring(docstring: str, indent: str = "    ") -> str:
    lines = docstring.split("\n")
    if len(lines) < 2:
        return textwrap.indent(docstring.strip(), indent)

    # Find the minimum indentation level (ignoring empty lines)
    non_root_lines = [ln for ln in lines if ln.lstrip() != ln]
    min_indent = (
        min(len(ln) - len(ln.lstrip()) for ln in non_root_lines)
        if non_root_lines
        else 0
    )

    # Re-indent the lines relative to the minimum indentation level
    reindented_lines = []
    for line in lines:
        stripped_line = line.lstrip()
        current_indent = len(line) - len(stripped_line)
        adjusted_indent = current_indent - min_indent
        reindented_line = " " * adjusted_indent + stripped_line
        reindented_lines.append(reindented_line)

    # Join the lines back into a single string
    reindented_docstring = "\n".join(reindented_lines)
    return textwrap.indent(reindented_docstring, indent)


class Param(NamedTuple):
    name: bytes
    type: bytes | None
    default: bytes | None
    is_vararg: bool
    is_kwarg: bool

    @classmethod
    def parse_recursive(cls, node: Node) -> Param:
        """Takes a node of type `parameter` and returns a Param.

        Recursively searches for type, default, vararg, and kwarg.

        Args:
            node: The node to parse.
            something_else: another test.

        Returns:
            The parsed parameter.

        Raises:
            YouGotUnluckyException: If the function feels like it. This is a bit of a longer one
                so that we can test the reindenting.
        """
        kwargs = {"type": None, "default": None, "is_vararg": False, "is_kwarg": False}

        def _search_for_type(t_node: Node) -> None:
            nodes = None
            match t_node:
                case Node(type="identifier", text=name):
                    kwargs["name"] = name
                case Node(type="type", text=type_):
                    kwargs["type"] = type_
                case Node(type="list_splat_pattern", named_children=[*nodes]):
                    kwargs["is_vararg"] = True
                case Node(type="dictionary_splat_pattern", named_children=[*nodes]):
                    kwargs["is_kwarg"] = True
                case Node(
                    type="default_parameter" | "typed_default_parameter",
                    named_children=[*nodes, default_node],
                ):
                    kwargs["default"] = default_node.text
                case Node(named_children=[*nodes]):
                    pass  # just had to bind `nodes` :)
                case _:
                    raise ValueError(f"Unexpected node type {t_node.type}")

            if nodes is not None:
                for t_node in nodes:
                    _search_for_type(t_node)

        _search_for_type(node)
        return cls(**kwargs)

    def unparse(self) -> str:
        """Reconstructs the parameter as a string."""
        star = "*" if self.is_vararg else ""
        star = "**" if self.is_kwarg else star
        type_ = f": {self.type.decode()}" if self.type else ""
        default = f"= {self.default.decode()}" if self.default else ""
        return f"{star}{self.name.decode()}{type_}{default}"


class Function(NamedTuple):
    name: bytes
    params: tuple[Param]
    body: bytes | None = None
    return_type: bytes | None = None
    docstring: bytes | None = None
    decorators: tuple[str] | None = None

    def unparse(self, indent: str = "    ") -> str:
        """Reconstructs the function as a bytes string."""
        params = ", ".join(p.unparse() for p in self.params)
        return_type = f" -> {self.return_type.decode()}" if self.return_type else ""
        signature = f"def {self.name.decode()}({params}){return_type}:"

        normalized_body = self.body.decode()
        normalized_body = reindent_complex_docstring(normalized_body, indent)
        if self.docstring:
            docstring = reindent_complex_docstring(self.docstring.decode(), indent)
            return f"{signature}\n{docstring}\n{normalized_body}"
        else:
            return f"{signature}\n{normalized_body}"


class ParamGathererVisitor(BaseVisitor):
    functions: list[Function] = []

    def visit_function_definition(self, node: Node) -> None:
        self.functions.append(self.make_fn_node(node))

    def visit_decorated_definition(self, node: Node) -> bool:
        decorators: list[bytes] = []
        for t_node in node.named_children:
            match t_node:
                case Node(type="decorator", text=dec):
                    decorators.append(dec)
                case Node(type="function_definition"):
                    fn = self.make_fn_node(t_node, decorators=tuple(decorators))
                    self.functions.append(fn)
                case _:
                    raise ValueError(f"Unexpected node type {t_node.type}")
        return False

    def make_fn_node(
        self, node: Node, decorators: tuple[bytes] | None = None
    ) -> Function:
        fn_data = {"body": b"", "decorators": decorators or ()}
        for n in node.named_children:
            match n:
                case Node(type="identifier", text=name):
                    fn_data["name"] = name
                case Node(type="parameters", named_children=[*param_nodes]):
                    fn_data["params"] = tuple(
                        Param.parse_recursive(n) for n in param_nodes
                    )
                case Node(type="type", text=type_):
                    fn_data["return_type"] = type_
                case Node(type="block", named_children=[*block_nodes]):
                    possible_docstring, *rest = block_nodes
                    match possible_docstring:
                        case Node(
                            type="expression_statement",
                            named_children=[Node(type="string", text=docstring)],
                        ):
                            fn_data["docstring"] = docstring
                            fn_data["body"] += b"\n".join(n.text for n in rest)
                        case _:
                            fn_data["body"] += b"\n".join(n.text for n in block_nodes)
                case Node(type="comment"):
                    fn_data["body"] += b"\n" + n.text + b"\n"
                case _:
                    raise ValueError(f"Unexpected node type {n.type}")
        return Function(**fn_data)


if __name__ == "__main__":
    from pathlib import Path
    from tree_sitter_languages import get_parser

    parser = get_parser("python")
    source = Path(__file__).read_bytes()
    tree = parser.parse(source)

    @lru_cache(maxsize=1337)
    @lru_cache
    def foo(bar: int = 20, *some_args, **kwargs: int) -> dict[str, int]:
        pass

    visitor = ParamGathererVisitor(parser)
    visitor.traverse(tree)
    print(visitor.functions)
