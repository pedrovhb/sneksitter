---
file: /home/pedro/Documents/chatgpt_export/Markdown/Grouping Nodes for Analysis.md
heading_stack: <root> -> 6db24c38-564f-43d4-b8c9-2fec4e4db353 -> System -> 2953287f-20e5-44fb-a584-4bfe4f961bbb -> System -> aaa23f50-fb72-4433-a7f7-075d9fdfe0f3 -> User -> b5e935e4-8ecf-4850-ac07-4d63ba79b17e -> Assistant -> ad08acfc-210e-4de6-8495-802cfd6644c0 -> Assistant -> 58d33044-a31f-4722-880d-41adf2e0d2e9 -> Tool -> 9a8e14e9-c1db-4b63-9860-668ca3c413e6 -> Assistant -> aaa20cb6-bdc0-41ca-b038-b00cfecd1334 -> User -> f356137c-fbe2-438d-87bb-9695d4112c6c -> Assistant -> d7ff89f8-b73e-4302-af13-473e623c04d9 -> Assistant -> 8df1bdf2-c2ab-45fe-8f3c-29e899a2be79 -> Tool -> f9188ff9-69b8-4c8b-9f72-46698e2fed91 -> Assistant -> a486650a-5d1b-44dd-a66a-ecbb8f23cf42 -> Assistant
---
# Assistant

```python
# Revised dummy data to simulate a more realistic hierarchical relationship.
nodes = [
    Node("function_definition", (4, 0), (31, 58)),
    Node("identifier", (4, 4), (4, 20)),
    Node("parameters", (4, 20), (4, 66)),
    Node("identifier", (4, 21), (4, 29)),
    Node("type", (4, 31), (4, 34)),
    Node("block", (5, 4), (31, 58)),
    Node("string", (5, 4), (8, 7)),
    Node("function_definition", (35, 0), (38, 46)),
    Node("identifier", (35, 4), (35, 9)),
    Node("parameters", (35, 9), (35, 73)),
    Node("identifier", (35, 10), (35, 16)),
    Node("type", (35, 18), (35, 21)),
    Node("block", (36, 4), (38, 46))
]

# Re-run the tree creation logic
sorted_nodes = sorted(nodes, key=lambda x: x.start_point)

root = HierarchicalNode(Node("root", (0, 0), (100, 100)))  # Set the root node to cover all possible child nodes
stack = [root]

for node in sorted_nodes:
    current_parent = stack[-1]
    
    while stack:
        if node.start_point >= current_parent.node.start_point and node.end_point <= current_parent.node.end_point:
            break
        else:
            stack.pop()
            current_parent = stack[-1] if stack else None

    new_node = HierarchicalNode(node)
    if current_parent:
        current_parent.children.append(new_node)
    
    stack.append(new_node)

# Print the tree structure
print(root)
```

[child ⬇️](#7fdad3d6-7b6d-4d3c-8450-6f8525f549d8)

---

(main branch ⎇)
###### 7fdad3d6-7b6d-4d3c-8450-6f8525f549d8
[parent ⬆️](#a486650a-5d1b-44dd-a66a-ecbb8f23cf42)
