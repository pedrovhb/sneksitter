---
file: /home/pedro/Documents/chatgpt_export/Markdown/Auto-Wrap Methods for Objects.md
heading_stack: <root> -> 02a68d18-f2e6-4dfc-9640-eefcff9a8938 -> System -> 16f71094-696f-4659-a5b7-a5ea706f6ddd -> System -> aaa26859-01d8-49bd-b879-7d8ec5f19da1 -> User -> Test code -> 9bb4a2f9-42fa-443c-a853-8b9f8dd57093 -> Assistant -> cf56d503-b701-49ba-82b9-461dc9391d56 -> Assistant
---
# Assistant

```python
from wrapt import ObjectProxy
from functools import partial

class EnhancedObjectProxy(ObjectProxy):
    def __init__(self, wrapped, enhancer):
        super(EnhancedObjectProxy, self).__init__(wrapped)
        self._self_enhancer = enhancer

    def __getattr__(self, name):
        attr = super(EnhancedObjectProxy, self).__getattr__(name)
        
        if callable(attr):
            return self._self_enhancer(attr)
        else:
            return attr

# Helper function to wrap methods
def enhancer(method):
    def wrapper(*args, **kwargs):
        print(f"Enhancer: Wrapping {method.__name__}")
        return method(*args, **kwargs)
    return wrapper

# Test class
class TestClass:
    def method1(self):
        return "method1 executed"
    
    def method2(self):
        return "method2 executed"

# Create object and wrap it
test_obj = TestClass()
enhanced_obj = EnhancedObjectProxy(test_obj, enhancer)

# Call methods
print(enhanced_obj.method1())
print(enhanced_obj.method2())
```

[child ⬇️](#6d3fd887-71c7-4832-b5c8-1333d0b0e8a3)

---

(main branch ⎇)
###### 6d3fd887-71c7-4832-b5c8-1333d0b0e8a3
[parent ⬆️](#cf56d503-b701-49ba-82b9-461dc9391d56)
