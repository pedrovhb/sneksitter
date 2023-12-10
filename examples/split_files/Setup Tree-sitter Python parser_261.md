# Assistant

```python
# Constructing a query to find all definitions of classes or functions
query_str = """
(
  (function_definition) @function.def
  (class_definition) @class.def
)
"""

# Creating the query
query = PY_LANGUAGE.query(query_str)

# Capturing the nodes
captures = query.captures(sample_tree.root_node)

# Displaying the captures
captures
```

[child ⬇️](#e2057ad5-a5e3-4792-bcb4-d1029ac213b4)

---

(other branch ⎇)
###### e2057ad5-a5e3-4792-bcb4-d1029ac213b4
[parent ⬆️](#be4283bc-4a57-45ac-a9d4-4c32bf2b5639)
