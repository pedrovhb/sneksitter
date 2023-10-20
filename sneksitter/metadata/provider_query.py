from pathlib import Path

from tree_sitter import Tree, Language

from sneksitter.metadata.base_provider import MetadataProvider
from sneksitter.utils import ts_traverse_bfs


class QueryTagMetadataProvider(MetadataProvider[str]):
    def __init__(self, query: str, language: Language) -> None:
        super().__init__()
        self.query = query
        self.language = language

    def resolve(self, tree: Tree) -> dict[int, str]:
        """Compute and store provider for nodes in `self.provider` dictionary."""
        metadata: dict[int, str] = {}
        compiled_query = self.language.query(self.query)
        captures = compiled_query.captures(tree.root_node)
        for node, tag in captures:
            metadata[node.id] = tag
        return metadata


if __name__ == "__main__":
    from tree_sitter_languages import get_parser, get_language

    parser = get_parser("python")
    language = get_language("python")
    tree = parser.parse(Path(__file__).read_bytes())
    query = """
    (class_definition
        name: (identifier) @class.name
        superclasses: (argument_list (_) @class.superclass)
        body: (block
            (function_definition
                name: (identifier) @method.name
            )
        )
    )
    """
    tag_metadata_provider = QueryTagMetadataProvider(query=query, language=language)
    tag_metadata = tag_metadata_provider.resolve(tree)
    node_ids_to_nodes = {node.id: node for node, depth in ts_traverse_bfs(tree)}

    for node_id, tag in tag_metadata.items():
        if not tag:
            continue
        print(tag, node_ids_to_nodes[node_id].text.decode())

    # Result:
    #   class.name QueryTagMetadataProvider
    #   class.superclass MetadataProvider[str]
    #   method.name __init__
    #   method.name resolve
