---
file: /home/pedro/Documents/chatgpt_export/Markdown/LibCST Helper Demonstration.md
heading_stack: <root> -> 18c0f1ba-374d-4172-b284-62c0ac0825f8 -> System -> 28b397c4-d269-4da8-98b4-b7dd276704c0 -> System -> aaa2665f-1e84-4cfd-921d-9a9e022a20dd -> User -> 64222186-7076-4ab1-ac82-a592c46aaf7d -> Assistant -> 0722e61c-10d6-4ddc-8d65-2687e32de790 -> Tool -> eaadfc85-96ad-46b5-890b-9577e8be73ea -> Assistant -> ab2d4700-7b84-4859-b220-f4e5454f730c -> Assistant -> 977264ba-ab27-46ce-828a-8f286e18f2f2 -> Tool -> 1d0d6ff0-c483-49c7-a6d8-5f49f5690cd0 -> Assistant -> b20ee073-a977-4047-ae51-666485745387 -> Assistant -> a0c81de4-0f77-4c57-b61c-4c213824def5 -> Tool -> cffbf75d-737c-40a6-8552-538f2d18a984 -> Assistant -> c40d6097-be50-4173-94ac-45fc87f6089b -> Assistant -> c3a9d57b-390f-4554-b240-97f271752492 -> Tool -> 25c70651-a21d-42c0-81c6-6fc6bdd1a2b6 -> Assistant -> aaa26001-fe0d-47d1-80a8-5546bccf40f5 -> User -> 122a0bdb-60cf-49e8-97de-8056376805ad -> Assistant -> Architecture -> Steps -> aaa22d63-7e3c-4038-ae81-c6da628abe7f -> User -> 6fb29092-adfa-49ef-a8c5-fbc475e168a1 -> Assistant -> 7d7d6e99-4842-46d8-a52f-d71e2f3d7e6b -> Tool -> 82f581f6-38c2-44da-a671-e70cf7bae462 -> Assistant -> aaa22c7e-7317-4a50-9cca-fcfc6c57acb5 -> User -> 640e9df2-372c-428c-aacb-af03ae802638 -> Assistant -> 60653f00-3541-49d1-82c1-a9eb3f5b667a -> Tool -> 006cbbe3-77a2-4072-94f3-f4cb643605fa -> Assistant -> 97388ae7-f3a7-49ad-be0a-4cec2faedfa8 -> Assistant -> aaa2f55c-57c9-4dc3-a910-623965400b88 -> User -> 7d1a20d5-e084-41d1-890f-331abd0b26eb -> Assistant -> 0c40e6f8-100e-44c9-b62a-ac85f8d426d6 -> Tool -> 17772f25-568a-43bc-a834-13a596a38837 -> Assistant -> 85817d38-9c91-4bbe-ad14-64f29b333dbd -> Assistant -> d5864175-67b9-49d7-9d65-3eb6a4a9d563 -> Tool -> 46e18970-6031-4682-9dd1-9402004cc8c6 -> Assistant -> 6f9fb546-1f45-40a4-9a91-7e4d8aa988de -> Assistant -> ea8206e7-1975-4619-a755-32cfbb5f002d -> Tool -> 943dae8b-997f-41ff-b5b7-b0ee8bb41213 -> Assistant -> 83ef2838-1788-49af-adb6-96a4b9e0c5ff -> Assistant -> 68004ece-c8f0-4aed-a7c7-ac97b88b2070 -> Tool -> 4f32fb32-9b65-49be-aa97-97379bf0d270 -> Assistant -> 877f7de8-009d-40b0-ac24-7c9229a829dd -> Assistant -> 0b9a6b59-011f-4c94-96a5-62b57429d91c -> Tool -> 8ba0c8d9-9055-48c1-b2fb-be14b9e86d98 -> Assistant -> 620f1811-2c21-4fe2-903b-0714f30bdcb0 -> Assistant -> 87398c72-7f83-41ea-8add-5942cc4a5b3f -> Tool -> 3bf63e94-2201-4ad3-ab06-28b0aee92b98 -> Assistant -> aaa27cfb-347a-4cb5-aa55-aacc9c15a5c5 -> User -> cfe67c45-839e-4cdb-a683-979853f35175 -> Assistant -> 0b80a9b8-90ca-47c9-bc68-70ea639464a4 -> Assistant -> aaa21714-1b65-49e6-b50b-de61f87d9d90 -> User -> a976eb9e-792f-4e54-aefe-e10a64ce3aa2 -> Assistant -> aaa23549-5d11-4cb6-b2d7-b91b56aa57c9 -> User -> 1598d8b2-5788-43eb-9eea-b68e34cb2af7 -> Assistant -> d16c379a-d6ed-4f57-a944-8ccbcb178ee0 -> Tool
---
# Tool

```python
---------------------------------------------------------------------------
ParserSyntaxError                         Traceback (most recent call last)
Cell In[25], line 36
     26 test_function_model = FunctionModel(
     27     name="my_function",
     28     parameters=[
   (...)
     33     decorators=[DecoratorModel(name="some_decorator", args=["arg1", "arg2"])]
     34 )
     35 function_component = FunctionComponent(test_function_model)
---> 36 generated_code = function_component.generate_code()
     38 print(generated_code)

Cell In[25], line 21, in FunctionComponent.generate_code(self)
     19 decorators = [f"@{decorator.name}({', '.join(decorator.args)})" for decorator in self.function_model.decorators]
     20 decorators_str = "\n".join(decorators)
---> 21 return parse_template_statement(
     22     f"{decorators_str}\ndef {self.function_model.name}({params_str}) -> {self.function_model.return_type}:\n    pass\n"
     23 )

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
parser error: error at 2:36: expected one of !=, %, &, (, *, **, +, -, ., /, //, <, <<, <=, =, ==, >, >=, >>, @, [, ^, and, if, in, is, not, or, |

    pass
        ^

```

[child ⬇️](#bef5c725-d101-46ec-9403-c878cc4b35d8)

---

(main branch ⎇)
###### bef5c725-d101-46ec-9403-c878cc4b35d8
[parent ⬆️](#d16c379a-d6ed-4f57-a944-8ccbcb178ee0)
