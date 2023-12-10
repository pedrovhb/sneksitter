---
file: /home/pedro/Documents/chatgpt_export/Markdown/Build Networkx Graph with Cursor.md
heading_stack: <root> -> 9454ce70-1f14-454c-b6d4-dc8e17388ae1 -> System -> cdc1e4df-6ed9-4474-aa70-316fd1d37354 -> System -> aaa2cfbd-357a-4571-8976-96badef48d18 -> User -> 660d2f56-57b7-4db7-a86f-6e27fd55def8 -> Assistant -> aaa2f53f-301b-417c-b7ee-ff3a213ff44f -> User -> f88bf305-bb2b-49d3-8c39-93884f395670 -> Assistant -> d19608c1-cf76-442e-8eab-86807320e37d -> Tool -> 6cb2143c-6833-483e-81c3-0d5c2c20c84a -> Assistant -> 51b0898f-7e88-4c13-b0c8-bbb7f8e79c51 -> Assistant -> fb7ae9bc-bb46-4c32-94d3-47dc0b2b5997 -> Tool -> e5bdaef0-5f8e-4822-829f-4a51aeb66212 -> Assistant -> ea55d543-5d28-4b1c-b826-048e5193a24e -> Assistant -> e11edf56-3f99-4581-a686-28205d3be656 -> Tool -> aaa2e899-d049-4567-ab73-9a0e30522e4a -> User -> e1eb96c2-6182-4f3d-9618-2090742a1ed5 -> Assistant -> 7ef60a9c-7eed-44d5-aa0f-3d90f7804b36 -> Tool -> 15b380ed-29fa-4b8e-91d1-18b9badf7375 -> Assistant -> 63125128-93cd-4245-85ed-4eb855b0d5d9 -> Tool -> 28322e40-fbc3-4697-b889-7bfc1cbd6646 -> Assistant -> aaa255bd-d556-491e-8170-56c47b45a097 -> User -> 320c67ff-0dfb-4c38-b56e-34468a3d105e -> Assistant -> afd3d6ea-3a9c-438a-9953-a86948012f11 -> Tool -> 607cc351-d587-4de9-8b81-48f78baa6808 -> Assistant -> 32520129-56ad-4b4c-aa5c-70a535c8d810 -> Tool -> 12bc79e2-6ccb-4f09-9cb2-4fa39aae46de -> Assistant -> 22aec5e1-4da7-49b8-8f82-256fcf4a7ac6 -> Assistant -> faa4b10f-1700-4da1-9d1a-92c8719a53cc -> Tool -> e10976ff-6dfc-4df1-bd25-e3e4eec6241a -> Assistant -> e0c0ab3e-0cba-4dcf-9ec0-3d480613825d -> Tool -> 1d103013-56f3-4295-9547-11bef7cac8b9 -> Assistant -> aaa262dc-9989-484c-b5ab-bdbc4e761f45 -> User -> cdbb92c6-377f-421a-b673-0bdfea10504f -> Assistant -> f76c5d36-6a88-44a7-b955-65eae7dbef08 -> Tool -> 9bd2af72-9be2-483d-b788-68d422a1f433 -> Assistant -> dcfc9cf8-8c16-419a-a476-65daf2156b3c -> Assistant -> 8c1d94ee-4c46-4273-a873-c859316d0ad4 -> Tool -> a9b8b5ac-12ca-451a-be14-5d5aa1e6a6a9 -> Assistant -> aaa27046-aa7d-42b1-bda5-49edff9ef608 -> User -> d3ca0b62-1b60-4edd-820b-0376f55b4896 -> Assistant
---
# Assistant

```python
# A more complex piece of Python code for parsing
complex_code = '''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
'''

# Parse the complex code to get an AST
tree = parser.parse(bytes(complex_code, "utf8"))

# Initialize a new cursor for tree traversal
cursor = tree.walk()

# Initialize a new NetworkX graph
G_complex = nx.DiGraph()

def build_complex_tree_sitter_graph(cursor, graph, current_node=None):
    if current_node is None:
        current_node = cursor.node.type
    
    # Add only named nodes to the graph
    if not cursor.node.is_named:
        return
    
    graph.add_node(current_node)
    
    if cursor.goto_first_child():
        child = cursor.node.type
        if cursor.node.is_named:
            graph.add_node(child)
            graph.add_edge(current_node, child)
            build_complex_tree_sitter_graph(cursor, graph, child)
        
        while cursor.goto_next_sibling():
            sibling = cursor.node.type
            if cursor.node.is_named:
                graph.add_node(sibling)
                graph.add_edge(current_node, sibling)
                build_complex_tree_sitter_graph(cursor, graph, sibling)
        
        cursor.goto_parent()

# Build the new graph
cursor.reset(tree.root_node)
G_complex.clear()
build_complex_tree_sitter_graph(cursor, G_complex)

# Pretty print the new tree using Graphviz with rounded rectangle nodes
pydot_graph_complex = to_pydot(G_complex)
pydot_graph_complex.set('rankdir', 'TB')
pydot_graph_complex.set('concentrate', True)
pydot_graph_complex.set_node_defaults(shape='box', style='rounded')

# Generate a visualization
png_image_complex = pydot_graph_complex.create_png(prog='dot')

# Display the image
image_complex = Image.open(BytesIO(png_image_complex))
display(image_complex)
```

[child ⬇️](#e1a86ecb-1e50-4d6b-9ea2-06390d9446e9)

---

(main branch ⎇)
###### e1a86ecb-1e50-4d6b-9ea2-06390d9446e9
[parent ⬆️](#d3ca0b62-1b60-4edd-820b-0376f55b4896)
