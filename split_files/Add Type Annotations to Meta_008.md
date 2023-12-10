---
file: /home/pedro/Documents/chatgpt_export/Markdown/Add Type Annotations to Meta.md
heading_stack: <root> -> af386d82-8669-4fd5-b1b2-6141aa4562cf -> System -> c2b49af7-74a2-4c92-a3e7-7d96aa50c9da -> System -> aaa24294-ad58-49fe-afce-ac71c5587460 -> User -> 42890c8a-58d9-4ccd-94b1-4878473cde35 -> Assistant
---
# Assistant

```python
from typing import Any, Tuple, Dict, Type, TypeVar
from weakref import WeakValueDictionary

_T = TypeVar('_T', bound='FlyweightMeta')

class FlyweightMeta(type):
    def __init__(cls: Type[_T], name: str, bases: Tuple[type, ...], attrs: Dict[str, Any]) -> None:
        super().__init__(name, bases, attrs)
        cls._pool = WeakValueDictionary()

    def __call__(cls: Type[_T], *args: Any, **kwargs: Any) -> _T:
        pool_key = (args, frozenset(kwargs.items()))

        if pool_key in cls._pool:
            return cls._pool[pool_key]

        instance = super().__call__(*args, **kwargs)
        cls._pool[pool_key] = instance

        return instance
```

[child ⬇️](#3e355077-7883-441e-a7ef-b2ee760764b2)

---

(main branch ⎇)
###### 3e355077-7883-441e-a7ef-b2ee760764b2
[parent ⬆️](#42890c8a-58d9-4ccd-94b1-4878473cde35)
