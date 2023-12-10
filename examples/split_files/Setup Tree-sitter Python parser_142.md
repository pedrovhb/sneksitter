#### 5. Imaginative: DSL-like String Parsing

We could allow for a mini DSL (Domain Specific Language) that gets parsed into a Tree-Sitter query, inspired by PySpark SQL.

```python
# Simple
QueryBuilder("node:function_definition capture:func_def")

# Advanced
QueryBuilder("node:function_definition capture:func_def predicate:type=main")
```

