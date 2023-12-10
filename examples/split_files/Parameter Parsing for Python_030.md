# Tool

```python
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[4], line 4
      1 from typing import Optional
      3 # Extending the existing Parameter class to include the from_node method
----> 4 class Parameter(Parameter):
      6     @classmethod
      7     def from_node(
      8         cls,
      9         node: Node,
     10         description: Optional[str] = None,
     11     ) -> Parameter:
     12         """
     13         Create a Parameter object from a tree-sitter Node.
     14         
   (...)
     20             A Parameter object populated based on the node and description.
     21         """

NameError: name 'Parameter' is not defined

```

[child ⬇️](#23abd332-216c-4df4-8da1-75189eb64d3e)

---

(main branch ⎇)
###### 23abd332-216c-4df4-8da1-75189eb64d3e
[parent ⬆️](#54798ad7-a127-4dc6-8649-6eef93243ed7)
