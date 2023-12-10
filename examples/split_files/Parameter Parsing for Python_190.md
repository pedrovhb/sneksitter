# Assistant

```python
# Refining extract_default to correctly identify and extract default value nodes
def extract_default(node: Node) -> Optional[bytes]:
    default_nodes = [child for child in node.children if child.type == 'default_parameter' or child.type == 'typed_default_parameter']
    if default_nodes:
        actual_default_nodes = [child for child in default_nodes[0].children if child.type not in ['identifier', ':', '=']]
        if actual_default_nodes:
            return actual_default_nodes[0].text
    elif node.type in ['default_parameter', 'typed_default_parameter']:
        # Directly process the node if it's already of the correct type
        actual_default_nodes = [child for child in node.children if child.type not in ['identifier', ':', '=']]
        if actual_default_nodes:
            return actual_default_nodes[0].text
    return None

# Rerun the test to verify the changes
parsed_parameters = Parameter.from_node_parameters(parameters_node)
parsed_parameters_data = [vars(param) for param in parsed_parameters]
parsed_parameters_data
```

[child ⬇️](#a29fff63-c9d7-4117-9712-dd0ff5508bcb)

---

(main branch ⎇)
###### a29fff63-c9d7-4117-9712-dd0ff5508bcb
[parent ⬆️](#70bec5e2-ec52-46f0-893b-59e56483fdff)
