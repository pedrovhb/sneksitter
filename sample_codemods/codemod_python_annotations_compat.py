import re
from pathlib import Path

from tree_sitter import Node
from tree_sitter_languages import get_parser

# from sneksitter.q import Q
from sneksitter.transformer import BaseTransformer
from sneksitter.utils import on_visit


class AnnotationCompatibilityTransformer(BaseTransformer):
    RE_TYPE_SUBSCRIPTION = re.compile(rb"([a-z]\w+)\[(.+)]")

    # def visit_type(self, node: Node) -> bytes:
    #     print(node.text)
    #     return node.text

    @on_visit(+Q(type="type"))
    def visit_node(self, node: Node) -> bytes:
        print(node.type, node.text)

        return node.text


if __name__ == "__main__":
    parser = get_parser("python")
    new_tree = AnnotationCompatibilityTransformer(parser).transform(Path(__file__))
    print(new_tree.text.decode())
