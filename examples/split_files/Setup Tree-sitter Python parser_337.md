# Assistant

```python
# Incrementally adding components back into the query
# This time, including function parameters
incremental_query_function = py_language.query("""
    (function_definition
        name: (identifier) @function_name
        parameters: (parameters) @function_parameters)
""")

# Test capturing the results to see if this part works
incremental_captures = incremental_query_function.captures(sample_tree.root_node)
incremental_captures
```

[child ⬇️](#3728f391-cab5-48b8-8fb2-0d877f2d8651)

---

(main branch ⎇)
###### 3728f391-cab5-48b8-8fb2-0d877f2d8651
[parent ⬆️](#d9dad5b7-3efd-43dd-8776-438b31ba16e3)
