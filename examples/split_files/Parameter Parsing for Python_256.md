# Assistant

It appears that the `actual_default_nodes_f` list is empty, which suggests that the criteria for including a node as the default value are not being met. I suspect that the list comprehension condition in `extract_default` might be too restrictive, especially the part that checks for `len(child.children) == 0`.

Let's modify the `extract_default` function to better capture such cases.

[child ⬇️](#cce2c447-873f-4c0d-b23e-294b1dbc0950)

---

(main branch ⎇)
###### cce2c447-873f-4c0d-b23e-294b1dbc0950
[parent ⬆️](#04a8aacd-1701-4d52-8409-1105516d8ac6)
