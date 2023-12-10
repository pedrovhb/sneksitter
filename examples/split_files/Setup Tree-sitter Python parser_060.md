### Convenience Functions

For elements that are frequently used, we could provide convenience functions to reduce boilerplate.

```python
def identifier(capture=None):
    return Node("identifier", capture=capture)
```

