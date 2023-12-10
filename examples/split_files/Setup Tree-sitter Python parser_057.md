### Idiomatic Use

An idiomatic use of this builder would look something like this:

```python
query = (QueryBuilder(Node("function_definition"))
         .add_child(Node("identifier", capture="function.def"))
         .build())
```

