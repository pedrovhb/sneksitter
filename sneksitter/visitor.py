from __future__ import annotations

import inspect
import textwrap
from collections import defaultdict
from enum import Enum, auto
from pathlib import Path
from typing import (
    Callable,
    TypeVar,
    TypeAlias,
    Generic,
    Literal,
    Protocol,
    ParamSpec,
    ClassVar,
    overload,
)

from tree_sitter import Node

from sneksitter.q import Q
from sneksitter.utils import CodeT, normalize_code, on_visit, on_leave

TraversalReturnT = TypeVar("TraversalReturnT")
NodePredicateFn: TypeAlias = Callable[[Node], bool]

_VisitResultT = TypeVar("_VisitResultT", covariant=True)

_P = ParamSpec("_P")
_T_co = TypeVar("_T_co", covariant=True)


class TraversalAction(Enum):
    Continue = auto()
    SkipSubtree = auto()
    Stop = auto()

    @classmethod
    def default_action(cls) -> TraversalAction:
        return cls.Continue


class NodeVisitFn(Protocol[_VisitResultT]):
    def __call__(
        self, visitor: TSVisitor[TraversalReturnT], node: Node
    ) -> TraversalAction | _VisitResultT | None:
        ...


class TSVisitor(Generic[TraversalReturnT]):
    def __init__(self, root_node: Node) -> None:
        self.root_node = root_node
        self._stack: list[Node] = [root_node]
        self._replacements: list[tuple[Node, CodeT]] = []

    _visit_predicate_methods: ClassVar[list[tuple[str, list[Callable]]]]
    _leave_predicate_methods: ClassVar[list[tuple[str, list[Callable]]]]

    _visit_type_methods: ClassVar[dict[str, NodeVisitFn]]
    _leave_type_methods: ClassVar[dict[str, NodeVisitFn]]

    def __init_subclass__(cls) -> None:
        cls._visit_predicate_methods = []
        cls._leave_predicate_methods = []

        cls._visit_type_methods = {}
        cls._leave_type_methods = {}

        for name, member in inspect.getmembers(cls):
            if (predicates := getattr(member, "_leave_predicates", None)) is not None:
                cls._leave_predicate_methods.append((predicates, member))
            if (predicates := getattr(member, "_visit_predicates", None)) is not None:
                cls._visit_predicate_methods.append((predicates, member))

            # if isinstance(member, PredicateWrapper):
            #     if member.event_type == "visit":
            #         cls._visit_predicate_methods.append(member)
            #     elif member.event_type == "leave":
            #         cls._leave_predicate_methods.append(member)
            #     else:
            #         raise ValueError(f"Unexpected event type {member.event_type}")

            if inspect.isfunction(member):
                if name.startswith("visit_"):
                    cls._visit_type_methods[name[6:]] = member

                elif name.startswith("leave_"):
                    cls._leave_type_methods[name[6:]] = member

    def _get_method_for_node(
        self,
        node: Node,
        event: Literal["visit", "leave"],
    ) -> NodeVisitFn | None:
        if event == "visit":
            type_name_methods = self._visit_type_methods
            predicate_methods = self._visit_predicate_methods
        else:
            type_name_methods = self._leave_type_methods
            predicate_methods = self._leave_predicate_methods

        for predicate_set, method in predicate_methods:
            if any(all(pred(node) for pred in preds) for preds in predicate_set):
                selected_method = method
                break
        else:
            selected_method = type_name_methods.get(node.type, None)
            selected_method = selected_method or type_name_methods.get("default", None)

        return selected_method

    def _perform_leave(self, traversed_node: Node) -> TraversalAction:
        leave_method = self._get_method_for_node(traversed_node, event="leave")
        if leave_method is None:
            return TraversalAction.default_action()

        result = leave_method(self, traversed_node)
        processed_result = self._handle_leave_result(traversed_node, result)
        return processed_result

    def _handle_leave_result(
        self,
        traversed_node: Node,
        result: TraversalAction | None,
    ) -> TraversalAction:
        if isinstance(result, TraversalAction):
            return result
        elif result is None:
            return TraversalAction.default_action()
        else:
            raise TypeError(f"Unexpected return from leave method: {type(result)}")

    def _perform_visit(self, traversed_node: Node) -> TraversalAction:
        visit_method = self._get_method_for_node(traversed_node, event="visit")
        if visit_method is None:
            return TraversalAction.default_action()

        result = visit_method(self, traversed_node)
        processed_result = self._handle_visit_result(traversed_node, result)
        if isinstance(processed_result, TraversalAction):
            return processed_result
        elif processed_result is None:
            return TraversalAction.default_action()
        else:
            raise TypeError(f"Unexpected return from visit method: {type(processed_result)}")

    def _handle_visit_result(
        self,
        traversed_node: Node,
        result: TraversalAction | None,
    ) -> TraversalAction:
        if isinstance(result, TraversalAction):
            return result
        elif result is None:
            return TraversalAction.default_action()
        else:
            raise TypeError(f"Unexpected return from visit method: {type(result)}")

    def _traverse(self, traversed_node: Node) -> TraversalAction:
        self._stack.append(traversed_node)
        try:
            visit_action = self._perform_visit(traversed_node)

            if visit_action != TraversalAction.SkipSubtree:
                for child in traversed_node.children:
                    child_action = self._traverse(child)
                    if child_action == TraversalAction.Stop:
                        return TraversalAction.Stop

            leave_action = self._perform_leave(traversed_node)

            if leave_action == TraversalAction.Stop:
                return TraversalAction.Stop
            elif leave_action == TraversalAction.SkipSubtree:
                raise ValueError("Leave action cannot be SkipSubtree")
            else:
                return visit_action

        finally:
            self._stack.pop()

    @property
    def crt_depth(self) -> int:
        return len(self._stack)

    @property
    def traversal_stack(self) -> tuple[Node, ...]:
        return tuple(self._stack)

    def get_traversal_result(self) -> TraversalReturnT:
        ...

    def traverse(self) -> TraversalReturnT:
        self._traverse(self.root_node)
        return self.get_traversal_result()


