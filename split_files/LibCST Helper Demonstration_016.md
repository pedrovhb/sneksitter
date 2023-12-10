---
file: /home/pedro/Documents/chatgpt_export/Markdown/LibCST Helper Demonstration.md
heading_stack: <root> -> 18c0f1ba-374d-4172-b284-62c0ac0825f8 -> System -> 28b397c4-d269-4da8-98b4-b7dd276704c0 -> System -> aaa2665f-1e84-4cfd-921d-9a9e022a20dd -> User -> 64222186-7076-4ab1-ac82-a592c46aaf7d -> Assistant -> 0722e61c-10d6-4ddc-8d65-2687e32de790 -> Tool -> eaadfc85-96ad-46b5-890b-9577e8be73ea -> Assistant -> ab2d4700-7b84-4859-b220-f4e5454f730c -> Assistant -> 977264ba-ab27-46ce-828a-8f286e18f2f2 -> Tool
---
# Tool

```python
parse_template_module: Module(
    body=[
        SimpleStatementLine(
            body=[
                ImportFrom(
                    module=Name(
                        value='bar',
                        lpar=[],
                        rpar=[],
                    ),
                    names=[
                        ImportAlias(
                            name=Name(
                                value='Foo',
                                lpar=[],
                                rpar=[],
                            ),
                            asname=None,
                            comma=MaybeSentinel.DEFAULT,
                        ),
                    ],
                    relative=[],
                    lpar=None,
                    rpar=None,
                    semicolon=MaybeSentinel.DEFAULT,
                    whitespace_after_from=SimpleWhitespace(
                        value=' ',
                    ),
                    whitespace_before_import=SimpleWhitespace(
                        value=' ',
                    ),
                    whitespace_after_import=SimpleWhitespace(
                        value=' ',
                    ),
                ),
            ],
            leading_lines=[],
            trailing_whitespace=TrailingWhitespace(
                whitespace=SimpleWhitespace(
                    value='',
                ),
                comment=None,
                newline=Newline(
                    value=None,
                ),
            ),
        ),
    ],
    header=[],
    footer=[],
    encoding='utf-8',
    default_indent='    ',
    default_newline='\n',
    has_trailing_newline=True,
)
parse_template_expression: BinaryOperation(
    left=Name(
        value='x',
        lpar=[],
        rpar=[],
    ),
    operator=Add(
        whitespace_before=SimpleWhitespace(
            value=' ',
        ),
        whitespace_after=SimpleWhitespace(
            value=' ',
        ),
    ),
    right=Name(
        value='y',
        lpar=[],
        rpar=[],
    ),
    lpar=[],
    rpar=[],
)
parse_template_statement: SimpleStatementLine(
    body=[
        Assert(
            test=Comparison(
                left=Name(
                    value='x',
                    lpar=[],
                    rpar=[],
                ),
                comparisons=[
                    ComparisonTarget(
                        operator=GreaterThan(
                            whitespace_before=SimpleWhitespace(
                                value=' ',
                            ),
                            whitespace_after=SimpleWhitespace(
                                value=' ',
                            ),
                        ),
                        comparator=Integer(
                            value='0',
                            lpar=[],
                            rpar=[],
                        ),
                    ),
                ],
                lpar=[],
                rpar=[],
            ),
            msg=SimpleString(
                value='"Uh oh!"',
                lpar=[],
                rpar=[],
            ),
            comma=Comma(
                whitespace_before=SimpleWhitespace(
                    value='',
                ),
                whitespace_after=SimpleWhitespace(
                    value=' ',
                ),
            ),
            whitespace_after_assert=SimpleWhitespace(
                value=' ',
            ),
            semicolon=MaybeSentinel.DEFAULT,
        ),
    ],
    leading_lines=[],
    trailing_whitespace=TrailingWhitespace(
        whitespace=SimpleWhitespace(
            value='',
        ),
        comment=None,
        newline=Newline(
            value=None,
        ),
    ),
)

```

[child ⬇️](#1d0d6ff0-c483-49c7-a6d8-5f49f5690cd0)

---

(main branch ⎇)
###### 1d0d6ff0-c483-49c7-a6d8-5f49f5690cd0
[parent ⬆️](#977264ba-ab27-46ce-828a-8f286e18f2f2)
