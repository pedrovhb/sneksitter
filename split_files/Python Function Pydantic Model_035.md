---
file: /home/pedro/Documents/chatgpt_export/Markdown/Python Function Pydantic Model.md
heading_stack: <root> -> 0762e539-3141-4568-97e1-8e2f28a26a31 -> System -> 7310dbb5-540b-40ba-ba28-f730ab506660 -> System -> aaa26adf-0eb0-4d7d-93a7-d9d284b5c9f3 -> User -> c6015848-a2ab-4b8c-8922-7bf89d9fdf34 -> Assistant -> Models -> 1. `ParameterModel` -> 2. `DecoratorModel` -> 3. `FunctionModel` -> Methods -> Class Method in `FunctionModel` -> Instance Method in `FunctionModel` -> aaa2eb12-3770-4c5c-a7d3-11878ab54370 -> User -> 0dd09b46-e035-48e5-b69f-280b00736c87 -> Assistant -> 02c086bb-208a-49fb-93b3-54248d0f2aa5 -> Tool -> 03e8d8b9-74a8-4a74-a1bf-aec328fe0a7c -> Assistant -> aaa26425-589c-40d9-908e-333cab56319e -> User -> 9e70ce7f-89db-47ac-85b9-7d73fd7ab640 -> Assistant -> 9cb5bb3a-3cd2-4945-b8b9-01e102f6b2ab -> Tool -> 4b953605-0288-49bf-8ce8-041f4a25504d -> Assistant -> 1801b898-5c26-4e7a-af26-d7268e8c01b5 -> Assistant -> 855176a8-5adb-411e-a098-cae3b880d095 -> Assistant
---
# Assistant

```python
# Refine Parameter and Function models to address the issues

class ParameterModel(BaseModel):
    name: str
    type_annotation: Optional[str] = None
    default_value: Optional[Union[str, int, float, bool, None]] = None
    is_vararg: bool = False
    is_kwarg: bool = False

    def generate_parameter_signature(self) -> str:
        type_str = f": {self.type_annotation}" if self.type_annotation else ""
        default_str = f" = {self.default_value}" if self.default_value is not None else ""
        prefix = "*" if self.is_vararg else "**" if self.is_kwarg else ""
        return f"{prefix}{self.name}{type_str}{default_str}"

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
                type_annotation=str(param.annotation).replace("<class '", "").replace("'>", "") if param.annotation != param.empty else None,
                default_value=param.default if param.default != param.empty else None,
                is_vararg=(param.kind == param.VAR_POSITIONAL),
                is_kwarg=(param.kind == param.VAR_KEYWORD)
            )
            params.append(param_model)

        # Return type
        return_type = str(func_details.return_annotation).replace("<class '", "").replace("'>", "") if func_details.return_annotation != func_details.empty else None

        return cls(name=name, parameters=params, return_type=return_type, docstring=docstring)

    def generate_function_signature(self) -> str:
        # Decorators
        decorators_str = "\n".join([f"@{decorator.name}({', '.join(map(str, decorator.params))})" if decorator.params else f"@{decorator.name}" for decorator in (self.decorators or [])])

        # Parameters
        params_str = ", ".join([param.generate_parameter_signature() for param in self.parameters])

        # Return type
        return_type_str = f" -> {self.return_type}" if self.return_type else ""

        # Complete function signature
        function_signature = f"{decorators_str}\n" if decorators_str else ""
        function_signature += f"def {self.name}({params_str}){return_type_str}:"

        return function_signature

# Re-test the model creation and function signature generation
function_model_refined = FunctionModel.from_function(sample_func)
function_signature_refined = function_model_refined.generate_function_signature()

function_model_refined, function_signature_refined
```

[child ⬇️](#22bbc826-60cc-4070-af85-31471f4bf1de)

---

(other branch ⎇)
###### 22bbc826-60cc-4070-af85-31471f4bf1de
[parent ⬆️](#855176a8-5adb-411e-a098-cae3b880d095)
