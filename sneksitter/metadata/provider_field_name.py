from tree_sitter import Tree, TreeCursor

from sneksitter.metadata.base import MetadataProvider


class FieldNameMetadataProvider(MetadataProvider[str]):
    def resolve(self, tree: Tree) -> dict[int, str]:
        """Compute and store metadata for nodes in `self.metadata` dictionary."""
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
