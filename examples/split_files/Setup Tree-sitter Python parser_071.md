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

