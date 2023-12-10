---
file: /home/pedro/Documents/chatgpt_export/Markdown/Build Networkx Graph with Cursor.md
heading_stack: <root> -> 9454ce70-1f14-454c-b6d4-dc8e17388ae1 -> System -> cdc1e4df-6ed9-4474-aa70-316fd1d37354 -> System -> aaa2cfbd-357a-4571-8976-96badef48d18 -> User -> 660d2f56-57b7-4db7-a86f-6e27fd55def8 -> Assistant -> aaa2f53f-301b-417c-b7ee-ff3a213ff44f -> User -> f88bf305-bb2b-49d3-8c39-93884f395670 -> Assistant -> d19608c1-cf76-442e-8eab-86807320e37d -> Tool -> 6cb2143c-6833-483e-81c3-0d5c2c20c84a -> Assistant -> 51b0898f-7e88-4c13-b0c8-bbb7f8e79c51 -> Assistant -> fb7ae9bc-bb46-4c32-94d3-47dc0b2b5997 -> Tool -> e5bdaef0-5f8e-4822-829f-4a51aeb66212 -> Assistant -> ea55d543-5d28-4b1c-b826-048e5193a24e -> Assistant -> e11edf56-3f99-4581-a686-28205d3be656 -> Tool
---
# Tool

```python
---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
Cell In[3], line 40
     37 G.clear()
     39 # Run the build_tree function again
---> 40 build_tree(cursor, G)
     41 G.nodes(), G.edges()

Cell In[1], line 49, in build_tree(cursor, graph, current_node)
     47     graph.add_node(sibling)
     48     graph.add_edge(current_node, sibling)
---> 49     build_tree(cursor, graph, sibling)
     51 cursor.go_to_parent()

Cell In[1], line 48, in build_tree(cursor, graph, current_node)
     46     sibling = cursor.current_node['name']
     47     graph.add_node(sibling)
---> 48     graph.add_edge(current_node, sibling)
     49     build_tree(cursor, graph, sibling)
     51 cursor.go_to_parent()

File ~/.local/lib/python3.8/site-packages/networkx/classes/digraph.py:635, in DiGraph.add_edge(self, u_of_edge, v_of_edge, **attr)
    633 datadict = self._adj[u].get(v, self.edge_attr_dict_factory())
    634 datadict.update(attr)
--> 635 self._succ[u][v] = datadict
    636 self._pred[v][u] = datadict

KeyboardInterrupt: 

WARNING: Automatic interrupt triggered after 60.0 seconds.
```

[child ⬇️](#aaa2e899-d049-4567-ab73-9a0e30522e4a)

---

(main branch ⎇)
###### aaa2e899-d049-4567-ab73-9a0e30522e4a
[parent ⬆️](#e11edf56-3f99-4581-a686-28205d3be656)
