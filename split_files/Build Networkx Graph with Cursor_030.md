---
file: /home/pedro/Documents/chatgpt_export/Markdown/Build Networkx Graph with Cursor.md
heading_stack: <root> -> 9454ce70-1f14-454c-b6d4-dc8e17388ae1 -> System -> cdc1e4df-6ed9-4474-aa70-316fd1d37354 -> System -> aaa2cfbd-357a-4571-8976-96badef48d18 -> User -> 660d2f56-57b7-4db7-a86f-6e27fd55def8 -> Assistant -> aaa2f53f-301b-417c-b7ee-ff3a213ff44f -> User -> f88bf305-bb2b-49d3-8c39-93884f395670 -> Assistant -> d19608c1-cf76-442e-8eab-86807320e37d -> Tool -> 6cb2143c-6833-483e-81c3-0d5c2c20c84a -> Assistant -> 51b0898f-7e88-4c13-b0c8-bbb7f8e79c51 -> Assistant -> fb7ae9bc-bb46-4c32-94d3-47dc0b2b5997 -> Tool -> e5bdaef0-5f8e-4822-829f-4a51aeb66212 -> Assistant -> ea55d543-5d28-4b1c-b826-048e5193a24e -> Assistant -> e11edf56-3f99-4581-a686-28205d3be656 -> Tool -> aaa2e899-d049-4567-ab73-9a0e30522e4a -> User -> e1eb96c2-6182-4f3d-9618-2090742a1ed5 -> Assistant
---
# Assistant

```python
# Fixing the infinite recursion issue by adding a unique ID to each node
# Also adding logic to skip already visited nodes

def build_tree_fixed(cursor: TraversalCursor, graph: nx.DiGraph, current_node: Optional[str] = None, visited: Optional[set] = None):
    if visited is None:
        visited = set()
        
    if current_node is None:
        current_node = cursor.current_node['name']
    
    if current_node in visited:
        return
    
    visited.add(current_node)
    graph.add_node(current_node)
    
    if cursor.go_to_first_child():
        child = cursor.current_node['name']
        graph.add_node(child)
        graph.add_edge(current_node, child)
        build_tree_fixed(cursor, graph, child, visited)
        
        while cursor.go_to_next_sibling():
            sibling = cursor.current_node['name']
            graph.add_node(sibling)
            graph.add_edge(current_node, sibling)
            build_tree_fixed(cursor, graph, sibling, visited)
        
        cursor.go_to_parent()

# Resetting the cursor and graph
cursor = TraversalCursor(nested_data)
G.clear()

# Adding more data to test
nested_data['children'].append(
    {
        'name': 'child3',
        'children': [{'name': 'child3_1'}, {'name': 'child3_2'}]
    }
)

# Run the build_tree_fixed function again
build_tree_fixed(cursor, G)
G.nodes(), G.edges()
```

[child ⬇️](#7ef60a9c-7eed-44d5-aa0f-3d90f7804b36)

---

(main branch ⎇)
###### 7ef60a9c-7eed-44d5-aa0f-3d90f7804b36
[parent ⬆️](#e1eb96c2-6182-4f3d-9618-2090742a1ed5)
