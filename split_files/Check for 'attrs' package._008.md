---
file: /home/pedro/Documents/chatgpt_export/Markdown/Check for 'attrs' package..md
heading_stack: <root> -> bd9eea87-b0dd-41c3-ab74-6c293d6f0941 -> System -> ddd34f01-a564-4185-a4ca-fc6bf52c2a5b -> System -> aaa20153-27d7-424b-b1c4-04cec31ff68d -> User -> 4e0fdc8f-d7b1-4f61-a2f4-e0470137e4f3 -> Assistant
---
# Assistant

```python
# Checking if the `attrs` package is available in the environment
import importlib.util

# Function to check for module availability
def is_module_available(module_name: str) -> bool:
    return importlib.util.find_spec(module_name) is not None

# Check for 'attrs' module
is_module_available("attrs")
```

[child ⬇️](#a12c67fd-7b82-49b0-bd94-6a6ce28d1627)

---

(main branch ⎇)
###### a12c67fd-7b82-49b0-bd94-6a6ce28d1627
[parent ⬆️](#4e0fdc8f-d7b1-4f61-a2f4-e0470137e4f3)
