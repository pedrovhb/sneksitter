# Tool

```python
({'functions.py': '/mnt/data/functions.py',
  'classes.py': '/mnt/data/classes.py'},
 'from pydantic import BaseModel\nfrom typing import Any, List, Tuple, Dict\n# Classes\nclass ImageIndexer(BaseModel):\n    index_storage: Any\n    metadata_storage: Any\n    @staticmethod\n    def index_images(directory:(str, recursive: bool) -> None:\n        pass\n    @staticmethod\n    def update_index(image_path:(str) -> None:\n        pass\n\nclass ImageSearcher(BaseModel):\n    index_storage: Any\n    metadata_storage: Any\n    @staticmethod\n    def search_by_text(query:(str, limit: int, file_type: str) ->')
```

[child ⬇️](#45f564c6-7303-4eeb-8b13-ebf40c0c25f8)

---

(main branch ⎇)
###### 45f564c6-7303-4eeb-8b13-ebf40c0c25f8
[parent ⬆️](#fe0bd704-545f-4770-b80e-aa39807e9cba)
