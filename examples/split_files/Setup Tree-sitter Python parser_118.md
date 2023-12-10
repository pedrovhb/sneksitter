#### Advanced Example
Chaining multiple filters:
```python
query = session.query(User).filter(User.name == 'John').filter(User.age > 30)
```

