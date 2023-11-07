from __future__ import annotations

import textwrap
from functools import lru_cache
from typing import NamedTuple

from tree_sitter import Node

from sneksitter.visitor import BaseVisitor


original_docstring = """Takes a root_node of type `parameter` and returns a Param.

Recursively searches for type, default, vararg, and kwarg.

Args:
    root_node: The root_node to parse.
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
        """Takes a root_node of type `parameter` and returns a Param.

        Recursively searches for type, default, vararg, and kwarg.

        Args:
            node: The root_node to parse.
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
                    raise ValueError(f"Unexpected root_node type {t_node.type}")

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


class Class(NamedTuple):
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
    classes: list[Class] = []

    def visit_class_definition(self, node: Node) -> None:
        self.classes.append(self.make_cls_node(node))

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
                    raise ValueError(f"Unexpected root_node type {t_node.type}")
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
                    raise ValueError(f"Unexpected root_node type {n.type}")
        return Function(**fn_data)

    def make_cls_node(
        self, node: Node, decorators: tuple[bytes] | None = None
    ) -> Class:
        fn_data = {"body": b"", "decorators": decorators or (), "params": ()}
        for n in node.named_children:
            match n:
                case Node(type="identifier", text=name):
                    fn_data["name"] = name
                case Node(type="pararameters", named_children=[*param_nodes]):
                    fn_data["params"] = tuple(
                        Param.parse_recursive(n) for n in param_nodes
                    )  # todo remove params, add functions member
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
                    # raise ValueError(f"Unexpected root_node type {n.type}")
                    print(f"Unexpected root_node type {n.type}")
        return Class(**fn_data)


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

    for fn in visitor.functions:
        print(fn)

    for cls in visitor.classes:
        print(cls)

    # Function(name=b'reindent_complex_docstring', params=(Param(name=b'docstring', type=b'str', default=None, is_vararg=False, is_kwarg=False), Param(name=b'indent', type=b'str', default=b'"    "', is_vararg=False, is_kwarg=False)), body=b'lines = docstring.split("\\n")\nif len(lines) < 2:\n        return textwrap.indent(docstring.strip(), indent)\n# Find the minimum indentation level (ignoring empty lines)\nnon_root_lines = [ln for ln in lines if ln.lstrip() != ln]\nmin_indent = (\n        min(len(ln) - len(ln.lstrip()) for ln in non_root_lines)\n        if non_root_lines\n        else 0\n    )\n# Re-indent the lines relative to the minimum indentation level\nreindented_lines = []\nfor line in lines:\n        stripped_line = line.lstrip()\n        current_indent = len(line) - len(stripped_line)\n        adjusted_indent = current_indent - min_indent\n        reindented_line = " " * adjusted_indent + stripped_line\n        reindented_lines.append(reindented_line)\n# Join the lines back into a single string\nreindented_docstring = "\\n".join(reindented_lines)\nreturn textwrap.indent(reindented_docstring, indent)', return_type=b'str', docstring=None, decorators=())
    # Function(name=b'parse_recursive', params=(Param(name=b'cls', type=None, default=None, is_vararg=False, is_kwarg=False), Param(name=b'root_node', type=b'Node', default=None, is_vararg=False, is_kwarg=False)), body=b'kwargs = {"type": None, "default": None, "is_vararg": False, "is_kwarg": False}\ndef _search_for_type(t_node: Node) -> None:\n            nodes = None\n            match t_node:\n                case Node(type="identifier", text=name):\n                    kwargs["name"] = name\n                case Node(type="type", text=type_):\n                    kwargs["type"] = type_\n                case Node(type="list_splat_pattern", named_children=[*nodes]):\n                    kwargs["is_vararg"] = True\n                case Node(type="dictionary_splat_pattern", named_children=[*nodes]):\n                    kwargs["is_kwarg"] = True\n                case Node(\n                    type="default_parameter" | "typed_default_parameter",\n                    named_children=[*nodes, default_node],\n                ):\n                    kwargs["default"] = default_node.text\n                case Node(named_children=[*nodes]):\n                    pass  # just had to bind `nodes` :)\n                case _:\n                    raise ValueError(f"Unexpected root_node type {t_node.type}")\n\n            if nodes is not None:\n                for t_node in nodes:\n                    _search_for_type(t_node)\n_search_for_type(root_node)\nreturn cls(**kwargs)', return_type=b'Param', docstring=b'"""Takes a root_node of type `parameter` and returns a Param.\n\n        Recursively searches for type, default, vararg, and kwarg.\n\n        Args:\n            root_node: The root_node to parse.\n            something_else: another test.\n\n        Returns:\n            The parsed parameter.\n\n        Raises:\n            YouGotUnluckyException: If the function feels like it. This is a bit of a longer one\n                so that we can test the reindenting.\n        """', decorators=(b'@classmethod',))
    # Function(name=b'unparse', params=(Param(name=b'self', type=None, default=None, is_vararg=False, is_kwarg=False),), body=b'star = "*" if self.is_vararg else ""\nstar = "**" if self.is_kwarg else star\ntype_ = f": {self.type.decode()}" if self.type else ""\ndefault = f"= {self.default.decode()}" if self.default else ""\nreturn f"{star}{self.name.decode()}{type_}{default}"', return_type=b'str', docstring=b'"""Reconstructs the parameter as a string."""', decorators=())
    # Function(name=b'unparse', params=(Param(name=b'self', type=None, default=None, is_vararg=False, is_kwarg=False), Param(name=b'indent', type=b'str', default=b'"    "', is_vararg=False, is_kwarg=False)), body=b'params = ", ".join(p.unparse() for p in self.params)\nreturn_type = f" -> {self.return_type.decode()}" if self.return_type else ""\nsignature = f"def {self.name.decode()}({params}){return_type}:"\nnormalized_body = self.body.decode()\nnormalized_body = reindent_complex_docstring(normalized_body, indent)\nif self.docstring:\n            docstring = reindent_complex_docstring(self.docstring.decode(), indent)\n            return f"{signature}\\n{docstring}\\n{normalized_body}"\n        else:\n            return f"{signature}\\n{normalized_body}"', return_type=b'str', docstring=b'"""Reconstructs the function as a bytes string."""', decorators=())
    # Function(name=b'visit_function_definition', params=(Param(name=b'self', type=None, default=None, is_vararg=False, is_kwarg=False), Param(name=b'root_node', type=b'Node', default=None, is_vararg=False, is_kwarg=False)), body=b'self.functions.append(self.make_fn_node(root_node))', return_type=b'None', docstring=None, decorators=())
    # Function(name=b'visit_decorated_definition', params=(Param(name=b'self', type=None, default=None, is_vararg=False, is_kwarg=False), Param(name=b'root_node', type=b'Node', default=None, is_vararg=False, is_kwarg=False)), body=b'decorators: list[bytes] = []\nfor t_node in root_node.named_children:\n            match t_node:\n                case Node(type="decorator", text=dec):\n                    decorators.append(dec)\n                case Node(type="function_definition"):\n                    fn = self.make_fn_node(t_node, decorators=tuple(decorators))\n                    self.functions.append(fn)\n                case _:\n                    raise ValueError(f"Unexpected root_node type {t_node.type}")\nreturn False', return_type=b'bool', docstring=None, decorators=())
    # Function(name=b'make_fn_node', params=(Param(name=b'self', type=None, default=None, is_vararg=False, is_kwarg=False), Param(name=b'root_node', type=b'Node', default=None, is_vararg=False, is_kwarg=False), Param(name=b'decorators', type=b'tuple[bytes] | None', default=b'None', is_vararg=False, is_kwarg=False)), body=b'fn_data = {"body": b"", "decorators": decorators or ()}\nfor n in root_node.named_children:\n            match n:\n                case Node(type="identifier", text=name):\n                    fn_data["name"] = name\n                case Node(type="parameters", named_children=[*param_nodes]):\n                    fn_data["params"] = tuple(\n                        Param.parse_recursive(n) for n in param_nodes\n                    )\n                case Node(type="type", text=type_):\n                    fn_data["return_type"] = type_\n                case Node(type="block", named_children=[*block_nodes]):\n                    possible_docstring, *rest = block_nodes\n                    match possible_docstring:\n                        case Node(\n                            type="expression_statement",\n                            named_children=[Node(type="string", text=docstring)],\n                        ):\n                            fn_data["docstring"] = docstring\n                            fn_data["body"] += b"\\n".join(n.text for n in rest)\n                        case _:\n                            fn_data["body"] += b"\\n".join(n.text for n in block_nodes)\n                case Node(type="comment"):\n                    fn_data["body"] += b"\\n" + n.text + b"\\n"\n                case _:\n                    raise ValueError(f"Unexpected root_node type {n.type}")\nreturn Function(**fn_data)', return_type=b'Function', docstring=None, decorators=())
    # Function(name=b'foo', params=(Param(name=b'bar', type=b'int', default=b'20', is_vararg=False, is_kwarg=False), Param(name=b'some_args', type=None, default=None, is_vararg=True, is_kwarg=False), Param(name=b'kwargs', type=b'int', default=None, is_vararg=False, is_kwarg=True)), body=b'pass', return_type=b'dict[str, int]', docstring=None, decorators=(b'@lru_cache(maxsize=1337)', b'@lru_cache'))
