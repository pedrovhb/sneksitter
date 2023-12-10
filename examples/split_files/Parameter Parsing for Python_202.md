# Assistant

```python
# Refining extract_default to correctly identify and extract default value nodes for typed_default_parameter nodes
def extract_default(node: Node) -> Optional[bytes]:
    if node.type in ['default_parameter', 'typed_default_parameter']:
        # Directly process the node if it's already of the correct type
        actual_default_nodes = [child for child in node.children if child.type not in ['identifier', ':', '=', 'type']]
        if actual_default_nodes:
            return actual_default_nodes[0].text
    else:
        default_nodes = [child for child in node.children if child.type == 'default_parameter' or child.type == 'typed_default_parameter']
        if default_nodes:
            actual_default_nodes = [child for child in default_nodes[0].children if child.type not in ['identifier', ':', '=', 'type']]
            if actual_default_nodes:
                return actual_default_nodes[0].text
    return None

# Rerun the test to verify the changes
parsed_parameters = Parameter.from_node_parameters(parameters_node)
parsed_parameters_data = [vars(param) for param in parsed_parameters]
parsed_parameters_data
```

[child ⬇️](#4aaad935-c41e-4d28-8ed4-77010f07bbb4)

---

(main branch ⎇)
###### 4aaad935-c41e-4d28-8ed4-77010f07bbb4
[parent ⬆️](#07c939d7-b376-4d1a-8f20-828b513768cc)
