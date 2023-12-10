# Assistant

```python
# First, let's implement some utility functions for parsing the tree-sitter nodes.
# These functions will serve as building blocks for the class methods.

def extract_name(node: Node) -> bytes:
    """Extract the parameter name from the node."""
    # Assuming the identifier child node holds the name
    name_node = [child for child in node.children if child.type == 'identifier']
    if name_node:
        return name_node[0].text
    return b""

def extract_type(node: Node) -> bytes | None:
    """Extract the type annotation from the node."""
    # Assuming the type child node holds the type annotation
    type_node = [child for child in node.children if child.type == 'type']
    if type_node:
        return type_node[0].text
    return None

def extract_default(node: Node) -> bytes | None:
    """Extract the default value from the node."""
    # Assuming a child node holds the default value
    default_node = [child for child in node.children if child.type == 'default_parameter']
    if default_node:
        # Further drill down to get the actual default value
        actual_default_node = [child for child in default_node[0].children if child.type not in ['identifier', ':', '=']]
        if actual_default_node:
            return actual_default_node[0].text
    return None

# Testing utility functions with some mock nodes would be the next step, but since we're focusing on class methods,
# I'll proceed to implement those.
```

[child ⬇️](#c4ea14ab-f4b7-4ef7-9af4-fb93e8124ea1)

---

(main branch ⎇)
###### c4ea14ab-f4b7-4ef7-9af4-fb93e8124ea1
[parent ⬆️](#a86208ba-2773-4ff3-8870-4ba6f96373c2)
