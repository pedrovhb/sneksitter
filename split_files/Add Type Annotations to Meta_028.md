---
file: /home/pedro/Documents/chatgpt_export/Markdown/Add Type Annotations to Meta.md
heading_stack: <root> -> af386d82-8669-4fd5-b1b2-6141aa4562cf -> System -> c2b49af7-74a2-4c92-a3e7-7d96aa50c9da -> System -> aaa24294-ad58-49fe-afce-ac71c5587460 -> User -> 42890c8a-58d9-4ccd-94b1-4878473cde35 -> Assistant -> 3e355077-7883-441e-a7ef-b2ee760764b2 -> Tool -> 52f1cc39-877e-4d9a-ac1b-c541879a08dd -> Assistant -> aaa297cf-5bd6-4e88-99ad-9565a3dcb295 -> User -> 2bf19926-04c4-4b5a-8ffa-177a1048e973 -> Assistant -> Potential Improvements: -> Alternative Approaches: -> aaa2dc72-e173-4e29-a3bf-a8f3afc99dbc -> User -> eef764cb-fb2f-4404-b894-e7fcc3fb26dc -> Assistant -> aaa22ddd-7040-4e6b-8d0f-1cdaada248a3 -> User -> 6b703758-4354-4dec-94b2-03d23186107e -> Assistant -> ae6e0bae-51a7-416c-b7e4-96bf9dbd0fe4 -> Tool
---
# Tool

```python
---------------------------------------------------------------------------
RecursionError                            Traceback (most recent call last)
Cell In[3], line 29
     26         self.y = y
     28 # Test
---> 29 a = MyClass(1, 2)
     30 b = MyClass(1, 2)
     31 c = MyClass(2, 3)

Cell In[3], line 14, in flyweight_class.<locals>.new_init(self, *args, **kwargs)
     12 else:
     13     original_init = cls.__dict__['__init__']
---> 14     original_init(self, *args, **kwargs)
     15     pool[pool_key] = self

Cell In[3], line 14, in flyweight_class.<locals>.new_init(self, *args, **kwargs)
     12 else:
     13     original_init = cls.__dict__['__init__']
---> 14     original_init(self, *args, **kwargs)
     15     pool[pool_key] = self

    [... skipping similar frames: flyweight_class.<locals>.new_init at line 14 (2967 times)]

Cell In[3], line 14, in flyweight_class.<locals>.new_init(self, *args, **kwargs)
     12 else:
     13     original_init = cls.__dict__['__init__']
---> 14     original_init(self, *args, **kwargs)
     15     pool[pool_key] = self

Cell In[3], line 10, in flyweight_class.<locals>.new_init(self, *args, **kwargs)
      7 @wraps(cls.__init__)
      8 def new_init(self, *args: Any, **kwargs: Any) -> None:
      9     pool_key = (args, frozenset(kwargs.items()))
---> 10     if pool_key in pool:
     11         self = pool[pool_key]
     12     else:

File /usr/lib/python3.8/weakref.py:151, in WeakValueDictionary.__contains__(self, key)
    149     self._commit_removals()
    150 try:
--> 151     o = self.data[key]()
    152 except KeyError:
    153     return False

RecursionError: maximum recursion depth exceeded while calling a Python object

```

[child ⬇️](#fa982528-7689-40e2-9903-52ec73241220)

---

(main branch ⎇)
###### fa982528-7689-40e2-9903-52ec73241220
[parent ⬆️](#ae6e0bae-51a7-416c-b7e4-96bf9dbd0fe4)
