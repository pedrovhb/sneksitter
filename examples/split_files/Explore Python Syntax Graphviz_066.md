# Tool

```python
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[9], line 8
      4 sqlite_parser = get_parser("sqlite")
      6 # Exploring the syntax of SQLite by using the lookahead_iterator method
      7 sqlite_lookahead_iterator_output = [(sqlite_parser.field_name_for_id(l), sqlite_parser.node_kind_for_id(l))
----> 8                                     for l in sqlite_parser.lookahead_iterator(1)]
     10 sqlite_lookahead_iterator_output

AttributeError: 'tree_sitter.Parser' object has no attribute 'lookahead_iterator'

```

[child ⬇️](#f4cbbc7d-9acb-4f14-9ff0-afb79cd6df8d)

---

(main branch ⎇)
###### f4cbbc7d-9acb-4f14-9ff0-afb79cd6df8d
[parent ⬆️](#82ee9c8b-dd73-4204-a9c0-1f13781867c5)
