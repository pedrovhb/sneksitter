from collections import defaultdict
from functools import cached_property
from pathlib import Path

from tree_sitter import Language, Node, Query

from sneksitter.metadata.base import MetadataProvider


class QueryTagMetadataProvider(MetadataProvider[set[str]]):
    def __init__(
        self,
        root_node: Node,
        query: str | Query,
        language: Language | None = None,
    ) -> None:
        super().__init__()
        self.root_node = root_node
        if isinstance(query, str):
            if language is None:
                raise ValueError("language must be provided if query is a string")
            self.query = language.query(query)
        else:
            if not isinstance(query, Query):
                raise TypeError("query must be a string or a Query")
            self.query = query

    def _resolve(self) -> None:
        """Compute and store provider for nodes in `self.provider` dictionary."""
        for node, tag in self.query.captures(self.root_node):
            self._metadata.setdefault(node, set()).add(tag)

    @cached_property
    def reversed_mapping(self) -> dict[str, set[Node]]:
        """Return a mapping from tag to set of nodes that have that tag."""
        mapping = defaultdict(set)
        for node, tags in self.items():
            for tag in tags:
                mapping[tag].add(node)
        return mapping


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
    tag_metadata_provider = QueryTagMetadataProvider(tree.root_node, query=query, language=language)

    tag_metadata_provider.resolve()

    for k, v in tag_metadata_provider.items():
        print(k.text, v)

    for k, v in tag_metadata_provider.reversed_mapping.items():
        print(k, v)

    print(
        [
            class_name.text.decode()
            for class_name in tag_metadata_provider.reversed_mapping["class.name"]
        ]
    )  # ['QueryTagMetadataProvider']

    # Result:
    #   class.name QueryTagMetadataProvider
    #   class.superclass MetadataProvider[str]
    #   method.name __init__
    #   method.name resolve
