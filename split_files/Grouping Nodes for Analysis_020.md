---
file: /home/pedro/Documents/chatgpt_export/Markdown/Grouping Nodes for Analysis.md
heading_stack: <root> -> 6db24c38-564f-43d4-b8c9-2fec4e4db353 -> System -> 2953287f-20e5-44fb-a584-4bfe4f961bbb -> System -> aaa23f50-fb72-4433-a7f7-075d9fdfe0f3 -> User -> b5e935e4-8ecf-4850-ac07-4d63ba79b17e -> Assistant -> ad08acfc-210e-4de6-8495-802cfd6644c0 -> Assistant -> 58d33044-a31f-4722-880d-41adf2e0d2e9 -> Tool -> 9a8e14e9-c1db-4b63-9860-668ca3c413e6 -> Assistant -> aaa20cb6-bdc0-41ca-b038-b00cfecd1334 -> User -> f356137c-fbe2-438d-87bb-9695d4112c6c -> Assistant -> d7ff89f8-b73e-4302-af13-473e623c04d9 -> Assistant
---
# Assistant

```python
from typing import Any, Dict, Optional

# The hierarchical structure to represent a node and its children
class HierarchicalNode:
    def __init__(self, node: Node):
        self.node = node
        self.children = []
    
    def __repr__(self, level=0):
        ret = "\t" * level + repr(self.node.type) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret

# Sort nodes by their start_point for ordered traversal
sorted_nodes = sorted(nodes, key=lambda x: x.start_point)

# Initialize the root of the tree
root = HierarchicalNode(Node("root", (0, 0), (0, 0)))

# Stack to keep track of parent nodes while traversing
stack: List[HierarchicalNode] = [root]

# Create the hierarchical tree
for node in sorted_nodes:
    current_parent = stack[-1]
    
    while stack:
        # Check if the current node belongs to the last parent in the stack
        if node.start_point >= current_parent.node.start_point and node.end_point <= current_parent.node.end_point:
            break
        else:
            stack.pop()
            current_parent = stack[-1] if stack else None
    
    # Create a HierarchicalNode and attach it to its parent
    new_node = HierarchicalNode(node)
    if current_parent:
        current_parent.children.append(new_node)
    
    # Push the new node to the stack
    stack.append(new_node)

# Print the tree structure
print(root)
```

[child ⬇️](#8df1bdf2-c2ab-45fe-8f3c-29e899a2be79)

---

(main branch ⎇)
###### 8df1bdf2-c2ab-45fe-8f3c-29e899a2be79
[parent ⬆️](#d7ff89f8-b73e-4302-af13-473e623c04d9)
