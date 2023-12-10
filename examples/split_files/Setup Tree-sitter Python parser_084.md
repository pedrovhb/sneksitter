#### Node Construction and Capture

The `.node()` method will initiate the construction of a new node. The `.capture_as()` method would be used to specify the capture name for the preceding node or field.

```python
def node(self, type: str) -> 'QueryBuilder':
    ...

def capture_as(self, name: str) -> 'QueryBuilder':
    ...
```

