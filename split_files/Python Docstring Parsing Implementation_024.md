---
file: /home/pedro/Documents/chatgpt_export/Markdown/Python Docstring Parsing Implementation.md
heading_stack: <root> -> 7cf81549-956c-4cca-93d6-c48821d96908 -> System -> 6476dbd4-7f75-47f1-8b0d-9b56ca8f2c66 -> System -> aaa20e7f-9860-46c5-9c77-d930a71406c3 -> User -> 7d012bc2-71e8-4e41-929e-ddebce0ccb7f -> Assistant -> 7a848fb4-fafb-4120-84f6-6725ea253bc6 -> Assistant -> 9d7c64d3-c964-4f73-8fcc-348a8808245f -> Tool -> 7871c14c-0813-4b57-850e-b8558bb04cdd -> Assistant -> aaa26f25-a8e5-4d20-9881-caea2489d0bc -> User -> 65a2c324-69d9-44db-a6e6-e9fcccbb110b -> Assistant -> 95a4e1ea-8365-4a4f-b155-9f0fe1d7374a -> Tool -> 64ee804e-ca9f-4d24-9cb5-71547925086d -> Assistant -> a57a358d-1f70-48b4-9cb1-3a9843aa8b55 -> Tool
---
# Tool

```python
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[3], line 4
      1 # Re-defining all data classes, as the previous execution was incomplete due to the error
      3 @dataclass
----> 4 class DocElement:
      5     @classmethod
      6     def from_str(cls: Type[T], text: str) -> T:
      7         raise NotImplementedError()

Cell In[3], line 6, in DocElement()
      3 @dataclass
      4 class DocElement:
      5     @classmethod
----> 6     def from_str(cls: Type[T], text: str) -> T:
      7         raise NotImplementedError()
      9     def to_str(self) -> str:

NameError: name 'T' is not defined

```

[child ⬇️](#6eed57d3-d50a-4638-8473-366254e18a81)

---

(other branch ⎇)
###### 6eed57d3-d50a-4638-8473-366254e18a81
[parent ⬆️](#a57a358d-1f70-48b4-9cb1-3a9843aa8b55)