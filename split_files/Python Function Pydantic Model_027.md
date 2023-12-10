---
file: /home/pedro/Documents/chatgpt_export/Markdown/Python Function Pydantic Model.md
heading_stack: <root> -> 0762e539-3141-4568-97e1-8e2f28a26a31 -> System -> 7310dbb5-540b-40ba-ba28-f730ab506660 -> System -> aaa26adf-0eb0-4d7d-93a7-d9d284b5c9f3 -> User -> c6015848-a2ab-4b8c-8922-7bf89d9fdf34 -> Assistant -> Models -> 1. `ParameterModel` -> 2. `DecoratorModel` -> 3. `FunctionModel` -> Methods -> Class Method in `FunctionModel` -> Instance Method in `FunctionModel` -> aaa2eb12-3770-4c5c-a7d3-11878ab54370 -> User -> 0dd09b46-e035-48e5-b69f-280b00736c87 -> Assistant -> 02c086bb-208a-49fb-93b3-54248d0f2aa5 -> Tool -> 03e8d8b9-74a8-4a74-a1bf-aec328fe0a7c -> Assistant -> aaa26425-589c-40d9-908e-333cab56319e -> User -> 9e70ce7f-89db-47ac-85b9-7d73fd7ab640 -> Assistant
---
# Assistant

```python
# Refining the FunctionModel and associated methods

class ParameterModel(BaseModel):
    name: str
    type_annotation: Optional[str] = None
    default_value: Optional[Union[str, int, float, bool, None]] = None
    is_vararg: bool = False
    is_kwarg: bool = False

class DecoratorModel(BaseModel):
    name: str
    params: Optional[List[Union[str, int, float, bool, None]]] = None

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

        params = []
        for param_name, param in func_details.parameters.items():
            type_annotation = None
            if param.annotation != param.empty:
                type_annotation = param.annotation.__name__ if inspect.isclass(param.annotation) else str(param.annotation)
            
            default_value = param.default if param.default != param.empty else None

            param_model = ParameterModel(
                name=param_name,
                type_annotation=type_annotation,
                default_value=default_value,
                is_vararg=(param.kind == param.VAR_POSITIONAL),
                is_kwarg=(param.kind == param.VAR_KEYWORD)
            )
            params.append(param_model)

        return_type = None
        if func_details.return_annotation != func_details.empty:
            return_type = func_details.return_annotation.__name__ if inspect.isclass(func_details.return_annotation) else str(func_details.return_annotation)

        return cls(name=name, parameters=params, return_type=return_type, docstring=docstring)

    def generate_function_signature(self) -> str:
        decorators_str = "\n".join([f"@{decorator.name}({', '.join(map(str, decorator.params))})" if decorator.params else f"@{decorator.name}" for decorator in (self.decorators or [])])

        params_str = []
        for param in self.parameters:
            param_str = param.name
            if param.is_vararg:
                param_str = f"*{param_str}"
            elif param.is_kwarg:
                param_str = f"**{param_str}"
            
            if param.type_annotation:
                param_str += f": {param.type_annotation}"
            
            if param.default_value is not None:
                param_str += f" = {param.default_value}"
            
            params_str.append(param_str)

        params_str = ", ".join(params_str)
        
        return_type_str = f" -> {self.return_type}" if self.return_type else ""

        function_signature = f"{decorators_str}\n" if decorators_str else ""
        function_signature += f"def {self.name}({params_str}){return_type_str}:"

        return function_signature

# Test the refined model creation and function signature generation
def sample_func(x: int, y: str, *args, z=10, **kwargs) -> None:
    """This is a refined sample function."""

function_model_refined = FunctionModel.from_function(sample_func)
function_signature_refined = function_model_refined.generate_function_signature()

function_model_refined, function_signature_refined
```

[child ⬇️](#9cb5bb3a-3cd2-4945-b8b9-01e102f6b2ab)

---

(other branch ⎇)
###### 9cb5bb3a-3cd2-4945-b8b9-01e102f6b2ab
[parent ⬆️](#9e70ce7f-89db-47ac-85b9-7d73fd7ab640)
