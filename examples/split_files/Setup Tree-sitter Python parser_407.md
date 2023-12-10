# Assistant

```python
# Let's first run a simpler query to just capture function names and decorators to see if we are getting any matches.
simple_query = py_language.query("""
    (decorated_definition
        (decorator (identifier) @decorator.name)
        (function_definition name: (identifier) @function.name)
    )
""")

# Capture the information
simple_captures = simple_query.captures(decorator_sample_tree.root_node)
simple_captures
```

[child ⬇️](#d1e5eeac-c820-4b3d-8c3b-ca4decbfaae1)

---

(main branch ⎇)
###### d1e5eeac-c820-4b3d-8c3b-ca4decbfaae1
[parent ⬆️](#7233baee-01e2-4e67-a6e7-bc3a89c61015)
