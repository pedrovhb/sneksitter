# Tool

```python
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[10], line 2
      1 # Using the tree_sitter_languages library to get the Python parser as specified
----> 2 parser = tree_sitter_languages.get_parser("python")
      4 # Sample Python code with complex function definition
      5 source_code = '''
      6 def foo(*vararg: str, x, y=1, /, f="a string default", *, z: int=5, w: Callable[P, T]=print, **kwargs) -> int:
      7     """This is a docstring."""
      8     pass
      9 '''

NameError: name 'tree_sitter_languages' is not defined

```

[child ⬇️](#321cb3c2-dfde-486d-9ecc-95ef4b6817f9)

---

(main branch ⎇)
###### 321cb3c2-dfde-486d-9ecc-95ef4b6817f9
[parent ⬆️](#7b89084c-52ee-48c4-a6f0-0763da4405b9)
