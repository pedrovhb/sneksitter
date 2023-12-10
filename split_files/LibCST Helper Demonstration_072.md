---
file: /home/pedro/Documents/chatgpt_export/Markdown/LibCST Helper Demonstration.md
heading_stack: <root> -> 18c0f1ba-374d-4172-b284-62c0ac0825f8 -> System -> 28b397c4-d269-4da8-98b4-b7dd276704c0 -> System -> aaa2665f-1e84-4cfd-921d-9a9e022a20dd -> User -> 64222186-7076-4ab1-ac82-a592c46aaf7d -> Assistant -> 0722e61c-10d6-4ddc-8d65-2687e32de790 -> Tool -> eaadfc85-96ad-46b5-890b-9577e8be73ea -> Assistant -> ab2d4700-7b84-4859-b220-f4e5454f730c -> Assistant -> 977264ba-ab27-46ce-828a-8f286e18f2f2 -> Tool -> 1d0d6ff0-c483-49c7-a6d8-5f49f5690cd0 -> Assistant -> b20ee073-a977-4047-ae51-666485745387 -> Assistant -> a0c81de4-0f77-4c57-b61c-4c213824def5 -> Tool -> cffbf75d-737c-40a6-8552-538f2d18a984 -> Assistant -> c40d6097-be50-4173-94ac-45fc87f6089b -> Assistant -> c3a9d57b-390f-4554-b240-97f271752492 -> Tool -> 25c70651-a21d-42c0-81c6-6fc6bdd1a2b6 -> Assistant -> aaa26001-fe0d-47d1-80a8-5546bccf40f5 -> User -> 122a0bdb-60cf-49e8-97de-8056376805ad -> Assistant -> Architecture -> Steps -> aaa22d63-7e3c-4038-ae81-c6da628abe7f -> User -> 6fb29092-adfa-49ef-a8c5-fbc475e168a1 -> Assistant -> 7d7d6e99-4842-46d8-a52f-d71e2f3d7e6b -> Tool -> 82f581f6-38c2-44da-a671-e70cf7bae462 -> Assistant -> aaa22c7e-7317-4a50-9cca-fcfc6c57acb5 -> User -> 640e9df2-372c-428c-aacb-af03ae802638 -> Assistant -> 60653f00-3541-49d1-82c1-a9eb3f5b667a -> Tool -> 006cbbe3-77a2-4072-94f3-f4cb643605fa -> Assistant -> 97388ae7-f3a7-49ad-be0a-4cec2faedfa8 -> Assistant -> aaa2f55c-57c9-4dc3-a910-623965400b88 -> User -> 7d1a20d5-e084-41d1-890f-331abd0b26eb -> Assistant -> 0c40e6f8-100e-44c9-b62a-ac85f8d426d6 -> Tool -> 17772f25-568a-43bc-a834-13a596a38837 -> Assistant -> 85817d38-9c91-4bbe-ad14-64f29b333dbd -> Assistant -> d5864175-67b9-49d7-9d65-3eb6a4a9d563 -> Tool -> 46e18970-6031-4682-9dd1-9402004cc8c6 -> Assistant -> 6f9fb546-1f45-40a4-9a91-7e4d8aa988de -> Assistant -> ea8206e7-1975-4619-a755-32cfbb5f002d -> Tool
---
# Tool

```python
---------------------------------------------------------------------------
ParserSyntaxError                         Traceback (most recent call last)
Cell In[12], line 40
     29 # Test the FunctionCodeGenerator
     30 test_function = FunctionCodeGenerator(
     31     name="my_function",
     32     parameters=[
   (...)
     37     decorators=[DecoratorModel(name="my_decorator")]
     38 )
---> 40 generated_code = test_function.generate_code()
     41 print(generated_code)

Cell In[12], line 26, in FunctionCodeGenerator.generate_code(self)
     19 func_template = f"""
     20 {decorators}
     21 def {self.name}({params}) -> {self.return_type}:
     22     pass
     23 """
     25 # Generate the function code using libcst
---> 26 func_code = parse_template_statement(func_template)
     27 return func_code

File ~/.local/lib/python3.8/site-packages/libcst/helpers/_template.py:422, in parse_template_statement(template, config, **template_replacements)
    404 """
    405 Accepts a statement template followed by a trailing newline. If a trailing
    406 newline is not provided, one will be added. Any :class:`~libcst.CSTNode`
   (...)
    418 to pass in a ``config`` from the current module under transformation.
    419 """
    421 source = mangle_template(template, {name for name in template_replacements})
--> 422 statement = cst.parse_statement(source, config)
    423 new_statement = unmangle_nodes(statement, template_replacements)
    424 if not isinstance(
    425     new_statement, (cst.SimpleStatementLine, cst.BaseCompoundStatement)
    426 ):

File ~/.local/lib/python3.8/site-packages/libcst/_parser/entrypoints.py:138, in parse_statement(source, config)
    123 """
    124 Accepts a statement followed by a trailing newline. If a trailing newline is not
    125 provided, one will be added. :func:`parse_statement` is provided mainly as a
   (...)
    135 not include leading/trailing comments.
    136 """
    137 # use detect_trailing_newline to insert a newline
--> 138 result = _parse(
    139     "stmt_input",
    140     source,
    141     config,
    142     detect_trailing_newline=True,
    143     detect_default_newline=False,
    144 )
    145 assert isinstance(result, (SimpleStatementLine, BaseCompoundStatement))
    146 return result

File ~/.local/lib/python3.8/site-packages/libcst/_parser/entrypoints.py:55, in _parse(entrypoint, source, config, detect_trailing_newline, detect_default_newline)
     52     else:
     53         raise ValueError(f"Unknown parser entry point: {entrypoint}")
---> 55     return parse(source_str)
     56 return _pure_python_parse(
     57     entrypoint,
     58     source,
   (...)
     61     detect_default_newline=detect_default_newline,
     62 )

ParserSyntaxError: Syntax Error @ 3:9.
parser error: error at 2:8: expected one of (, *, +, -, ..., AWAIT, False, NAME, NUMBER, None, True, [, break, continue, lambda, match, not, pass, ~

        def my_function(x: int = 10, y: str) -> bool:
        ^

```

[child ⬇️](#943dae8b-997f-41ff-b5b7-b0ee8bb41213)

---

(other branch ⎇)
###### 943dae8b-997f-41ff-b5b7-b0ee8bb41213
[parent ⬆️](#ea8206e7-1975-4619-a755-32cfbb5f002d)