# Assistant

```python
from enum import Enum, auto

class ParamState(Enum):
    INIT = auto()
    NAME = auto()
    VARARG = auto()
    KWARG = auto()
    TYPE = auto()
    DEFAULT = auto()
    POS_ONLY = auto()
    KW_ONLY = auto()
```

Now let's proceed with the code that will actually handle the parsing.

[child ⬇️](#45bd1bba-f9c3-4155-8793-2913f7d7ce64)

---

(main branch ⎇)
###### 45bd1bba-f9c3-4155-8793-2913f7d7ce64
[parent ⬆️](#1e12ab6d-fb7a-4149-802e-834c601599fd)
