# Tool

```python
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[46], line 34
     32         current_function.parameters.append(extract_text(node))
     33 elif capture == 'decorator':
---> 34     current_decorator = DecoratorInfo(name=extract_text(node))
     35     if current_function:
     36         current_function.decorators.append(current_decorator)

Cell In[46], line 19, in <lambda>(node)
     16 parsed_functions = []
     18 # Helper function to extract text from a node
---> 19 extract_text = lambda node: source_code[node.start_byte:node.end_byte].decode()
     21 # Iterate through the captures and populate the dataclasses
     22 current_function = None

NameError: name 'source_code' is not defined

```

[child ⬇️](#5ac754dd-a6c9-4af0-a472-5dc98a71d8d2)

---

(main branch ⎇)
###### 5ac754dd-a6c9-4af0-a472-5dc98a71d8d2
[parent ⬆️](#38ae3dbe-3b28-4cc0-bba8-98b882a2445d)
