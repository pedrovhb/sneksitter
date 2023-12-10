### Some Quick Mock-up Examples:

```python
# Simple Query using Q object
q1 = Q(type="function_def")
q2 = Q(lambda node: node.parent.type == "function_def")

# Complex Query using bitwise operators
q3 = Q(type="call_expression") & Q(lambda node: node.parent.type != "function_def")

# Query using attribute surrogates
attr = A().parent.type
q4 = Q(attr == "function_def")

# Nested Queries (with immediate child)
q5 = Q(type="function_def") > "parameters"

# Nested Queries (with all descendants)
q6 = Q(type="function_def") >> "parameters"

# Recursion control
q_recursive = +Q(type="function_def")
q_non_recursive = -Q(type="function_def")
```

