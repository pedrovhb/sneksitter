import json

from tree_sitter import Node, Tree

from sneksitter.visitor import BaseVisitor


class DictionaryBuilderVisitor(BaseVisitor):
    """Build a dictionary from a tree."""

    def __init__(self) -> None:
        super().__init__()
        self._dict = {}
        self._stack = []

    def visit_module(self, node: Node) -> None:
        self._dict = {"type": "module", "children": [], "text": node.text.decode()}
        self._stack.append(self._dict)

    def visit(self, node: Node) -> None:
        self._stack.append(
            {"type": node.type, "children": [], "text": node.text.decode()}
        )

    def leave(self, node: Node) -> None:
        self._stack[-2]["children"].append(self._stack.pop())

    def leave_module(self, node: Node) -> None:
        self._stack.pop()

    def get_dict(self) -> dict:
        return self._dict

    @classmethod
    def tree_to_dict(cls, tree: Tree) -> dict:
        """Class method to traverse the tree and call the visitor's methods."""
        visitor = cls()
        visitor.traverse(tree)
        return visitor.get_dict()

    @classmethod
    def tree_to_json(cls, tree: Tree) -> str:
        """Class method to traverse the tree and call the visitor's methods."""

        return json.dumps(cls.tree_to_dict(tree), indent=4)


if __name__ == "__main__":
    from pathlib import Path
    from tree_sitter_languages import get_parser

    parser = get_parser("python")
    source = Path(__file__).read_bytes()
    tree = parser.parse(source)

    transformed_tree = DictionaryBuilderVisitor.tree_to_json(tree)
    Path("/tmp/example_visitor_dict.json").write_text(transformed_tree)
    print(transformed_tree)
