### 4. PySpark DataFrame

PySpark DataFrames offer a DSL (Domain Specific Language) for manipulating big data.

#### Simple Example
Selecting a column:
```python
df.select('column_name')
```

#### Advanced Example
Filtering and chaining:
```python
df.filter(df['age'] > 30).groupBy('age').count()
```

