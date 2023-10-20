from tree_sitter import Node

from sneksitter.transformer import BaseTransformer


class ParamTransformer(BaseTransformer):
    def visit_parameters(self, node: Node) -> bool:
        for child in node.named_children:
            self.add_replacement(child, child.text.upper())
        return False

    def visit_call(self, node: Node) -> bool:
        called = node.named_children[0]
        self.add_replacement(called, called.text.upper())
        args = node.named_children[1]
        for arg in args.named_children:
            self.add_replacement(
                arg, arg.text[::-1]
            )  # this makes some weird stuff happen
        return False

    def visit_block(self, node: Node) -> bool:
        """*meta*"""
        if node.parent.type == "function_definition":
            if (
                node.named_children[0].type == "expression_statement"
                and node.named_children[0].named_children[0].type == "string"
            ):
                child = node.named_children[0].named_children[0]
                self.add_replacement(child, child.text.upper())
                print(f"Hey, I found a docstring! {child.text}")
        return True


if __name__ == "__main__":
    from pathlib import Path
    from tree_sitter_languages import get_parser

    parser = get_parser("python")
    source = Path(__file__).read_bytes()
    tree = parser.parse(source)

    transformed_tree = ParamTransformer(parser).transform(tree)
    print(transformed_tree.root_node.text.decode())
