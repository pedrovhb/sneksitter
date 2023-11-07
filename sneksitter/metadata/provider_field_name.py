from tree_sitter import Tree, TreeCursor

from sneksitter.metadata.base_provider import MetadataProvider
from sneksitter.utils import on_visit, on_leave
from typing import TypeVar

_T = TypeVar("_T")


class FieldNameMetadataProvider(MetadataProvider[str]):
    def resolve(self, tree: Tree) -> dict[int, str]:
        """Compute and store provider for nodes in `self.provider` dictionary."""
        metadata: dict[int, str] = {}

        def _walk(cursor: TreeCursor) -> None:
            metadata[cursor.node.id] = cursor.field_name

            if cursor.goto_first_child():
                _walk(cursor)
                while cursor.goto_next_sibling():
                    _walk(cursor)
                cursor.goto_parent()

        _walk(tree.walk())
        return metadata


if __name__ == "__main__":
    from tree_sitter_languages import get_parser

    parser = get_parser("python")
    tree = parser.parse(b"def foo(a: int=4):\n    pass")

    metadata = FieldNameMetadataProvider().resolve(tree)

    print({node_id: field_name for node_id, field_name in metadata.items() if field_name})
    # {
    #   39275992: 'name',
    #   39276000: 'parameters',
    #   39017232: 'name',
    #   39017248: 'type',
    #   39274640: 'value',
    #   39276024: 'body'
    # }

    from sneksitter import BaseVisitor
    from tree_sitter import Node, Tree
    from tree_sitter_languages import get_parser
    from pathlib import Path

    class DefinitionNameShower(BaseVisitor[dict[str, dict]]):
        METADATA_PROVIDERS = (FieldNameMetadataProvider,)

        def __init__(self, tree: Tree) -> None:
            super().__init__(tree)
            self._definitions_stack = []
            self._definitions_tree = {}

        def traverse(self, *args: object, **kwargs: object) -> _T:
            super().traverse(*args, **kwargs)
            return self._definitions_tree

        @on_visit(
            lambda node, visitor: visitor[FieldNameMetadataProvider, node] == "name",
            parent__type=lambda t: t in ("class_definition", "function_definition"),
        )
        def visit_definition_name(self, node: Node) -> None:
            pass

        @on_leave(
            lambda node, visitor: visitor[FieldNameMetadataProvider, node] == "name",
            parent__type=lambda t: t in ("class_definition", "function_definition"),
        )
        def leave_definition_name(self, node: Node) -> None:
            pass

    parser = get_parser("python")
    tree = parser.parse(Path(__file__).read_bytes())
    print(DefinitionNameShower(tree).traverse())
    print(DefinitionNameShower(tree).traverse())
