---
file: /home/pedro/Documents/chatgpt_export/Markdown/Add Type Annotations to Meta.md
heading_stack: <root> -> af386d82-8669-4fd5-b1b2-6141aa4562cf -> System -> c2b49af7-74a2-4c92-a3e7-7d96aa50c9da -> System -> aaa24294-ad58-49fe-afce-ac71c5587460 -> User -> 42890c8a-58d9-4ccd-94b1-4878473cde35 -> Assistant -> 3e355077-7883-441e-a7ef-b2ee760764b2 -> Tool -> 52f1cc39-877e-4d9a-ac1b-c541879a08dd -> Assistant -> aaa297cf-5bd6-4e88-99ad-9565a3dcb295 -> User -> 2bf19926-04c4-4b5a-8ffa-177a1048e973 -> Assistant -> Potential Improvements: -> Alternative Approaches: -> aaa2dc72-e173-4e29-a3bf-a8f3afc99dbc -> User -> eef764cb-fb2f-4404-b894-e7fcc3fb26dc -> Assistant -> aaa22ddd-7040-4e6b-8d0f-1cdaada248a3 -> User -> 6b703758-4354-4dec-94b2-03d23186107e -> Assistant
---
# Assistant

```python
from functools import wraps
from typing import Callable, Any, Dict, Type

def flyweight_class(cls: Type) -> Type:
    pool = WeakValueDictionary()
    
    @wraps(cls.__init__)
    def new_init(self, *args: Any, **kwargs: Any) -> None:
        pool_key = (args, frozenset(kwargs.items()))
        if pool_key in pool:
            self = pool[pool_key]
        else:
            original_init = cls.__dict__['__init__']
            original_init(self, *args, **kwargs)
            pool[pool_key] = self
            
    setattr(cls, '__init__', new_init)
    
    return cls

# Example usage
@flyweight_class
class MyClass:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

# Test
a = MyClass(1, 2)
b = MyClass(1, 2)
c = MyClass(2, 3)

print(a is b)  # Should be True
print(a is c)  # Should be False
```

[child ⬇️](#ae6e0bae-51a7-416c-b7e4-96bf9dbd0fe4)

---

(main branch ⎇)
###### ae6e0bae-51a7-416c-b7e4-96bf9dbd0fe4
[parent ⬆️](#6b703758-4354-4dec-94b2-03d23186107e)
