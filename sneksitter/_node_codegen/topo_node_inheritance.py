from typing import List, Dict, Set, NamedTuple, Iterator, Tuple, Union
from collections import defaultdict
import json


# NamedTuple to use as a key for the inheritance tree
class TypeKey(NamedTuple):
    type: str
    named: bool


# Type aliases for better readability
TypeRelationships = Dict[str, List[str]]
InheritanceTree = Dict[TypeKey, Dict[str, List[TypeKey]]]


def read_json_file(file_path: str) -> List[Dict]:
    with open(file_path, "r") as f:
        return json.load(f)


def extract_type_relationships(data: List[Dict]) -> TypeRelationships:
    relationships = {}
    for entry in data:
        type_name = entry.get("type")
        subtypes = entry.get("subtypes", [])
        if subtypes:
            relationships[type_name] = [subtype["type"] for subtype in subtypes]
    return relationships


def find_most_specific_type(
    subtype: str, type_relationships: TypeRelationships, visited: Set[str]
) -> Union[str, None]:
    most_specific_type = None
    for supertype, subtypes in type_relationships.items():
        if subtype in subtypes:
            visited.add(supertype)
            next_level = find_most_specific_type(supertype, type_relationships, visited)
            most_specific_type = next_level if next_level else supertype
    return most_specific_type


def build_inheritance_tree(
    data: List[Dict], type_relationships: TypeRelationships
) -> InheritanceTree:
    tree = defaultdict(lambda: {"bases": [], "subtypes": []})
    for entry in data:
        type_name = entry.get("type")
        named = entry.get("named", False)
        key = TypeKey(type_name, named)
        subtypes = entry.get("subtypes", [])
        for subtype_entry in subtypes:
            subtype_key = TypeKey(subtype_entry["type"], subtype_entry["named"])
            most_specific_type = find_most_specific_type(
                subtype_entry["type"], type_relationships, set()
            )
            if most_specific_type is None or most_specific_type == type_name:
                tree[key]["subtypes"].append(subtype_key)
        most_specific_type = find_most_specific_type(type_name, type_relationships, set())
        if most_specific_type:
            base_key = TypeKey(most_specific_type, named)
            tree[key]["bases"].append(base_key)
    return tree


def topological_sort_dfs(
    node: TypeKey, visited: Set[TypeKey], stack: List[TypeKey], tree: InheritanceTree
):
    visited.add(node)
    for subtype in tree.get(node, {}).get("subtypes", []):
        if subtype not in visited:
            topological_sort_dfs(subtype, visited, stack, tree)
    stack.append(node)


def topological_sort_node_type_iterator(
    tree: InheritanceTree,
) -> Iterator[Tuple[TypeKey, Dict[str, List[TypeKey]]]]:
    visited = set()
    stack = []
    for node in tree.keys():
        if node not in visited:
            topological_sort_dfs(node, visited, stack, tree)
    sorted_order = stack[::-1]
    for node in sorted_order:
        yield (node, tree.get(node, {"bases": [], "subtypes": []}))


if __name__ == "__main__":
    # Example usage
    file_path = "/home/pedro/scratch/tree-sitter-repos/tree-sitter-python/src/node-types.json"
    data = read_json_file(file_path)
    type_relationships = extract_type_relationships(data)
    inheritance_tree = build_inheritance_tree(data, type_relationships)

    topo_iterator = topological_sort_node_type_iterator(inheritance_tree)
    for item in topo_iterator:
        print(item)
