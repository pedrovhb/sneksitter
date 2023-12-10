#### 3. Creative and Novel: Context Managers

Using Python's context manager, we could nest queries to build more complex structures naturally.

```python
# Simple
with QueryBuilder() as qb:
    qb.node("function_definition")

# Advanced
with QueryBuilder() as qb:
    with qb.node("function_definition") as func_def:
        func_def.capture("func_def").predicate(lambda x: x.type == "main")
```

