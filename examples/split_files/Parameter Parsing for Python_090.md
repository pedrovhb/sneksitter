# Assistant

```python
# Updating utility functions to target the correct sub-nodes for extraction

def extract_name(node: Node) -> bytes:
    if node.type in ['typed_parameter', 'default_parameter', 'typed_default_parameter']:
        identifier_nodes = [child for child in node.children if child.type == 'identifier']
        if identifier_nodes:
            return identifier_nodes[0].text

    elif node.type in ['list_splat_pattern', 'dictionary_splat_pattern']:
        return node.children[1].text if len(node.children) > 1 else b""

    return node.text if node.type == 'identifier' else b""


def extract_type(node: Node) -> Optional[bytes]:
    type_nodes = [child for child in node.children if child.type == 'type']
    if type_nodes:
        return type_nodes[0].text
    return None


def extract_default(node: Node) -> Optional[bytes]:
    default_nodes = [child for child in node.children if child.type == 'default_parameter']
    if default_nodes:
        actual_default_nodes = [child for child in default_nodes[0].children if child.type not in ['identifier', ':', '=']]
        if actual_default_nodes:
            return actual_default_nodes[0].text
    return None

# Rerun the test to verify the changes
parsed_parameters = Parameter.from_node_parameters(parameters_node)
parsed_parameters_data = [vars(param) for param in parsed_parameters]
parsed_parameters_data
```

[child ⬇️](#766dbfa5-c3fc-447d-8d7c-74b1c6a1dd27)

---

(main branch ⎇)
###### 766dbfa5-c3fc-447d-8d7c-74b1c6a1dd27
[parent ⬆️](#1e751c0e-3294-4bcf-a074-c3d7058c05e4)
