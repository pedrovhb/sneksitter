### DSL-like Experience

The ultimate goal is to offer a DSL-like experience for building queries:

```python
query = (QueryBuilder(function_definition())
         .add_child(identifier("function.def"))
         .build())
```

