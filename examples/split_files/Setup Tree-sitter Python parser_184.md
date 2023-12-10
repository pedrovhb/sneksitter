# Assistant

```python
# Function to visualize nodes as an indented tree with vertically aligned node text
def visualize_tree(node, indent=0, text=None, max_text_width=12):
    """Recursively print the tree structure with vertically aligned node text."""
    snippet = text[node.start_byte:node.end_byte][:max_text_width].decode("utf-8").replace("\n", "\\n")
    snippet = snippet.ljust(max_text_width)
    print("  " * indent + f"{node.type}: {snippet}")
    for child in node.children:
        visualize_tree(child, indent + 1, text, max_text_width)

# Visualizing the tree structure of the parsed example code with vertically aligned node text
visualize_tree(root_node, text=bytes(example_code, "utf8"))
```

[child ⬇️](#8c150b10-f9d6-46e3-897d-a4781038bcb1)

---

(other branch ⎇)
###### 8c150b10-f9d6-46e3-897d-a4781038bcb1
[parent ⬆️](#8cbf2766-7ffd-4f0b-a4a7-07eb847057a2)
