# Assistant

```python
# Let's run a query to capture function names, parameters, and their corresponding decorators.
# We'll aim to associate each decorator with its corresponding function during post-processing.
complex_query = py_language.query("""
    (decorated_definition
        (decorator (identifier) @decorator)
        (function_definition
            name: (identifier) @function.name
            parameters: (parameters (identifier) @parameter)
        )
    )
""")

# Capture the information
complex_captures = complex_query.captures(decorator_sample_tree.root_node)
complex_captures
```

[child ⬇️](#6b93dfd0-c0e9-497b-8c9c-ff67faceab54)

---

(main branch ⎇)
###### 6b93dfd0-c0e9-497b-8c9c-ff67faceab54
[parent ⬆️](#8e9a79ed-647a-41c5-9bea-cddf5e92ca1c)
