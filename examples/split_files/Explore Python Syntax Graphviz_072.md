# Assistant

```python
# Getting the SQLite language object similar to how we got the Python language object
sqlite_lang = get_language("sqlite")

# Exploring the syntax of SQLite by using the lookahead_iterator method
sqlite_lookahead_iterator_output = [(sqlite_lang.field_name_for_id(l), sqlite_lang.node_kind_for_id(l))
                                    for l in sqlite_lang.lookahead_iterator(1)]

sqlite_lookahead_iterator_output
```

[child ⬇️](#e534f1c3-b20f-46c2-80e0-64bcc165c5a1)

---

(main branch ⎇)
###### e534f1c3-b20f-46c2-80e0-64bcc165c5a1
[parent ⬆️](#c3fbc009-0d4a-42cc-ae0d-6b0cb32fd8dc)
