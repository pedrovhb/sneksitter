---
file: /home/pedro/Documents/chatgpt_export/Markdown/Build Networkx Graph with Cursor.md
heading_stack: <root> -> 9454ce70-1f14-454c-b6d4-dc8e17388ae1 -> System -> cdc1e4df-6ed9-4474-aa70-316fd1d37354 -> System -> aaa2cfbd-357a-4571-8976-96badef48d18 -> User -> 660d2f56-57b7-4db7-a86f-6e27fd55def8 -> Assistant -> aaa2f53f-301b-417c-b7ee-ff3a213ff44f -> User -> f88bf305-bb2b-49d3-8c39-93884f395670 -> Assistant
---
# Assistant

```python
import networkx as nx
from typing import Optional

# Simulating a traversal cursor with a basic nested dictionary as the underlying data structure
class TraversalCursor:
    def __init__(self, structure):
        self.structure = structure
        self.current_node = self.structure
        self.parent_stack = []  # To keep track of parent nodes
        self.sibling_iter = None  # To keep track of sibling nodes
    
    def go_to_first_child(self):
        if self.current_node.get('children'):
            self.parent_stack.append(self.current_node)
            self.current_node = self.current_node['children'][0]
            self.sibling_iter = iter(self.parent_stack[-1]['children'][1:])
            return True
        return False
    
    def go_to_next_sibling(self):
        try:
            self.current_node = next(self.sibling_iter)
            return True
        except StopIteration:
            return False
    
    def go_to_parent(self):
        if self.parent_stack:
            self.current_node = self.parent_stack.pop()
            return True
        return False

def build_tree(cursor: TraversalCursor, graph: nx.DiGraph, current_node: Optional[str] = None):
    if current_node is None:
        current_node = cursor.current_node['name']
    
    graph.add_node(current_node)
    
    if cursor.go_to_first_child():
        child = cursor.current_node['name']
        graph.add_node(child)
        graph.add_edge(current_node, child)
        build_tree(cursor, graph, child)
        
        while cursor.go_to_next_sibling():
            sibling = cursor.current_node['name']
            graph.add_node(sibling)
            graph.add_edge(current_node, sibling)
            build_tree(cursor, graph, sibling)
        
        cursor.go_to_parent()

# Example nested data structure
nested_data = {
    'name': 'root',
    'children': [
        {
            'name': 'child1',
            'children': [{'name': 'child1_1'}, {'name': 'child1_2'}]
        },
        {
            'name': 'child2',
            'children': [{'name': 'child2_1'}]
        }
    ]
}

# Initialize networkx graph and traversal cursor
G = nx.DiGraph()
cursor = TraversalCursor(nested_data)

# Start building the tree from the root node
build_tree(cursor, G)
G.nodes(), G.edges()
```

[child ⬇️](#d19608c1-cf76-442e-8eab-86807320e37d)

---

(main branch ⎇)
###### d19608c1-cf76-442e-8eab-86807320e37d
[parent ⬆️](#f88bf305-bb2b-49d3-8c39-93884f395670)
