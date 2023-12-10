# Assistant

```python
# Function to visualize named nodes as an indented tree with vertically aligned "|" characters
def visualize_tree(node, indent=0, text=None, max_type_width=25):
    """Recursively print the tree structure with vertically aligned '|' characters."""
    if node.is_named:
        snippet = text[node.start_byte:node.end_byte][:10].decode("utf-8").replace("\n", "\\n")
        snippet = snippet.ljust(10, ' ')
        node_type = node.type.ljust(max_type_width, ' ')
        print("  " * indent + f"{node_type} | {snippet}...")
    for child in node.children:
        visualize_tree(child, indent + 1, text, max_type_width)

# Visualizing the tree structure of the parsed example code with vertically aligned '|' characters
# and showing only named nodes
visualize_tree(root_node, text=bytes(example_code, "utf8"))
```

[child ⬇️](#6b4f3530-129a-480d-8afe-b627dc88ec62)

---

(other branch ⎇)
###### 6b4f3530-129a-480d-8afe-b627dc88ec62
[parent ⬆️](#775e1aed-454b-4cf1-a708-b3dc00593d7f)
