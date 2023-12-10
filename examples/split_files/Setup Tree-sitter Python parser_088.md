#### Predicates

Predicates like `eq?` can be added using the `.predicate()` method, which takes the predicate name and its arguments.

```python
def predicate(self, name: str, *args) -> 'QueryBuilder':
    ...
```

