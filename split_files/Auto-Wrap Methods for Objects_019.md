---
file: /home/pedro/Documents/chatgpt_export/Markdown/Auto-Wrap Methods for Objects.md
heading_stack: <root> -> 02a68d18-f2e6-4dfc-9640-eefcff9a8938 -> System -> 16f71094-696f-4659-a5b7-a5ea706f6ddd -> System -> aaa26859-01d8-49bd-b879-7d8ec5f19da1 -> User -> Test code -> 9bb4a2f9-42fa-443c-a853-8b9f8dd57093 -> Assistant -> cf56d503-b701-49ba-82b9-461dc9391d56 -> Assistant -> 6d3fd887-71c7-4832-b5c8-1333d0b0e8a3 -> Tool -> 20b096ce-9aa9-43c1-ba53-8914ac441b58 -> Assistant -> aaa2100b-fcee-40e7-af71-e70792d1842f -> User -> b74f810d-35a5-47ab-917b-46dc82187704 -> Assistant
---
# Assistant

```python
# Implementing EnhancedObjectProxy to automatically wrap methods of wrapped objects

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

# Enhancer function to wrap methods
def node_enhancer(method):
    def wrapper(self, *args, **kwargs):
        result = method(self.__wrapped__, *args, **kwargs)
        return EnhancedNode(result, self._self_enhanced_tree) if result else result
    return wrapper

def tree_enhancer(method):
    def wrapper(self, *args, **kwargs):
        result = method(self.__wrapped__, *args, **kwargs)
        return EnhancedTree(result, self._self_source_code) if result else result
    return wrapper

def cursor_enhancer(method):
    def wrapper(self, *args, **kwargs):
        result = method(self.__wrapped__, *args, **kwargs)
        return EnhancedCursor(result, self._self_enhanced_tree
```

[child ⬇️](#aaa237c2-2866-4cc3-899c-e5f234a1f6a9)

---

(main branch ⎇)
###### aaa237c2-2866-4cc3-899c-e5f234a1f6a9
[parent ⬆️](#b74f810d-35a5-47ab-917b-46dc82187704)
