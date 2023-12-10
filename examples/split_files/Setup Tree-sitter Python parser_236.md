# Assistant

```python
# Revised function to visualize named nodes as an indented tree with vertically aligned "|" characters
def visualize_tree(node, prefix='', text=None, max_type_width=0):
    """Recursively print the tree structure with vertically aligned '|' characters."""
    if node.is_named:
        snippet = text[node.start_byte:node.end_byte][:10].decode("utf-8").replace("\n", "\\n")
        node_type = node.type.ljust(max_type_width, ' ')
        print(f"{prefix}{node_type} | {snippet}...")
        new_prefix = ' ' * (len(prefix) + max_type_width + 3)  # 3 accounts for " | "
        for child in node.children:
            visualize_tree(child, prefix=new_prefix, text=text, max_type_width=max_type_width)

# Visualizing the tree structure of the parsed example code with vertically aligned '|' characters
# and showing only named nodes
visualize_tree(root_node, text=bytes(example_code, "utf8"), max_type_width=max_type_width)
```

[child ⬇️](#b8b0939f-82bf-4bc6-a5af-ae7a71c28ee6)

---

(other branch ⎇)
###### b8b0939f-82bf-4bc6-a5af-ae7a71c28ee6
[parent ⬆️](#427dd136-9105-496c-bce8-3fc6b13cb888)
