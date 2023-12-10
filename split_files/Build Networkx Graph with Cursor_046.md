---
file: /home/pedro/Documents/chatgpt_export/Markdown/Build Networkx Graph with Cursor.md
heading_stack: <root> -> 9454ce70-1f14-454c-b6d4-dc8e17388ae1 -> System -> cdc1e4df-6ed9-4474-aa70-316fd1d37354 -> System -> aaa2cfbd-357a-4571-8976-96badef48d18 -> User -> 660d2f56-57b7-4db7-a86f-6e27fd55def8 -> Assistant -> aaa2f53f-301b-417c-b7ee-ff3a213ff44f -> User -> f88bf305-bb2b-49d3-8c39-93884f395670 -> Assistant -> d19608c1-cf76-442e-8eab-86807320e37d -> Tool -> 6cb2143c-6833-483e-81c3-0d5c2c20c84a -> Assistant -> 51b0898f-7e88-4c13-b0c8-bbb7f8e79c51 -> Assistant -> fb7ae9bc-bb46-4c32-94d3-47dc0b2b5997 -> Tool -> e5bdaef0-5f8e-4822-829f-4a51aeb66212 -> Assistant -> ea55d543-5d28-4b1c-b826-048e5193a24e -> Assistant -> e11edf56-3f99-4581-a686-28205d3be656 -> Tool -> aaa2e899-d049-4567-ab73-9a0e30522e4a -> User -> e1eb96c2-6182-4f3d-9618-2090742a1ed5 -> Assistant -> 7ef60a9c-7eed-44d5-aa0f-3d90f7804b36 -> Tool -> 15b380ed-29fa-4b8e-91d1-18b9badf7375 -> Assistant -> 63125128-93cd-4245-85ed-4eb855b0d5d9 -> Tool -> 28322e40-fbc3-4697-b889-7bfc1cbd6646 -> Assistant -> aaa255bd-d556-491e-8170-56c47b45a097 -> User -> 320c67ff-0dfb-4c38-b56e-34468a3d105e -> Assistant -> afd3d6ea-3a9c-438a-9953-a86948012f11 -> Tool -> 607cc351-d587-4de9-8b81-48f78baa6808 -> Assistant
---
# Assistant

```python
# Now, let's use tree_sitter_languages to get a tree-sitter parser for Python
import tree_sitter_languages

# Get a Python parser
parser = tree_sitter_languages.get_parser("python")

# Sample Python code for parsing
sample_code = '''
def hello_world():
    print("Hello, world!")
'''

# Parse the sample code to get an Abstract Syntax Tree (AST)
tree = parser.parse(bytes(sample_code, "utf8"))

# Initialize a cursor for tree traversal
cursor = tree.walk()

# Initialize networkx graph
G_tree_sitter = nx.DiGraph()

def build_tree_sitter_graph(cursor, graph, current_node=None):
    if current_node is None:
        current_node = cursor.node_type
    
    graph.add_node(current_node)
    
    if cursor.goto_first_child():
        child = cursor.node_type
        graph.add_node(child)
        graph.add_edge(current_node, child)
        build_tree_sitter_graph(cursor, graph, child)
        
        while cursor.goto_next_sibling():
            sibling = cursor.node_type
            graph.add_node(sibling)
            graph.add_edge(current_node, sibling)
            build_tree_sitter_graph(cursor, graph, sibling)
        
        cursor.goto_parent()

# Build the graph
build_tree_sitter_graph(cursor, G_tree_sitter)

# Print nodes and edges
G_tree_sitter.nodes(), G_tree_sitter.edges()
```

[child ⬇️](#32520129-56ad-4b4c-aa5c-70a535c8d810)

---

(main branch ⎇)
###### 32520129-56ad-4b4c-aa5c-70a535c8d810
[parent ⬆️](#607cc351-d587-4de9-8b81-48f78baa6808)
