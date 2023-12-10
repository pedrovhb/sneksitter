---
file: /home/pedro/Documents/chatgpt_export/Markdown/Python Function Pydantic Model.md
heading_stack: <root> -> 0762e539-3141-4568-97e1-8e2f28a26a31 -> System -> 7310dbb5-540b-40ba-ba28-f730ab506660 -> System -> aaa26adf-0eb0-4d7d-93a7-d9d284b5c9f3 -> User -> c6015848-a2ab-4b8c-8922-7bf89d9fdf34 -> Assistant -> Models -> 1. `ParameterModel` -> 2. `DecoratorModel` -> 3. `FunctionModel` -> Methods -> Class Method in `FunctionModel` -> Instance Method in `FunctionModel` -> aaa2eb12-3770-4c5c-a7d3-11878ab54370 -> User -> 0dd09b46-e035-48e5-b69f-280b00736c87 -> Assistant
---
# Assistant

```python
from pydantic import BaseModel, Field
from typing import List, Optional, Union, Callable
import inspect

# Define Parameter Model
class ParameterModel(BaseModel):
    name: str
    type_annotation: Optional[str] = None
    default_value: Optional[Union[str, int, float, bool, None]] = None
    is_vararg: bool = False
    is_kwarg: bool = False

# Define Decorator Model
class DecoratorModel(BaseModel):
    name: str
    params: Optional[List[Union[str, int, float, bool, None]]] = None

# Define Function Model
class FunctionModel(BaseModel):
    name: str
    parameters: List[ParameterModel]
    return_type: Optional[str] = None
    docstring: Optional[str] = None
    decorators: Optional[List[DecoratorModel]] = None

    @classmethod
    def from_function(cls, func: Callable) -> 'FunctionModel':
        func_details = inspect.signature(func)
        name = func.__name__
        docstring = func.__doc__

        # Parameters
        params = []
        for param_name, param in func_details.parameters.items():
            param_model = ParameterModel(
                name=param_name,
                type_annotation=str(param.annotation) if param.annotation != param.empty else None,
                default_value=param.default if param.default != param.empty else None,
                is_vararg=(param.kind == param.VAR_POSITIONAL),
                is_kwarg=(param.kind == param.VAR_KEYWORD)
            )
            params.append(param_model)

        # Return type
        return_type = str(func_details.return_annotation) if func_details.return_annotation != func_details.empty else None

        return cls(name=name, parameters=params, return_type=return_type, docstring=docstring)

    def generate_function_signature(self) -> str:
        # Decorators
        decorators_str = "\n".join([f"@{decorator.name}({', '.join(map(str, decorator.params))})" if decorator.params else f"@{decorator.name}" for decorator in (self.decorators or [])])

        # Parameters
        params_str = ", ".join([
            f"{param.name}: {param.type_annotation}" if param.type_annotation else param.name for param in self.parameters
        ])

        # Return type
        return_type_str = f" -> {self.return_type}" if self.return_type else ""

        # Complete function signature
        function_signature = f"{decorators_str}\n" if decorators_str else ""
        function_signature += f"def {self.name}({params_str}){return_type_str}:"

        return function_signature

# Test the model creation and function signature generation
def sample_func(x: int, y: str, *args, **kwargs) -> None:
    """This is a sample function."""

function_model = FunctionModel.from_function(sample_func)
function_signature = function_model.generate_function_signature()

function_model, function_signature
```

[child ⬇️](#02c086bb-208a-49fb-93b3-54248d0f2aa5)

---

(other branch ⎇)
###### 02c086bb-208a-49fb-93b3-54248d0f2aa5
[parent ⬆️](#0dd09b46-e035-48e5-b69f-280b00736c87)
