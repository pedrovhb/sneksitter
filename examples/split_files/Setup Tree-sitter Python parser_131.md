#### Lambda for Predicates

```python
# Using lambda for predicates
query = qb.match('function')['function_def'].predicate(lambda x: f'eq? {x} main')
```

By drawing inspiration from these libraries, we can create an interface that is both Pythonic and intuitive, while still allowing for complex queries.

---

(main branch ⎇)
###### aaa29f65-2f73-4aa5-b946-56f113d7b6fc
[parent ⬆️](#acf2e97a-76ad-4094-9e62-d942f0e2cf8f)
