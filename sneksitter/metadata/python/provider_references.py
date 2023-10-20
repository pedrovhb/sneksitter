from tree_sitter import Tree, Node

from sneksitter.metadata.base_visitor_provider import VisitorBasedMetadataProvider, _T

try:
    import jedi
except ImportError as e:
    raise ImportError(
        "The PythonReferenceMetadataProvider requires the `jedi` package to be installed"
    ) from e

# Demonstrating usage of Jedi to get references to a target_node
# https://jedi.readthedocs.io/en/latest/docs/api.html#jedi.api.Script.references


class PythonReferenceMetadataProvider(VisitorBasedMetadataProvider):
    def metadata_for_node(self, node_id: int) -> _T:
        return self.metadata.get(node_id)


if __name__ == "__main__":
    from tree_sitter_languages import get_parser
    from pathlib import Path

    parser = get_parser("python")
    tree = parser.parse(Path(__file__).read_bytes())
    script = jedi.Script(tree.text.decode(), path=Path(__file__).absolute())
    print(script)
