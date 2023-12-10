### Query Builder Class

The `QueryBuilder` class will maintain an internal list of nodes, manage the nesting levels, and construct the final S-expression.

```python
class QueryBuilder:
    def __init__(self):
        self.query = []
        self.nesting_level = 0
```

