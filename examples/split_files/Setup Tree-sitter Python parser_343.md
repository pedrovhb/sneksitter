# Assistant

```python
# Adding decorator components back into the query for further debugging
incremental_query_with_decorator = py_language.query("""
    (function_definition
        name: (identifier) @function_name
        parameters: (parameters) @function_parameters
        (decorator
            (identifier) @function_decorator
            (argument_list)? @decorator_args?))
""")

# Test capturing the results to see if this part works
incremental_captures_with_decorator = incremental_query_with_decorator.captures(sample_tree.root_node)
incremental_captures_with_decorator
```

[child ⬇️](#f79b8ded-47d2-4625-9c01-29858bdf0d29)

---

(main branch ⎇)
###### f79b8ded-47d2-4625-9c01-29858bdf0d29
[parent ⬆️](#f20653cd-3d3c-40e5-88b0-6e47b15ad50c)
