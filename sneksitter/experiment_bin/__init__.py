import tree_sitter_languages
from tree_sitter import Parser


def get_parser(language):
    parser = Parser()
    parser.set_language(tree_sitter_languages.get_language(language))
    return parser


def parse_code(parser, code):
    return parser.parse(bytes(code, "utf8"))


def get_all_nodes(tree):
    cursor = tree.walk()
    nodes = [cursor.node]
    visited = set()
    while cursor.goto_first_child() or cursor.goto_next_sibling():
        current_node = cursor.node
        if current_node.id in visited:
            cursor.goto_parent()
            continue
        visited.add(current_node.id)
        nodes.append(current_node)
    return nodes


def compare_nodes_for_diff(node1, node2, code1, code2):
    if node1 and node2 and (node1.type, node1.text) != (node2.type, node2.text):
        return {
            "from_code1": code1[node1.start_byte : node1.end_byte],
            "from_code2": code2[node2.start_byte : node2.end_byte],
            "node1": node1,
            "node2": node2,
        }
    elif bool(node1) != bool(node2):
        return {
            "from_code1": code1[node1.start_byte : node1.end_byte] if node1 else "",
            "from_code2": code2[node2.start_byte : node2.end_byte] if node2 else "",
            "node1": node1,
            "node2": node2,
        }
    return None


def find_direct_replacements(original_nodes, modified_nodes, code1, code2):
    replacements = []
    for original_node, modified_node in zip(original_nodes, modified_nodes):
        diff = compare_nodes_for_diff(original_node, modified_node, code1, code2)
        if diff:
            replacements.append(diff)
    return replacements


# Example usage of the module
if __name__ == "__main__":
    parser = get_parser("python")
    original_code = "def example(arg1, arg2):\\n    return arg1 + arg2"
    modified_code = "def example(arg1, *arg2):\\n    return sum(arg2)"

    original_tree = parse_code(parser, original_code)
    modified_tree = parse_code(parser, modified_code)

    original_nodes = get_all_nodes(original_tree)
    modified_nodes = get_all_nodes(modified_tree)

    replacements = find_direct_replacements(
        original_nodes, modified_nodes, original_code, modified_code
    )
    for replacement in replacements:
        print(replacement)
        # {'from_code1': 'def example(arg1, arg2):\\n    return arg1 + arg2', 'from_code2': 'def example(arg1, *arg2):\\n    return sum(arg2)', 'node1': <Node type=module, start_point=(0, 0), end_point=(0, 48)>, 'node2': <Node type=module, start_point=(0, 0), end_point=(0, 47)>}
        # {'from_code1': 'def example(arg1, arg2):\\n    return arg1 + arg2', 'from_code2': 'def example(arg1, *arg2):\\n    return sum(arg2)', 'node1': <Node type=function_definition, start_point=(0, 0), end_point=(0, 48)>, 'node2': <Node type=function_definition, start_point=(0, 0), end_point=(0, 47)>}
        # {'from_code1': '(arg1, arg2)', 'from_code2': '(arg1, *arg2)', 'node1': <Node type=parameters, start_point=(0, 11), end_point=(0, 23)>, 'node2': <Node type=parameters, start_point=(0, 11), end_point=(0, 24)>}
        # {'from_code1': 'arg2', 'from_code2': '*arg2', 'node1': <Node type=identifier, start_point=(0, 18), end_point=(0, 22)>, 'node2': <Node type=list_splat_pattern, start_point=(0, 18), end_point=(0, 23)>}
        # {'from_code1': ')', 'from_code2': '*', 'node1': <Node type=")", start_point=(0, 22), end_point=(0, 23)>, 'node2': <Node type="*", start_point=(0, 18), end_point=(0, 19)>}
