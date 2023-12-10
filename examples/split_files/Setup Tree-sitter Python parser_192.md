# Assistant

```python
# Function to visualize named nodes as an indented tree with vertically aligned node text
def visualize_tree(node, indent=0, text=None, max_text_width=20, max_indent=4):
    """Recursively print the tree structure with vertically aligned node text."""
    if node.is_named:
        snippet = text[node.start_byte:node.end_byte][:max_text_width].decode("utf-8").replace("\n", "\\n")
        snippet = snippet.ljust(max_text_width, ' ')
        print("  " * indent + f"{node.type}: ".ljust(max_indent*2, ' ') + f"| {snippet}...")
    for child in node.children:
        visualize_tree(child, indent + 1, text, max_text_width, max_indent)

# Visualizing the tree structure of the parsed example code with vertically aligned node text
# and showing only named nodes
visualize_tree(root_node, text=bytes(example_code, "utf8"))
```

[child ⬇️](#2a2aee91-6855-43a6-b0ce-de79d7a9e280)

---

(other branch ⎇)
###### 2a2aee91-6855-43a6-b0ce-de79d7a9e280
[parent ⬆️](#c8da16fb-7ac4-4d4b-be9f-8d82bc9c4931)
