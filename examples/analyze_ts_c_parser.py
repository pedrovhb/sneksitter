from pathlib import Path

from tree_sitter import Node
from tree_sitter_languages import get_parser

from sneksitter.visitor import TSVisitor, TraversalAction


class AnalyzeTSParser(TSVisitor):
    # def visit_default(self, node: Node) -> None:
    #     if node.is_named:
    #         node_text = node.text[:50].decode().replace("\n", "\\n")
    #         print(str.ljust(" " * self.crt_depth + node.type, 40), f" | {node_text}")

    # def visit_identifier(self, node: Node):
    #     print(f"identifier {node.text.decode()!r}")
    #     if node.text.decode() == "sym_identifier":
    #         print("a")

    def __init__(self, root_node: Node) -> None:
        super().__init__(root_node)
        self.ts_symbol_map = {}
        self.ts_symbol_identifiers = {}

    def visit_init_declarator(self, node: Node) -> None:
        # [init_declarator.field_name_for_child(i) for i in range(init_declarator.child_count)]
        print(
            node.child_by_field_name("declarator"),
            node.child_by_field_name("declarator").text
            if node.child_by_field_name("declarator") is not None
            else None,
        )
        if node.child_by_field_name("declarator").text == b"b'* const ts_symbol_names[]'":
            print("a")

    def visit_array_declarator(self, node: Node) -> None:
        if node.text == b"ts_symbol_names[]":
            declaration = node.parent.parent.parent
            initialization_pairs = declaration.named_children[-1].named_children[-1].named_children
            for pair in initialization_pairs:
                name, value = pair.named_children
                print(name.text, value.text)
                self.ts_symbol_map[name] = value

    def visit_type_identifier(self, node: Node) -> None:
        print(f"type_identifier {node.text.decode()!r}")

        if node.text == b"ts_symbol_identifiers":
            enumerator_list = node.next_sibling
            assert enumerator_list.type == "enumerator_list"
            for enumerator in enumerator_list.children:
                if enumerator.type != "enumerator":
                    continue
                item_name, item_number = enumerator.children[0], enumerator.children[2]
                assert item_name.type == "identifier"
                assert item_number.type == "number_literal"
                print(item_name.text, item_number.text)
                self.ts_symbol_identifiers[item_name] = item_number

        elif node.text == b"TSSymbol":
            print("b")
        elif node.text == b"TSSymbolMetadata":
            print("cb")
        elif node.text == b"ts_field_identifiers":
            print("db")
        else:
            return TraversalAction.SkipSubtree


if __name__ == "__main__":
    parser = get_parser("c")
    tree = parser.parse(
        Path(
            "/home/pedro/projs/sneksitter/get_parsers/tree-sitter-python/src/parser.c"
        ).read_bytes()
    )
    visitor = AnalyzeTSParser(tree.root_node)
    visitor.traverse()

    print(visitor.ts_symbol_map)
    print(visitor.ts_symbol_identifiers)

    sym_ids = {
        k.text.decode(): int(v.text.decode()) for k, v in visitor.ts_symbol_identifiers.items()
    }

    sym_map = {}
    for k, v in visitor.ts_symbol_map.items():
        symbols = tuple(n.text.decode() for n in k.children if n.type == "identifier")
        sym_map[symbols] = v.text.decode()

    print(sym_ids, sym_map)
