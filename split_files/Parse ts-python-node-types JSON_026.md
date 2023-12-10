---
file: /home/pedro/Documents/chatgpt_export/Markdown/Parse ts-python-node-types JSON.md
heading_stack: <root> -> e99eb7ad-94e4-41d7-b226-2e95209438dc -> System -> f5218b62-0612-4055-a04f-15c2a4456b30 -> System -> aaa24a7d-6d79-4f2a-aa46-73a3895b401a -> User -> e2bcdb24-7d4d-4880-bc78-36cac65ea2b7 -> Assistant -> 3af7ae0b-c579-4d4a-90d3-732ef36c4077 -> Assistant -> 8d7a4cfc-4710-4160-b2cd-0ae6821ce860 -> Tool -> 4d1b6605-d6a7-4faf-a82b-dbdbcecc9118 -> Assistant -> aaa292e7-abf4-48a3-8ec5-c9395760f1df -> User -> 95e92a2a-1ecc-4d37-a231-440fb0df8742 -> Assistant -> 61a16991-9ab7-4460-a1c6-a8b1a7370e7e -> Assistant -> 62ccd67c-1542-4215-8ac3-81d905af856a -> Tool -> 3842346c-c97b-4398-8973-b03072176022 -> Assistant -> ae562db2-9408-4995-aff8-83204950a0e6 -> Assistant
---
# Assistant

```python
from toolz import groupby, valfilter

# Separate named and unnamed types
is_named = lambda x: x['named']
grouped_by_named = groupby(is_named, node_types_data)

# Filter out entries that don't have 'type' key (just for safety)
valid_entries = lambda x: all('type' in entry for entry in x)
filtered_by_validity = {k: valfilter(valid_entries, v) for k, v in grouped_by_named.items()}

# Display the first few items of each group to verify
{k: v[:3] for k, v in filtered_by_validity.items()}
```

[child ⬇️](#48038f5b-5642-4239-92fc-ed7a2c2bbf2e)

---

(main branch ⎇)
###### 48038f5b-5642-4239-92fc-ed7a2c2bbf2e
[parent ⬆️](#ae562db2-9408-4995-aff8-83204950a0e6)
