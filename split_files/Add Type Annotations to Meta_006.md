---
file: /home/pedro/Documents/chatgpt_export/Markdown/Add Type Annotations to Meta.md
heading_stack: <root> -> af386d82-8669-4fd5-b1b2-6141aa4562cf -> System -> c2b49af7-74a2-4c92-a3e7-7d96aa50c9da -> System -> aaa24294-ad58-49fe-afce-ac71c5587460 -> User
---
# User

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


Please add type annotations.

[child ⬇️](#42890c8a-58d9-4ccd-94b1-4878473cde35)

---

(main branch ⎇)
###### 42890c8a-58d9-4ccd-94b1-4878473cde35
[parent ⬆️](#aaa24294-ad58-49fe-afce-ac71c5587460)
