#### Advanced Example
Using lambda for more complex queries:
```python
soup.find_all(lambda tag: tag.name == 'div' and 'class' in tag.attrs)
```

