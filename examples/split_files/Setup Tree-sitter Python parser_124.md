#### Advanced Example
Filtering and chaining:
```python
df.filter(df['age'] > 30).groupBy('age').count()
```

