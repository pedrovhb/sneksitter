### Builder Pattern

We can design a Builder class that provides methods for constructing each part of a query. Each method would return a new instance of the Builder, allowing for chained calls. To kick things off, the Builder could start with a `Node` object and then provide methods for adding children, fields, and other elements.

```python
class QueryBuilder:
    def __init__(self, root: Node):
        self.root = root
    
    def add_child(self, child: Node) -> 'QueryBuilder':
        if self.root.children is None:
            self.root.children = []
        self.root.children.append(child)
        return self
    
    def add_field(self, field: str) -> 'QueryBuilder':
        self.root.field = field
        return self
    
    def capture_as(self, name: str) -> 'QueryBuilder':
        self.root.capture = name
        return self
    
    def build(self) -> Node:
        return self.root
```

