import re
from pathlib import Path
from typing import Union

from tree_sitter import Node
from tree_sitter_languages import get_parser

from sneksitter.transformer import BaseTransformer
from sneksitter.utils import on_visit


class AnnotationCompatibilityTransformer(BaseTransformer):
    RE_TYPE_SUBSCRIPTION = re.compile(rb"(?P<name>:[a-z]\w+)\[(?P<subscript>:.+)]")

    # def visit_type(self, root_node: Node) -> bytes:
    #     print(root_node.text)
    #     return root_node.text

    def parse_type(self, node_text: bytes) -> bytes:
        if node_text == b"Union[str, int]":
            return b"Any"

        def _handle_subscription(match: re.Match) -> bytes:
            print("handlity")
            if match.group(b"name") == b"Union":
                print("splittitly")
                # todo would split into |
                return b"typing.Union[" + match.group("subscript") + "]"

        return re.sub(
            self.RE_TYPE_SUBSCRIPTION,
            _handle_subscription,
            node_text,
        )

    def visit_type(self, node: Node) -> bytes:
        print(node.type, node.text)

        return self.parse_type(node.text)


if __name__ == "__main__":

    def foo() -> Union[str, int]:
        return 42

    parser = get_parser("python")
    new_tree = AnnotationCompatibilityTransformer(parser).transform(Path(__file__))
    print(new_tree.text.decode())
