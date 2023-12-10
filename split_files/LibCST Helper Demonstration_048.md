---
file: /home/pedro/Documents/chatgpt_export/Markdown/LibCST Helper Demonstration.md
heading_stack: <root> -> 18c0f1ba-374d-4172-b284-62c0ac0825f8 -> System -> 28b397c4-d269-4da8-98b4-b7dd276704c0 -> System -> aaa2665f-1e84-4cfd-921d-9a9e022a20dd -> User -> 64222186-7076-4ab1-ac82-a592c46aaf7d -> Assistant -> 0722e61c-10d6-4ddc-8d65-2687e32de790 -> Tool -> eaadfc85-96ad-46b5-890b-9577e8be73ea -> Assistant -> ab2d4700-7b84-4859-b220-f4e5454f730c -> Assistant -> 977264ba-ab27-46ce-828a-8f286e18f2f2 -> Tool -> 1d0d6ff0-c483-49c7-a6d8-5f49f5690cd0 -> Assistant -> b20ee073-a977-4047-ae51-666485745387 -> Assistant -> a0c81de4-0f77-4c57-b61c-4c213824def5 -> Tool -> cffbf75d-737c-40a6-8552-538f2d18a984 -> Assistant -> c40d6097-be50-4173-94ac-45fc87f6089b -> Assistant -> c3a9d57b-390f-4554-b240-97f271752492 -> Tool -> 25c70651-a21d-42c0-81c6-6fc6bdd1a2b6 -> Assistant -> aaa26001-fe0d-47d1-80a8-5546bccf40f5 -> User -> 122a0bdb-60cf-49e8-97de-8056376805ad -> Assistant -> Architecture -> Steps -> aaa22d63-7e3c-4038-ae81-c6da628abe7f -> User -> 6fb29092-adfa-49ef-a8c5-fbc475e168a1 -> Assistant -> 7d7d6e99-4842-46d8-a52f-d71e2f3d7e6b -> Tool -> 82f581f6-38c2-44da-a671-e70cf7bae462 -> Assistant -> aaa22c7e-7317-4a50-9cca-fcfc6c57acb5 -> User -> 640e9df2-372c-428c-aacb-af03ae802638 -> Assistant
---
# Assistant

```python
from typing import Any
from libcst import parse_template_statement, parse_template_expression

class FunctionCodeGenerator(FunctionModel):
    def generate_code(self) -> Any:
        """
        Generate the code for a Python function using libcst templates.
        """
        # Generate parameters
        params = ", ".join(
            [
                f"{param.name}: {param.type_annotation}"
                + (f" = {param.default_value}" if param.default_value else "")
                for param in self.parameters
            ]
        )
        
        # Generate decorators
        decorators = "\n".join([f"@{decorator.name}" for decorator in self.decorators])
        
        # Create the function template
        func_template = f"""
        {decorators}
        def {self.name}({params}) -> {self.return_type}:
            pass
        """
        
        # Generate the function code using libcst
        func_code = parse_template_statement(func_template)
        return func_code

# Test the FunctionCodeGenerator
test_function = FunctionCodeGenerator(
    name="my_function",
    parameters=[
        ParameterModel(name="x", type_annotation="int", default_value="10"),
        ParameterModel(name="y", type_annotation="str"),
    ],
    return_type="bool",
    decorators=[DecoratorModel(name="my_decorator")]
)

generated_code = test_function.generate_code()
print(generated_code)
```

[child ⬇️](#60653f00-3541-49d1-82c1-a9eb3f5b667a)

---

(other branch ⎇)
###### 60653f00-3541-49d1-82c1-a9eb3f5b667a
[parent ⬆️](#640e9df2-372c-428c-aacb-af03ae802638)
