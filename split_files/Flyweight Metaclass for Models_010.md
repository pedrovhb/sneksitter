---
file: /home/pedro/Documents/chatgpt_export/Markdown/Flyweight Metaclass for Models.md
heading_stack: <root> -> 644104e6-eee2-47c9-8b74-983fcdce89aa -> System -> c734da8b-007e-4793-a988-4ab6af4a8c7f -> System -> aaa21a84-fb1c-420d-a200-7e9ff8bd1dca -> User -> cc118a5e-cea7-4eb5-8a55-2d298a0eb3e4 -> Assistant -> aee36206-2846-4af8-97fc-c08ea32d04f7 -> Assistant
---
# Assistant

```python
from typing import Dict, Type, Any
from weakref import WeakValueDictionary

class FlyweightMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        cls._pool = WeakValueDictionary()
    
    def __call__(cls, *args, **kwargs):
        pool_key = (args, frozenset(kwargs.items()))
        if pool_key in cls._pool:
            return cls._pool[pool_key]
        instance = super().__call__(*args, **kwargs)
        cls._pool[pool_key] = instance
        return instance

# Test with a simple class
class Test(metaclass=FlyweightMeta):
    def __init__(self, x):
        self.x = x

# Test to ensure flyweight works
a = Test(1)
b = Test(1)
c = Test(2)
print(a is b)  # Should be True
print(a is c)  # Should be False
```

[child ⬇️](#fe5d834e-f4ba-4d75-a77b-b419a41172d6)

---

(main branch ⎇)
###### fe5d834e-f4ba-4d75-a77b-b419a41172d6
[parent ⬆️](#aee36206-2846-4af8-97fc-c08ea32d04f7)