class TSTransformer(TSVisitor[bytes]):
    def add_replacement(self, node: Node, replacement: CodeT) -> None:
        self._replacements.append((node, replacement))

    def _resolve_replacements(self) -> bytes:
        code = self.root_node.text
        import tree_sitter_languages

        parser = tree_sitter_languages.get_parser("python")
        tree = parser.parse(code)

        # Get a postorder list of replacements
        def traverse_postorder(node: Node) -> Iterable[Node]:
            for child in node.children[::-1]:
                yield from traverse_postorder(child)
            yield node

        def traverse_preorder(node: Node) -> Iterable[Node]:
            yield node
            for child in node.children[::-1]:
                yield from traverse_preorder(child)

        replacements_dict = {node: replacement for node, replacement in self._replacements}
        for node in traverse_preorder(self.root_node):
            if node not in replacements_dict:
                continue
            replacement = replacements_dict[node]
            new_code = normalize_code(replacement)
            tree.ed
            # new_code_lines = new_code.splitlines()
            # end_col = node.start_point[1] + len(new_code_lines[-1])
            # end_line = node.start_point[0] + len(new_code_lines) - 1
            # new_end_point = (end_line, end_col)

            # edit_range = dict(
            #     start_byte=node.start_byte,
            #     old_end_byte=node.end_byte,
            #     new_end_byte=node.start_byte + len(replacement),
            #     start_point=node.start_point,
            #     old_end_point=node.end_point,
            #     new_end_point=new_end_point,
            # )
            # tree.edit(**edit_range)
            code = code[: node.start_byte] + replacement + code[node.end_byte :]
            # tree = parser.parse(code, tree)
            # node.edit(**edit_range)
            # code = tree.text
            print(code.decode())
            print("========\n\n")

        # for node in reversed(list(traverse_postorder(self.root_node))):
        #     if node not in replacements_dict:
        #         continue
        #     replacement = replacements_dict[node]
        #     new_code = normalize_code(replacement)
        #     new_code_lines = new_code.splitlines()
        #     end_col = node.start_point[1] + len(new_code_lines[-1])
        #     end_line = node.start_point[0] + len(new_code_lines) - 1
        #     new_end_point = (end_line, end_col)
        #     node.edit(
        #         start_byte=node.start_byte,
        #         old_end_byte=node.end_byte,
        #         new_end_byte=node.start_byte + len(replacement),
        #         start_point=node.start_point,
        #         old_end_point=node.end_point,
        #         new_end_point=new_end_point,
        #     )
        #     code = code[: node.start_byte] + replacement + code[node.end_byte :]
        #
        #     tree = parser.parse(code, tree)
        #     code = tree.text

        return code

    def _handle_leave_result(
        self, traversed_node: Node, result: TraversalAction | CodeT
    ) -> TraversalAction:
        if isinstance(result, (str, bytes, Node)):
            self.add_replacement(traversed_node, result)
            result = TraversalAction.default_action()
        return super()._handle_leave_result(traversed_node, result)

    def get_traversal_result(self) -> bytes:
        return self._resolve_replacements()


