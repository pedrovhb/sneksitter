---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (14).md
heading_stack: <root> -> b421fd60-2b52-4eee-9122-5a7806574998 -> System -> 0e0de881-5a7b-4301-9643-ccff084a4ddf -> System -> aaa24362-c889-42c5-afec-aae36a2536d8 -> User
---
# User

Let's use Mako to design and build a Python library for generating class code from templates. What would the ideal API for this look like? I'm thinking something like

my_class = Class(name="MyClass", bases=(my_other_class,), decorators=(Decorator(dataclass, args=None, kwargs=None), attributes=AnnotatedAttribute(name="age", type=(str, int), default=18))

Given an API like that, what are the helper classes we'd have to create? How would each know to generate its piece of code so higher level ones like Class can generate their own code by composing the recursive code generation interface? How do we make sure indentation, etc is properly handled?

Let's explore these and other questions in detail.

[child ⬇️](#5e125b51-4948-41c1-bdf3-93b510bdb1af)

---

(main branch ⎇)
###### 5e125b51-4948-41c1-bdf3-93b510bdb1af
[parent ⬆️](#aaa24362-c889-42c5-afec-aae36a2536d8)
