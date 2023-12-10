# Assistant

```python
from tree_sitter import Language, Parser

# Load Python grammar
PY_LANGUAGE = Language('build/my-languages.so', 'python')
parser = Parser()
parser.set_language(PY_LANGUAGE)

# Sample Python code with complex function definition
source_code = '''
def foo(*vararg: str, x, y=1, /, f="a string default", *, z: int=5, w: Callable[P, T]=print, **kwargs) -> int:
    """This is a docstring."""
    pass
'''

# Parse the source code
tree = parser.parse
```

[child ⬇️](#aaa2cdb3-473c-4fc8-9440-96e9915fac05)

---

(main branch ⎇)
###### aaa2cdb3-473c-4fc8-9440-96e9915fac05
[parent ⬆️](#89d01ee3-bd4d-4220-87c7-8d9c4508ea8f)
