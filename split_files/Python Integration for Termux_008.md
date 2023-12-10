---
file: /home/pedro/Documents/chatgpt_export/Markdown/Python Integration for Termux.md
heading_stack: <root> -> 842cfa9b-19ae-407c-8813-15465c7406d0 -> System -> 31367e2d-c0e4-4443-a49e-817399b436c2 -> System -> aaa20301-df23-46a0-bb75-e8209ca363a5 -> User -> 19e8ae49-a10b-4edf-8f5c-f0043a98579a -> Assistant
---
# Assistant

```python
from zipfile import ZipFile
from pathlib import Path

# Define the path to the uploaded zip file and the extraction directory
zip_path = Path("/mnt/data/termux-api-master.zip")
extract_dir = Path("/mnt/data/termux-api-master/")

# Extract the zip file
with ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

# List the files in the extracted directory to check what we have
list(extract_dir.glob("**/*"))
```

[child ⬇️](#e189b0fe-67e6-492f-b4fe-ce4d348c8aef)

---

(main branch ⎇)
###### e189b0fe-67e6-492f-b4fe-ce4d348c8aef
[parent ⬆️](#19e8ae49-a10b-4edf-8f5c-f0043a98579a)
