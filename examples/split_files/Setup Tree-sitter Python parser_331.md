# Assistant

```python
# Simplifying the query to isolate the issue
# Only capturing function names for now
simplified_query_function = py_language.query("""
    (function_definition
        name: (identifier) @function_name)
""")

# Test capturing the results to see if this part works
simplified_captures = simplified_query_function.captures(sample_tree.root_node)

simplified_captures
```

[child ⬇️](#9e911583-0653-4dfb-87f4-315b8e3951a3)

---

(main branch ⎇)
###### 9e911583-0653-4dfb-87f4-315b8e3951a3
[parent ⬆️](#be0e01f0-7b4c-49ed-93df-1d948e85afe0)
