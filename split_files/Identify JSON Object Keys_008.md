---
file: /home/pedro/Documents/chatgpt_export/Markdown/Identify JSON Object Keys.md
heading_stack: <root> -> 60747265-0c6c-4b6e-beaa-f7d51044e0af -> System -> 63001cc6-1d28-4fbb-a549-efc65281f584 -> System -> aaa2e9e0-e9cb-4e2c-b570-b8aa9620d0d8 -> User -> 5e02f37b-fdaa-439a-b691-0a59c0854770 -> Assistant
---
# Assistant

```python
from pathlib import Path
import json

# Initialize a set to collect unique keys
unique_keys = set()

# Read the file and identify the keys in each JSON object
file_path = Path("/mnt/data/3894654deac8dd__2022-06-03-22.jsonl")
with file_path.open("r") as file:
    for line in file:
        json_obj = json.loads(line.strip())
        unique_keys.update(json_obj.keys())

unique_keys
```

[child ⬇️](#1d6a55c7-f0df-4843-8981-4d2196502c42)

---

(main branch ⎇)
###### 1d6a55c7-f0df-4843-8981-4d2196502c42
[parent ⬆️](#5e02f37b-fdaa-439a-b691-0a59c0854770)
