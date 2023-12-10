# Assistant

```python
# Function to visualize named nodes as an indented tree with vertically aligned "|" characters
def visualize_tree(node, indent=0, text=None, max_type_width=20):
    """Recursively print the tree structure with vertically aligned '|' characters."""
    if node.is_named:
        snippet = text[node.start_byte:node.end_byte][:10].decode("utf-8").replace("\n", "\\n")
        snippet = snippet.ljust(10, ' ')
        node_type = node.type.ljust(max_type_width, ' ')
        alignment_spaces = ' ' * (max_type_width * indent)
        print(f"{alignment_spaces}{node_type} | {snippet}...")
    for child in node.children:
        visualize_tree(child, indent + 1, text, max_type_width)

# Visualizing the tree structure of the parsed example code with vertically aligned '|' characters
# and showing only named nodes
visualize_tree(root_node, text=bytes(example_code, "utf8"))
```

[child ⬇️](#98708bce-736e-4a44-80ca-7298a57e574f)

---

(other branch ⎇)
###### 98708bce-736e-4a44-80ca-7298a57e574f
[parent ⬆️](#38cc4b94-780d-40a9-b7a2-e79296a41719)
