---
file: /home/pedro/Documents/chatgpt_export/Markdown/LibCST Helper Demonstration.md
heading_stack: <root> -> 18c0f1ba-374d-4172-b284-62c0ac0825f8 -> System -> 28b397c4-d269-4da8-98b4-b7dd276704c0 -> System -> aaa2665f-1e84-4cfd-921d-9a9e022a20dd -> User -> 64222186-7076-4ab1-ac82-a592c46aaf7d -> Assistant -> 0722e61c-10d6-4ddc-8d65-2687e32de790 -> Tool -> eaadfc85-96ad-46b5-890b-9577e8be73ea -> Assistant -> ab2d4700-7b84-4859-b220-f4e5454f730c -> Assistant -> 977264ba-ab27-46ce-828a-8f286e18f2f2 -> Tool -> 1d0d6ff0-c483-49c7-a6d8-5f49f5690cd0 -> Assistant -> b20ee073-a977-4047-ae51-666485745387 -> Assistant -> a0c81de4-0f77-4c57-b61c-4c213824def5 -> Tool -> cffbf75d-737c-40a6-8552-538f2d18a984 -> Assistant -> c40d6097-be50-4173-94ac-45fc87f6089b -> Assistant -> c3a9d57b-390f-4554-b240-97f271752492 -> Tool -> 25c70651-a21d-42c0-81c6-6fc6bdd1a2b6 -> Assistant -> aaa26001-fe0d-47d1-80a8-5546bccf40f5 -> User -> 122a0bdb-60cf-49e8-97de-8056376805ad -> Assistant -> Architecture -> Steps -> aaa22d63-7e3c-4038-ae81-c6da628abe7f -> User -> 6fb29092-adfa-49ef-a8c5-fbc475e168a1 -> Assistant -> 7d7d6e99-4842-46d8-a52f-d71e2f3d7e6b -> Tool -> 82f581f6-38c2-44da-a671-e70cf7bae462 -> Assistant -> aaa22c7e-7317-4a50-9cca-fcfc6c57acb5 -> User -> 640e9df2-372c-428c-aacb-af03ae802638 -> Assistant -> 60653f00-3541-49d1-82c1-a9eb3f5b667a -> Tool -> 006cbbe3-77a2-4072-94f3-f4cb643605fa -> Assistant -> 97388ae7-f3a7-49ad-be0a-4cec2faedfa8 -> Assistant -> aaa2f55c-57c9-4dc3-a910-623965400b88 -> User -> 7d1a20d5-e084-41d1-890f-331abd0b26eb -> Assistant -> 0c40e6f8-100e-44c9-b62a-ac85f8d426d6 -> Tool -> 17772f25-568a-43bc-a834-13a596a38837 -> Assistant -> 85817d38-9c91-4bbe-ad14-64f29b333dbd -> Assistant -> d5864175-67b9-49d7-9d65-3eb6a4a9d563 -> Tool -> 46e18970-6031-4682-9dd1-9402004cc8c6 -> Assistant -> 6f9fb546-1f45-40a4-9a91-7e4d8aa988de -> Assistant -> ea8206e7-1975-4619-a755-32cfbb5f002d -> Tool -> 943dae8b-997f-41ff-b5b7-b0ee8bb41213 -> Assistant -> 83ef2838-1788-49af-adb6-96a4b9e0c5ff -> Assistant
---
# Assistant

```python
from libcst import Name

# Refactoring FunctionCodeGenerator to correctly use libcst template helpers
class FunctionCodeGenerator(FunctionModel):
    def generate_code(self) -> Any:
        """
        Generate the code for a Python function using libcst templates.
        """
        # Generate parameter nodes
        params = ", ".join(
            [
                f"{param.name}: {param.type_annotation}"
                + (f" = {param.default_value}" if param.default_value else "")
                for param in self.parameters
            ]
        )
        
        # Generate decorator nodes
        decorator_nodes = [
            parse_template_expression(f"@{decorator.name}")
            for decorator in self.decorators
        ]
        
        # Create the function template
        func_template = """
        def {name}({params}) -> {return_type}:
            pass
        """
        
        # Generate the function code using libcst
        func_code = parse_template_statement(
            func_template, 
            name=Name(self.name),
            params=params,
            return_type=Name(self.return_type)
        )
        
        return func_code, decorator_nodes

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

generated_code, generated_decorators = test_function.generate_code()
print("Generated Code:", generated_code)
print("Generated Decorators:", generated_decorators)
```

[child ⬇️](#68004ece-c8f0-4aed-a7c7-ac97b88b2070)

---

(other branch ⎇)
###### 68004ece-c8f0-4aed-a7c7-ac97b88b2070
[parent ⬆️](#83ef2838-1788-49af-adb6-96a4b9e0c5ff)