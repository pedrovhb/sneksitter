# Assistant

```python
# Modifying the query to potentially fix the syntax error related to optional decorator arguments
incremental_query_with_decorator_fixed = py_language.query("""
    (function_definition
        name: (identifier) @function_name
        parameters: (parameters) @function_parameters
        (decorator (identifier) @function_decorator)?)
""")

# Test capturing the results to see if this part works
incremental_captures_with_decorator_fixed = incremental_query_with_decorator_fixed.captures(sample_tree.root_node)
incremental_captures_with_decorator_fixed
```

[child ⬇️](#0fc717df-3640-412f-8aed-d8f677f827c4)

---

(main branch ⎇)
###### 0fc717df-3640-412f-8aed-d8f677f827c4
[parent ⬆️](#1a26d0e0-bf3d-4be1-a72e-e9b53c366488)
