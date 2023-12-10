---
file: /home/pedro/Documents/chatgpt_export/Markdown/Parse ts-python-node-types JSON.md
heading_stack: <root> -> e99eb7ad-94e4-41d7-b226-2e95209438dc -> System -> f5218b62-0612-4055-a04f-15c2a4456b30 -> System -> aaa24a7d-6d79-4f2a-aa46-73a3895b401a -> User -> e2bcdb24-7d4d-4880-bc78-36cac65ea2b7 -> Assistant -> 3af7ae0b-c579-4d4a-90d3-732ef36c4077 -> Assistant
---
# Assistant

```python
from pathlib import Path
import json

# Load the JSON file
file_path = Path("/mnt/data/ts-python-node-types.json")
with file_path.open('r') as f:
    node_types_data = json.load(f)

# Show a snippet of the data to understand its structure
node_types_data[:5]
```

[child ⬇️](#8d7a4cfc-4710-4160-b2cd-0ae6821ce860)

---

(main branch ⎇)
###### 8d7a4cfc-4710-4160-b2cd-0ae6821ce860
[parent ⬆️](#3af7ae0b-c579-4d4a-90d3-732ef36c4077)