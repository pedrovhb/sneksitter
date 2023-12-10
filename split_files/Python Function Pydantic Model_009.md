---
file: /home/pedro/Documents/chatgpt_export/Markdown/Python Function Pydantic Model.md
heading_stack: <root> -> 0762e539-3141-4568-97e1-8e2f28a26a31 -> System -> 7310dbb5-540b-40ba-ba28-f730ab506660 -> System -> aaa26adf-0eb0-4d7d-93a7-d9d284b5c9f3 -> User -> c6015848-a2ab-4b8c-8922-7bf89d9fdf34 -> Assistant -> Models
---
### Models

#### 1. `ParameterModel`

- `name`: str - Name of the parameter
- `type_annotation`: Optional[str] - Type annotation, if any
- `default_value`: Optional[Union[str, int, float, bool, None]] - Default value, if any
- `is_vararg`: bool - Is it a `*args` parameter?
- `is_kwarg`: bool - Is it a `**kwargs` parameter?

#### 2. `DecoratorModel`

- `name`: str - Name of the decorator
- `params`: Optional[List[Union[str, int, float, bool, None]]] - Parameters for the decorator, if any

#### 3. `FunctionModel`

- `name`: str - Name of the function
- `parameters`: List[`ParameterModel`] - List of parameters
- `return_type`: Optional[str] - Return type annotation, if any
- `docstring`: Optional[str] - Docstring for the function
- `decorators`: Optional[List[`DecoratorModel`]] - List of decorators

