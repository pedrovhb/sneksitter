---
file: /home/pedro/Documents/chatgpt_export/Markdown/Build Networkx Graph with Cursor.md
heading_stack: <root> -> 9454ce70-1f14-454c-b6d4-dc8e17388ae1 -> System -> cdc1e4df-6ed9-4474-aa70-316fd1d37354 -> System -> aaa2cfbd-357a-4571-8976-96badef48d18 -> User -> 660d2f56-57b7-4db7-a86f-6e27fd55def8 -> Assistant -> aaa2f53f-301b-417c-b7ee-ff3a213ff44f -> User -> f88bf305-bb2b-49d3-8c39-93884f395670 -> Assistant -> d19608c1-cf76-442e-8eab-86807320e37d -> Tool -> 6cb2143c-6833-483e-81c3-0d5c2c20c84a -> Assistant -> 51b0898f-7e88-4c13-b0c8-bbb7f8e79c51 -> Assistant -> fb7ae9bc-bb46-4c32-94d3-47dc0b2b5997 -> Tool -> e5bdaef0-5f8e-4822-829f-4a51aeb66212 -> Assistant -> ea55d543-5d28-4b1c-b826-048e5193a24e -> Assistant -> e11edf56-3f99-4581-a686-28205d3be656 -> Tool -> aaa2e899-d049-4567-ab73-9a0e30522e4a -> User -> e1eb96c2-6182-4f3d-9618-2090742a1ed5 -> Assistant -> 7ef60a9c-7eed-44d5-aa0f-3d90f7804b36 -> Tool -> 15b380ed-29fa-4b8e-91d1-18b9badf7375 -> Assistant
---
# Assistant

```python
# Pretty-printing the graph elements as a tree
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt

def pretty_print_tree(graph: nx.DiGraph, root: str):
    pos = graphviz_layout(graph, prog="dot")
    labels = {node: node for node in graph.nodes()}
    
    plt.figure(figsize=(10, 10))
    nx.draw(graph, pos, labels=labels, with_labels=True, node_color="lightblue", font_size=10, font_color="black", font_weight="bold", node_size=1000, arrows=True)
    plt.title("Tree Structure")
    plt.show()

# Pretty print the tree
pretty_print_tree(G, "root")
```

[child ⬇️](#63125128-93cd-4245-85ed-4eb855b0d5d9)

---

(main branch ⎇)
###### 63125128-93cd-4245-85ed-4eb855b0d5d9
[parent ⬆️](#15b380ed-29fa-4b8e-91d1-18b9badf7375)