if __name__ == "__main__":

    def demo() -> None:
        from tree_sitter_languages import get_parser

        parser_markdown = get_parser("markdown")

        sample_markdown = textwrap.dedent(
            """\
            # Some sample markdown

            A little known fact: Markdown was invented in 1438AC by a monk named John Markdown.
            It was originally called "John's Markup", but the name was changed to "Markdown" in 
            1439AC following a series of unfortunate events which ultimately led to John 
            renouncing his faith and becoming a pirate.

            Markdown originally didn't support links, but they were added in 1440AC when John
            was trying to figure out how to direct people to [his website](https://johnswebsite.com).

            ![A picture of John](https://johnswebsite.com/john.jpg)


            ## A list of things

            - Thing 1
            - Thing 2
              - Thing 2.1
                - Thing 2.2 [with a link](https://example.com)
            - Thing 3
            """
        ).encode()

        tree_markdown = parser_markdown.parse(sample_markdown)

        class MarkdownLinkRemovalVisitor(TSTransformer):
            @on_leave(lambda node: node.type == "link")
            def replace_link(self, node: Node) -> bytes:
                link_text_node = node.children[0]
                assert link_text_node.type == "link_text"
                print(f"Replacing link {node.text} with text {link_text_node.text}")
                return link_text_node.text

            def leave_image(self, node: Node) -> bytes:
                """Replace images with their alt text."""
                image_description = node.children[0]
                assert image_description.type == "image_description"
                return b"<image: " + image_description.text + b">"

        visitor = MarkdownLinkRemovalVisitor(tree_markdown.root_node)
        result = visitor.traverse()
        print(result.decode())

        parser_python = get_parser("python")
        sample_python = textwrap.dedent(
            """\
            def foo(some, args, *varargs, some: int, some: float=3.14, **kwargs):
                print("Hello, World!")

            class Bar:

                def __init__(self) -> None:
                    pass

                def foo(self):
                    pass

            foo()"""
        ).encode()

        class PrintParamsVisitor(TSVisitor):
            definition_stack: list[Node] = []
            parameter_mapping = defaultdict[Node, list[str]](list)

            def visit_function_definition(self, node: Node) -> None:
                self.definition_stack.append(node)

            def leave_function_definition(self, node: Node) -> None:
                self.definition_stack.pop()

            @on_visit(Q(parent__type="parameters") & Q(is_named=True))
            def my_parameter_visitor(self, node: Node) -> None:
                latest_definition = self.definition_stack[-1] if self.definition_stack else None
                self.parameter_mapping[latest_definition].append(node.text)

            def visit_default(self, node: Node) -> TraversalAction:
                print(
                    self.crt_depth * "  ",
                    node.type,
                    node.text.decode().replace("\n", "\\n"),
                )
                return TraversalAction.default_action()

            def get_traversal_result(self) -> dict[Node, list[str]]:
                return self.parameter_mapping

        tree = parser_python.parse(sample_python)

        params = PrintParamsVisitor(tree.root_node).traverse()
        for node, param_names in params.items():
            print(node.child_by_field_name("name").text.decode())
            print("  ", param_names)

        # foo
        #    [b'some', b'args', b'*varargs', b'some: int', b'some: float=3.14', b'**kwargs']
        # __init__
        #    [b'self']
        # foo
        #    [b'self']

        class NestedDictVisitor(TSVisitor):
            class_stack: list[str] = []  # Stack to track the current class scope
            function_mapping: dict = defaultdict(
                lambda: defaultdict(list)
            )  # Nested dictionary for function parameters

            def visit_class_definition(self, node: Node) -> None:
                class_name = node.child_by_field_name("name").text.decode()
                self.class_stack.append(class_name)

            def leave_class_definition(self, node: Node) -> None:
                self.class_stack.pop()

            def visit_function_definition(self, node: Node) -> None:
                current_scope = self.class_stack[-1] if self.class_stack else "root"
                function_name = node.child_by_field_name("name").text.decode()
                self.function_mapping[current_scope][function_name] = []

            @on_visit(
                lambda node: node.parent and node.parent.type == "parameters",
                lambda node: node.is_named,
            )
            def my_parameter_visitor(self, node: Node) -> None:
                if node.parent and node.parent.type == "parameters" and node.is_named:
                    current_scope = self.class_stack[-1] if self.class_stack else "root"
                    function_node = node.parent.parent
                    function_name = function_node.child_by_field_name("name").text.decode()
                    self.function_mapping[current_scope][function_name].append(node.text.decode())

            def get_traversal_result(self) -> dict:
                return self.function_mapping

        # Traversing the tree and getting the result
        nested_dict_visitor = NestedDictVisitor(tree.root_node)
        nested_dict_visitor.traverse()
        result = nested_dict_visitor.get_traversal_result()
        print(result)

        def get_directory_fn_overview(path: Path):
            # Build a mapping of directories and python files recursively
            py_files = list(path.rglob("*.py"))
            # For each python file, parse it and get the function mapping
            function_mapping = {}
            for py_file in py_files:
                with open(py_file, "rb") as f:
                    code = f.read()
                tree = parser_python.parse(code)
                function_mapping[py_file] = NestedDictVisitor(tree.root_node).traverse()

            # Break out the function mapping into a directory mapping
            directory_mapping = defaultdict(list)
            for py_file, functions in function_mapping.items():
                directory_mapping[py_file.parent].append(functions)
            return directory_mapping

        overview = get_directory_fn_overview(Path("."))
        # print as yaml
        import yaml

        print(yaml.dump(overview))

    demo()
