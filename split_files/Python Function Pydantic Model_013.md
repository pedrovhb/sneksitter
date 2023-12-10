---
file: /home/pedro/Documents/chatgpt_export/Markdown/Python Function Pydantic Model.md
heading_stack: <root> -> 0762e539-3141-4568-97e1-8e2f28a26a31 -> System -> 7310dbb5-540b-40ba-ba28-f730ab506660 -> System -> aaa26adf-0eb0-4d7d-93a7-d9d284b5c9f3 -> User -> c6015848-a2ab-4b8c-8922-7bf89d9fdf34 -> Assistant -> Models -> 1. `ParameterModel` -> 2. `DecoratorModel` -> 3. `FunctionModel` -> Methods
---
### Methods

#### Class Method in `FunctionModel`

- `@classmethod`
- `def from_function(cls, func: Callable) -> 'FunctionModel':`
  - Use Python's `inspect` module to capture function details and instantiate a `FunctionModel`.

#### Instance Method in `FunctionModel`

- `def generate_function_signature(self) -> str:`
  - Generate the function signature as a string (excluding the body) based on the model instance.

Would you like to proceed with the implementation based on this design?

[child ⬇️](#aaa2eb12-3770-4c5c-a7d3-11878ab54370)

---

(other branch ⎇)
###### aaa2eb12-3770-4c5c-a7d3-11878ab54370
[parent ⬆️](#c6015848-a2ab-4b8c-8922-7bf89d9fdf34)
