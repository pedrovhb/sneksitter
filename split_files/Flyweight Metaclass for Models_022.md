---
file: /home/pedro/Documents/chatgpt_export/Markdown/Flyweight Metaclass for Models.md
heading_stack: <root> -> 644104e6-eee2-47c9-8b74-983fcdce89aa -> System -> c734da8b-007e-4793-a988-4ab6af4a8c7f -> System -> aaa21a84-fb1c-420d-a200-7e9ff8bd1dca -> User -> cc118a5e-cea7-4eb5-8a55-2d298a0eb3e4 -> Assistant -> aee36206-2846-4af8-97fc-c08ea32d04f7 -> Assistant -> fe5d834e-f4ba-4d75-a77b-b419a41172d6 -> Tool -> 3cc5cb2f-9bf2-4ec7-b730-4b7a6e37379d -> Assistant -> aaa2c0bf-efc0-41ea-9394-4821c3fecdd6 -> User -> 7770a31d-c47b-48a5-9a87-cd318296e663 -> Assistant -> 186f96c5-6c2e-4c78-90de-dfcc8ee777fc -> Tool -> c7e4a869-cad6-4bc6-8ce6-a57f1c21d6a5 -> Assistant
---
# Assistant

The Flyweight pattern has been applied to your classes using the metaclass `FlyweightMeta`. Since these classes are immutable and hashable (thanks to `@dataclass(frozen=True, eq=True)`), they're ideal candidates for this pattern. You should now see memory and potentially speed benefits when creating multiple objects with the same attributes.

Would you like to run some tests to verify that the Flyweight pattern is correctly applied?

[child ⬇️](#aaa25436-2417-4590-99f2-b2c737ebd76e)

---

(main branch ⎇)
###### aaa25436-2417-4590-99f2-b2c737ebd76e
[parent ⬆️](#c7e4a869-cad6-4bc6-8ce6-a57f1c21d6a5)
