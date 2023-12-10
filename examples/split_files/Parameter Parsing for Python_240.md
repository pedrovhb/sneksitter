# Assistant

```python
# Adjusting extract_default to use len(node.children) instead of a non-existent 'has_children' attribute
def extract_default(node: Node) -> Optional[bytes]:
    if node.type in ['default_parameter', 'typed_default_parameter']:
        actual_default_nodes = [child for child in node.children if child.type not in ['identifier', ':', '=', 'type'] and len(child.children) == 0]
        if actual_default_nodes:
            return actual_default_nodes[0].text
    else:
        default_nodes = [child for child in node.children if child.type == 'default_parameter' or child.type == 'typed_default_parameter']
        if default_nodes:
            actual_default_nodes = [child for child in default_nodes[0].children if child.type not in ['identifier', ':', '=', 'type'] and len(child.children) == 0]
            if actual_default_nodes:
                return actual_default_nodes[0].text
    return None

# Rerun the test to verify the changes
parsed_parameters = Parameter.from_node_parameters(parameters_node)
parsed_parameters_data = [vars(param) for param in parsed_parameters]
parsed_parameters_data
```

[child ⬇️](#73095664-88d1-4cc4-a45d-b8de18ed8505)

---

(main branch ⎇)
###### 73095664-88d1-4cc4-a45d-b8de18ed8505
[parent ⬆️](#a17e2ae2-8e1e-4bf8-9b6b-65cb61466221)
