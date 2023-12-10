# Assistant

```python
# Refining the extract_name function using named_children for more accurate attribute extraction
def extract_name(node: Node) -> bytes:
    if node.type in ['typed_parameter', 'default_parameter', 'typed_default_parameter']:
        identifier_nodes = [child for child in node.named_children if child.type == 'identifier']
        if identifier_nodes:
            return identifier_nodes[0].text

    elif node.type == 'list_splat_pattern' or node.type == 'dictionary_splat_pattern':
        identifier_nodes = [child for child in node.named_children if child.type == 'identifier']
        if identifier_nodes:
            return identifier_nodes[0].text

    return node.text if node.type == 'identifier' else b""

# Rerun the test to verify the changes
parsed_parameters = Parameter.from_node_parameters(parameters_node)
parsed_parameters_data = [vars(param) for param in parsed_parameters]
parsed_parameters_data
```

[child ⬇️](#81c209aa-7e75-4b56-b1a1-a33d7e298228)

---

(main branch ⎇)
###### 81c209aa-7e75-4b56-b1a1-a33d7e298228
[parent ⬆️](#7d4f45c7-c2a0-4488-9b24-dbc39793e09f)
