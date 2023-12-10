---
file: /home/pedro/Documents/chatgpt_export/Markdown/Flyweight Metaclass for Models.md
heading_stack: <root> -> 644104e6-eee2-47c9-8b74-983fcdce89aa -> System -> c734da8b-007e-4793-a988-4ab6af4a8c7f -> System -> aaa21a84-fb1c-420d-a200-7e9ff8bd1dca -> User -> cc118a5e-cea7-4eb5-8a55-2d298a0eb3e4 -> Assistant
---
# Assistant

Given the data structure you've provided, implementing the Flyweight pattern can help in sharing and reusing objects, thus optimizing memory usage. Since your classes are immutable (`@dataclass(frozen=True)`), they are good candidates for Flyweight.

The key idea behind the Flyweight pattern is to have a shared pool of objects. When a request for a new object is made, the pool is checked first to see if an object with the same intrinsic state already exists. If it does, that object is returned; otherwise, a new object is created, added to the pool, and then returned.

Let's implement a metaclass for the Flyweight pattern. This metaclass will:
1. Maintain a `_pool` dictionary for each class it creates.
2. Override the `__call__` method to search the `_pool` before creating a new instance.

Here's how it would look:

[child ⬇️](#aee36206-2846-4af8-97fc-c08ea32d04f7)

---

(main branch ⎇)
###### aee36206-2846-4af8-97fc-c08ea32d04f7
[parent ⬆️](#cc118a5e-cea7-4eb5-8a55-2d298a0eb3e4)
