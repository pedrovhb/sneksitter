---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (8).md
heading_stack: <root> -> 87bd7f6a-c34c-4e21-a681-520aea876871 -> System -> 0305e3b7-9645-4e79-89a2-794319c6d100 -> System -> aaa236d3-b162-4863-965c-406dd86ac031 -> User -> 6389456d-56b1-43ae-97a4-9af03a2416cc -> Assistant
---
# Assistant

To design a library for functional composition that includes functions, async functions, iterators, and async iterators, we'll need to consider a few key design elements:

1. **Composition Operator**: We'll use the `/` operator for composition, leveraging Python's `__truediv__` for this. When you do `a / b`, it essentially performs `a.__truediv__(b)`.
2. **Function Types**: We'll need to handle regular functions, async functions, iterators, and async iterators. This can involve some type hinting using `Protocol`, `TypeVar`, etc.
3. **Execution**: The composition should execute the functions in the sequence they are composed in. If one of them is async, the composed function should also be async.
4. **Iterators & Async Iterators**: If any of the functions are iterators, the composed function should yield results as they are available.

Let's start by defining the basic `Composed` class.

[child ⬇️](#e3e20cb1-d7af-4b3a-8989-0f635e7b7b37)

---

(other branch ⎇)
###### e3e20cb1-d7af-4b3a-8989-0f635e7b7b37
[parent ⬆️](#6389456d-56b1-43ae-97a4-9af03a2416cc)
