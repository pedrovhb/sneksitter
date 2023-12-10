---
file: /home/pedro/Documents/chatgpt_export/Markdown/Python Function Pydantic Model.md
heading_stack: <root> -> 0762e539-3141-4568-97e1-8e2f28a26a31 -> System -> 7310dbb5-540b-40ba-ba28-f730ab506660 -> System -> aaa26adf-0eb0-4d7d-93a7-d9d284b5c9f3 -> User -> c6015848-a2ab-4b8c-8922-7bf89d9fdf34 -> Assistant -> Models -> 1. `ParameterModel` -> 2. `DecoratorModel` -> 3. `FunctionModel` -> Methods -> Class Method in `FunctionModel` -> Instance Method in `FunctionModel` -> aaa2eb12-3770-4c5c-a7d3-11878ab54370 -> User -> 0dd09b46-e035-48e5-b69f-280b00736c87 -> Assistant -> 02c086bb-208a-49fb-93b3-54248d0f2aa5 -> Tool -> 03e8d8b9-74a8-4a74-a1bf-aec328fe0a7c -> Assistant -> aaa26425-589c-40d9-908e-333cab56319e -> User -> 9e70ce7f-89db-47ac-85b9-7d73fd7ab640 -> Assistant -> 9cb5bb3a-3cd2-4945-b8b9-01e102f6b2ab -> Tool -> 4b953605-0288-49bf-8ce8-041f4a25504d -> Assistant -> 1801b898-5c26-4e7a-af26-d7268e8c01b5 -> Assistant -> 855176a8-5adb-411e-a098-cae3b880d095 -> Assistant -> 22bbc826-60cc-4070-af85-31471f4bf1de -> Tool -> e3ed333b-ba18-4842-b480-3f634245d238 -> Assistant -> aaa2ded3-1a21-484d-9326-598b00f61110 -> User -> 5b0b16af-8e39-4842-b887-04965d88167a -> Assistant -> 82554842-e6c7-4a6c-953b-8778ad13f907 -> Tool -> 9e6d99ad-6826-402d-b2df-17c8435586f0 -> Assistant -> 8ea69820-2e45-4f03-a531-0caeea4ca772 -> Assistant -> c8a255a2-f1db-4668-b976-619d18cc4c9a -> Tool -> e5a85609-e6ea-4263-800f-599e24019950 -> Assistant -> 7077a825-b4ed-4044-aeb4-4c2eef133509 -> Assistant -> 27051524-a0d0-48c2-b51f-127049bbddc3 -> Tool -> 8080c22e-9466-44bf-8bd6-5688b064d583 -> Assistant -> aaa239f7-a854-420f-9afa-841001491865 -> User -> cabb6712-685d-49e8-8af7-837ea6277f43 -> System -> a3034118-ba1f-4ee0-b487-daa540cdf236 -> Assistant -> 2f7d2cd2-9aa9-4ca1-a42f-53296be00132 -> Tool -> 8ff07254-af54-49bf-8e6f-8e2801ba7184 -> Assistant -> 2e959f2c-486e-444b-a6cf-8bb8eda6a77d -> Tool -> 77161e88-66bd-481a-b462-51820df15a4b -> Assistant -> f9e86d22-1f27-4bd6-8664-7cb72c386b6b -> Assistant -> aaa2b611-e6c8-4bed-b99d-34a0efb777c4 -> User -> 20eb6f92-e97d-4bff-9548-cc674656cf49 -> Assistant
---
# Assistant

```python
# Update the FunctionModel to include both docstring and 'pass' if there's no docstring
class FunctionModel(FunctionModel):  # Extending the existing FunctionModel
    def generate_function_signature(self) -> str:
        # Decorators
        decorators_str = "\n".join([f"@{decorator.name}({', '.join(map(str, decorator.params))})" if decorator.params else f"@{decorator.name}" for decorator in (self.decorators or [])])
        
        # Parameters
        params_str = ", ".join([
            f"{param.name}: {param.type_annotation}" if param.type_annotation else param.name for param in self.parameters
        ])
        params_str = params_str.replace("args: ", "*args: ").replace("kwargs: ", "**kwargs: ")
        
        # Return type
        return_type_str = f" -> {self.return_type}" if self.return_type else ""
        
        # Function body
        body = f'    """{self.docstring}"""' if self.docstring else "    pass"
        body = f"{body}\n    pass" if not self.docstring else body
        
        # Complete function signature
        function_signature = f"{decorators_str}\n" if decorators_str else ""
        function_signature += f"def {self.name}({params_str}){return_type_str}:\n{body}"

        return function_signature

# Test the model with a wider range of cases, including decorators
def decorator_1(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def decorator_2(x):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator

@decorator_1
@decorator_2(10)
def sample_func_1(x: int, y: str, *args, **kwargs) -> None:
    """This is a sample function."""

def sample_func_2(x, y) -> str:
    pass

@decorator_1
def sample_func_3(x, y, *args, z=10, **kwargs):
    """Another sample function."""

@decorator_2(5)
def sample_func_4(x: float) -> int:
    pass

sample_functions = [sample_func_1, sample_func_2, sample_func_3, sample_func_4]
sample_results = []

for func in sample_functions:
    # Extract decorators
    decorators = []
    if hasattr(func, "__wrapped__"):
        original_func = func.__wrapped__
        decorators.append(DecoratorModel(name=func.__name__, params=None))
        func = original_func

    function_model = FunctionModel.from_function(func)
    function_model.decorators = decorators  # Add the extracted decorators
    function_signature = function_model.generate_function_signature()
    sample_results.append((function_model, function_signature))

sample_results
```

[child ⬇️](#54e67c7c-bc03-4f36-9a83-4e77d9e68e9e)

---

(other branch ⎇)
###### 54e67c7c-bc03-4f36-9a83-4e77d9e68e9e
[parent ⬆️](#20eb6f92-e97d-4bff-9548-cc674656cf49)
