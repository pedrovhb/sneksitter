### 1. Pandas

Pandas DataFrame API is quite powerful and allows for complex queries in an intuitive manner.

#### Simple Example
Selecting a column by name:
```python
df['column_name']
```

#### Advanced Example
Applying lambda functions as predicates:
```python
df[df['column_name'].apply(lambda x: x > 5)]
```

