# Assistant

```python
# Function to find the maximum node type width in the tree
def find_max_type_width(node):
    max_width = 0
    if node.is_named:
        max_width = len(node.type)
    for child in node.children:
        child_max_width = find_max_type_width(child)
        max_width = max(max_width, child_max_width)
    return max_width

# Function to visualize named nodes as an indented tree with vertically aligned "|" characters
def visualize_tree(node, indent=0, text=None, max_type_width=0):
    """Recursively print the tree structure with vertically aligned '|' characters."""
    if node.is_named:
        snippet = text[node.start_byte:node.end_byte][:10].decode("utf-8").replace("\n", "\\n")
        snippet = snippet.ljust(10, ' ')
        node_type = node.type.ljust(max_type_width, ' ')
        print(f"{'  ' * indent}{node_type} | {snippet}...")
    for child in node.children:
        visualize_tree(child, indent + 1, text, max_type_width)

# Find the maximum node type width in the tree for alignment
max_type_width = find_max_type_width(root_node)

# Visualizing the tree structure of the parsed example code with vertically aligned '|' characters
# and showing only named nodes
visualize_tree(root_node, text=bytes(example_code, "utf8"), max_type_width=max_type_width)
```

[child ⬇️](#64babbc7-1f29-44bc-a795-34b4ad012737)

---

(other branch ⎇)
###### 64babbc7-1f29-44bc-a795-34b4ad012737
[parent ⬆️](#d27c9f99-339e-42a4-ade8-1c32c7cd950f)
