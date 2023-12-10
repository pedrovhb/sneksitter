# Assistant

```python
# Print the S-expression representation of the root node to inspect the tree structure
root_sexpr = decorator_sample_tree.root_node.sexp()
print(root_sexpr)

# Modify the query to use quantification for capturing multiple decorators
quantified_query = py_language.query("""
    (decorated_definition
        (decorator (identifier) @decorator)+
        (function_definition
            name: (identifier) @function.name
            parameters: (parameters (identifier) @parameter)?
        )
    )
""")

# Capture the information
quantified_captures = quantified_query.captures(decorator_sample_tree.root_node)
quantified_captures
```

[child ⬇️](#98f33520-5d16-4d85-9646-8833303506f3)

---

(main branch ⎇)
###### 98f33520-5d16-4d85-9646-8833303506f3
[parent ⬆️](#8fd50e8b-0ac5-4d37-a6e0-a48c3e5d8f5b)
