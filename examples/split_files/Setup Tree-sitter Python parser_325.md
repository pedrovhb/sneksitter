# Assistant

```python
# Debugging the query syntax by breaking down the query into its components
# Starting with function definition only to simplify debugging
debug_query_function = py_language.query("""
    (function_definition
        name: (identifier) @function_name
        parameters: (parameters) @function_parameters
        (decorator (identifier) @function_decorator (argument_list) @decorator_args?))
""")

# If this part works, we can then proceed to include the class definition component
```

[child ⬇️](#66964fd2-2cec-4d17-bdb8-3dd8c6faee0d)

---

(main branch ⎇)
###### 66964fd2-2cec-4d17-bdb8-3dd8c6faee0d
[parent ⬆️](#9e90052b-b88e-44f6-9f45-6f6b72a310ec)
