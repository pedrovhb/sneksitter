# Assistant

```python
# Debugging: Inserting print statements in the extract_default function to understand its behavior
def extract_default(node: Node) -> Optional[bytes]:
    print(f"Debug: extract_default called for node type {node.type}")
    default_nodes = [child for child in node.children if child.type == 'default_parameter' or child.type == 'typed_default_parameter']
    if default_nodes:
        print(f"Debug: Found default node of type {default_nodes[0].type}")
        actual_default_nodes = [child for child in default_nodes[0].children if child.type not in ['identifier', ':', '=']]
        if actual_default_nodes:
            print(f"Debug: Found actual default node of type {actual_default_nodes[0].type}")
            return actual_default_nodes[0].text
    return None

# Debugging: Investigating how the extract_default function processes the default_parameter node for y=1
extract_default(default_param_node)
```

[child ⬇️](#21d03324-9832-4b24-8d56-14fd357885ab)

---

(main branch ⎇)
###### 21d03324-9832-4b24-8d56-14fd357885ab
[parent ⬆️](#eaa8f628-80f2-442b-9c25-5a3780d34537)
