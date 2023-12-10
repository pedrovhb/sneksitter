---
file: /home/pedro/Documents/chatgpt_export/Markdown/Build Networkx Graph with Cursor.md
heading_stack: <root> -> 9454ce70-1f14-454c-b6d4-dc8e17388ae1 -> System -> cdc1e4df-6ed9-4474-aa70-316fd1d37354 -> System -> aaa2cfbd-357a-4571-8976-96badef48d18 -> User -> 660d2f56-57b7-4db7-a86f-6e27fd55def8 -> Assistant -> aaa2f53f-301b-417c-b7ee-ff3a213ff44f -> User -> f88bf305-bb2b-49d3-8c39-93884f395670 -> Assistant -> d19608c1-cf76-442e-8eab-86807320e37d -> Tool -> 6cb2143c-6833-483e-81c3-0d5c2c20c84a -> Assistant -> 51b0898f-7e88-4c13-b0c8-bbb7f8e79c51 -> Assistant -> fb7ae9bc-bb46-4c32-94d3-47dc0b2b5997 -> Tool -> e5bdaef0-5f8e-4822-829f-4a51aeb66212 -> Assistant -> ea55d543-5d28-4b1c-b826-048e5193a24e -> Assistant
---
# Assistant

```python
# Fixing the traversal logic by resetting the sibling iterator when going back to the parent
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
            # Resetting sibling iterator
            if self.parent_stack:
                self.sibling_iter = iter(self.parent_stack[-1]['children'])
            else:
                self.sibling_iter = None
            return True
        return False

# Resetting the cursor and graph
cursor = TraversalCursor(nested_data)
G.clear()

# Run the build_tree function again
build_tree(cursor, G)
G.nodes(), G.edges()
```

[child ⬇️](#e11edf56-3f99-4581-a686-28205d3be656)

---

(main branch ⎇)
###### e11edf56-3f99-4581-a686-28205d3be656
[parent ⬆️](#ea55d543-5d28-4b1c-b826-048e5193a24e)
