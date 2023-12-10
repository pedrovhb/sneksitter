---
file: /home/pedro/Documents/chatgpt_export/Markdown/Add Type Annotations to Meta.md
heading_stack: <root> -> af386d82-8669-4fd5-b1b2-6141aa4562cf -> System -> c2b49af7-74a2-4c92-a3e7-7d96aa50c9da -> System -> aaa24294-ad58-49fe-afce-ac71c5587460 -> User -> 42890c8a-58d9-4ccd-94b1-4878473cde35 -> Assistant -> 3e355077-7883-441e-a7ef-b2ee760764b2 -> Tool -> 52f1cc39-877e-4d9a-ac1b-c541879a08dd -> Assistant -> aaa297cf-5bd6-4e88-99ad-9565a3dcb295 -> User -> 2bf19926-04c4-4b5a-8ffa-177a1048e973 -> Assistant -> Potential Improvements: -> Alternative Approaches: -> aaa2dc72-e173-4e29-a3bf-a8f3afc99dbc -> User -> eef764cb-fb2f-4404-b894-e7fcc3fb26dc -> Assistant
---
# Assistant

```python
from typing import Callable, Union

class FlyweightMetaWithCustomKey(FlyweightMeta):
    def __init__(cls: Type[_T], name: str, bases: Tuple[type, ...], attrs: Dict[str, Any]) -> None:
        super().__init__(name, bases, attrs)
        cls._key_func = attrs.get('_key_func', cls.default
```

---

(main branch ⎇)
###### aaa22ddd-7040-4e6b-8d0f-1cdaada248a3
[parent ⬆️](#2bf19926-04c4-4b5a-8ffa-177a1048e973)
