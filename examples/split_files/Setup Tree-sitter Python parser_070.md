### Builder Pattern

The builder pattern is used for constructing complex objects step by step. We can have a `QueryBuilder` class that provides methods for adding nodes, fields, and captures.

#### QueryBuilder Class

```python
class QueryBuilder:
    def __init__(self):
        self.query = []
        
    def add_node(self, node: Node) -> 'QueryBuilder':
        self.query.append(node)
        return self
    
    def build(self) -> str:
        # Logic for converting query list to S-expression
```

