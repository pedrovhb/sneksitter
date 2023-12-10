### 2. SQLAlchemy

SQLAlchemy ORM provides a way to build SQL queries in a Pythonic way, using overloading and chaining methods.

#### Simple Example
Filter by equality:
```python
query = session.query(User).filter(User.name == 'John')
```

#### Advanced Example
Chaining multiple filters:
```python
query = session.query(User).filter(User.name == 'John').filter(User.age > 30)
```

