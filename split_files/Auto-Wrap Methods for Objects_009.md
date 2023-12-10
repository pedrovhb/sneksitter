---
file: /home/pedro/Documents/chatgpt_export/Markdown/Auto-Wrap Methods for Objects.md
heading_stack: <root> -> 02a68d18-f2e6-4dfc-9640-eefcff9a8938 -> System -> 16f71094-696f-4659-a5b7-a5ea706f6ddd -> System -> aaa26859-01d8-49bd-b879-7d8ec5f19da1 -> User -> Test code -> 9bb4a2f9-42fa-443c-a853-8b9f8dd57093 -> Assistant
---
# Assistant

To avoid manually wrapping each method, you can use Python's `__getattr__` method to catch attribute accesses dynamically. This method is called when an attribute lookup doesn't find the attribute in the object's dictionary. Within `__getattr__`, you can then wrap the original method with your enhanced version before returning it. 

To make this work with the `ObjectProxy` from the `wrapt` library, you can override its `__getattr__` method to wrap the underlying objects' methods.

Here's a code sample that demonstrates how to do this:

[child ⬇️](#cf56d503-b701-49ba-82b9-461dc9391d56)

---

(main branch ⎇)
###### cf56d503-b701-49ba-82b9-461dc9391d56
[parent ⬆️](#9bb4a2f9-42fa-443c-a853-8b9f8dd57093)
