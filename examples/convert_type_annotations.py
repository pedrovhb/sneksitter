from pathlib import Path

from tree_sitter import Node
from tree_sitter_languages import get_parser

from sneksitter.visitor import TSTransformer

# class _AnnotationTransformer(TSTransformer):
#
#     def leave_identifier(self, node: Node) -> bytes:


def foo(x: list[dict[int, int]]) -> int | str | bytes:
    return 1


class AnnotationConverter(TSTransformer):
    def __init__(self, root_node: Node) -> None:
        super().__init__(root_node)
        self._has_import_typing_statement = False
        self._type_stack = []

    @property
    def is_in_type(self) -> bool:
        return bool(self._type_stack)

    def visit_type(self, node: Node) -> None:
        self._type_stack.append(node)
        return None

    def leave_type(self, node: Node) -> None:
        self._type_stack.pop()
        return None

    def visit_import_statement(self, node: Node) -> None:
        if node.text == b"import typing":
            self._has_import_typing_statement = True

    def leave_subscript(self, node: Node) -> None:
        if self.is_in_type:
            subscripted_type = node.named_children[0]
            if subscripted_type.text in (b"list", b"dict", b"tuple", b"set", b"frozenset"):
                self.add_replacement(subscripted_type, b"typing." + subscripted_type.text.title())

    def leave_typed_parameter(self, node: Node) -> bytes:
        print(node)

    def visit_default(self, node: Node) -> None:
        if node.is_named:
            print(" " * self.crt_depth, node.type, node.text[:50].decode().replace("\n", "\\n"))

    # todo - make it easier to allow adding nodes
    # def leave_module(self, node: Node) -> bytes:
    #     if not self._has_import_typing_statement:
    #         self.add_replacement(node, b"import typing\n\n" + node.text)
    #     return node.text


if __name__ == "__main__":
    parser = get_parser("python")
    tree = parser.parse(Path(__file__).read_bytes())
    cleaner = AnnotationConverter(tree.root_node)
    print(cleaner.traverse().decode())
