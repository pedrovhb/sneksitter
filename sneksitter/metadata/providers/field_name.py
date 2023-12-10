from pathlib import Path

from tree_sitter import Node
from tree_sitter_languages import get_parser

from sneksitter.metadata.base import VisitorBasedMetadataProvider


class FieldNameMetadataProvider(VisitorBasedMetadataProvider[str]):
    """A metadata provider that sets tree-sitter field name as metadata for each node that has it.

    For instance, a Python function_definition node looks like this:

        def
        [name] identifier
        [parameters] parameters
        [body] block

    Where "def" is an anonymous node type, "name", "parameters", and "body" are field names,
    and "identifier", "parameters", and "block" are the node types for the children of the
    function_definition node.
    """

    def visit_default(self, node: Node) -> None:
        for i, child in enumerate(node.children):
            child_field_name = node.field_name_for_child(i)
            if child_field_name is not None:
                self._set_metadata(child, child_field_name)
        return None


if __name__ == "__main__":
    parser = get_parser("python")
    tree = parser.parse(Path(__file__).read_bytes())
    provider = FieldNameMetadataProvider(tree.root_node)
    provider.resolve()

    print(provider)
    for k, v in provider.items():
        print(k, v)
