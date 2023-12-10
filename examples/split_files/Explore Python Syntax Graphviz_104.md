# Assistant

```python
# Checking the documentation for the relevant methods using help()
help_docs = {}
for method_name in ['next_state', 'field_name_for_id', 'lookahead_iterator']:
    method = getattr(sqlite_lang, method_name)
    help_docs[method_name] = help(method)

help_docs
```

[child ⬇️](#b868be6e-d1b4-48d9-87d7-0a038be88429)

---

(other branch ⎇)
###### b868be6e-d1b4-48d9-87d7-0a038be88429
[parent ⬆️](#8b61d765-ffe3-4265-850f-75d0d3adcd68)
