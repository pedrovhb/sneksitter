---
file: /home/pedro/Documents/chatgpt_export/Markdown/LibCST Helper Demonstration.md
heading_stack: <root> -> 18c0f1ba-374d-4172-b284-62c0ac0825f8 -> System -> 28b397c4-d269-4da8-98b4-b7dd276704c0 -> System -> aaa2665f-1e84-4cfd-921d-9a9e022a20dd -> User
---
# User

Please set this up and demonstrate use of the libcst helpers:

Helpers
Helpers are higher level functions built for reducing recurring code boilerplate. We add helpers as method of CSTNode or libcst.helpers package based on those principles:

CSTNode method: simple, read-only and only require data of the direct children of a CSTNode.

libcst.helpers: node transforms or require recursively traversing the syntax tree.

Construction Helpers
Functions that assist in creating a new LibCST tree.

libcst.helpers.parse_template_module(template: str, config: PartialParserConfig = PartialParserConfig(), **template_replacements: Union[BaseExpression, Annotation, AssignTarget, Param, Parameters, Arg, BaseStatement, BaseSmallStatement, BaseSuite, BaseSlice, SubscriptElement, Decorator])→ Module[source]
Accepts an entire python module template, including all leading and trailing whitespace. Any CSTNode provided as a keyword argument to this function will be inserted into the template at the appropriate location similar to an f-string expansion. For example:

module = parse_template_module("from {mod} import Foo\n", mod=Name("bar"))
The above code will parse to a module containing a single FromImport statement, referencing module bar and importing object Foo from it. Remember that if you are parsing a template as part of a substitution inside a transform, its considered best practice to pass in a config from the current module under transformation.

Note that unlike parse_module(), this function does not support bytes as an input. This is due to the fact that it is processed as a template before parsing as a module.

libcst.helpers.parse_template_expression(template: str, config: PartialParserConfig = PartialParserConfig(), **template_replacements: Union[BaseExpression, Annotation, AssignTarget, Param, Parameters, Arg, BaseStatement, BaseSmallStatement, BaseSuite, BaseSlice, SubscriptElement, Decorator])→ BaseExpression[source]
Accepts an expression template on a single line. Leading and trailing whitespace is not valid (there’s nowhere to store it on the expression node). Any CSTNode provided as a keyword argument to this function will be inserted into the template at the appropriate location similar to an f-string expansion. For example:

expression = parse_template_expression("x + {foo}", foo=Name("y")))
The above code will parse to a BinaryOperation expression adding two names (x and y) together.

Remember that if you are parsing a template as part of a substitution inside a transform, its considered best practice to pass in a config from the current module under transformation.

libcst.helpers.parse_template_statement(template: str, config: PartialParserConfig = PartialParserConfig(), **template_replacements: Union[BaseExpression, Annotation, AssignTarget, Param, Parameters, Arg, BaseStatement, BaseSmallStatement, BaseSuite, BaseSlice, SubscriptElement, Decorator])→ Union[SimpleStatementLine, BaseCompoundStatement][source]
Accepts a statement template followed by a trailing newline. If a trailing newline is not provided, one will be added. Any CSTNode provided as a keyword argument to this function will be inserted into the template at the appropriate location similar to an f-string expansion. For example:

statement = parse_template_statement("assert x > 0, {msg}", msg=SimpleString('"Uh oh!"'))
The above code will parse to an assert statement checking that some variable x is greater than zero, or providing the assert message "Uh oh!".

Remember that if you are parsing a template as part of a substitution inside a transform, its considered best practice to pass in a config from the current module under transformation.

Transformation Helpers
Functions that assist in transforming an existing LibCST node.

libcst.helpers.insert_header_comments(node: Module, comments: List[str])→ Module[source]
Insert comments after last non-empty line in header. Use this to insert one or more comments after any copyright preamble in a Module. Each comment in the list of comments must start with a # and will be placed on its own line in the appropriate location.

Traversing Helpers
Functions that assist in traversing an existing LibCST tree.

libcst.helpers.get_full_name_for_node(node: Union[str, CSTNode])→ Optional[str][source]
Return a dot concatenated full name for str, Name, Attribute. Call, Subscript, FunctionDef, ClassDef, Decorator. Return None for not supported Node.

libcst.helpers.get_full_name_for_node_or_raise(node: Union[str, CSTNode])→ str[source]
Return a dot concatenated full name for str, Name, Attribute. Call, Subscript, FunctionDef, ClassDef. Raise Exception for not supported Node.

libcst.helpers.ensure_type(node: object, nodetype: Type[CSTNodeT])→ CSTNodeT[source]
Takes any python object, and a LibCST CSTNode subclass and refines the type of the python object. This is most useful when you already know that a particular object is a certain type but your type checker is not convinced. Note that this does an instance check for you and raises an exception if it is not the right type, so this should be used in situations where you are sure of the type given previous checks.

[child ⬇️](#64222186-7076-4ab1-ac82-a592c46aaf7d)

---

(main branch ⎇)
###### 64222186-7076-4ab1-ac82-a592c46aaf7d
[parent ⬆️](#aaa2665f-1e84-4cfd-921d-9a9e022a20dd)
