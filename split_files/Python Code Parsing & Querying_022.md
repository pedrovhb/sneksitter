---
file: /home/pedro/Documents/chatgpt_export/Markdown/Python Code Parsing & Querying.md
heading_stack: <root> -> 406f6641-271b-4a6b-99a1-790128be2ccd -> System -> f130a532-fc36-404b-b0e3-c26e0633c6e1 -> System -> aaa28037-7e53-419f-8481-51c794baccfa -> User -> Importing the necessary module and initializing the parser and language objects -> Getting the Python language and parser -> Parsing the sample code -> Printing the structure -> Constructing the query to find all definitions of classes or functions -> Creating the query -> Capturing the nodes -> Displaying the captures -> 53cd9cab-e486-484d-8cf0-194db868867f -> Assistant -> 55c32a27-fba1-4039-9e30-57f7e21cf221 -> Tool -> b3df5168-e046-4ffc-8d28-3933f74f6eb9 -> Assistant -> 79c0cb78-cd7a-49be-a928-4d619fa5b831 -> Tool
---
# Tool

```python
(module (function_definition name: (identifier) parameters: (parameters) body: (block (pass_statement))) (function_definition name: (identifier) parameters: (parameters (identifier) (identifier)) body: (block (return_statement (binary_operator left: (identifier) right: (identifier))))) (decorated_definition (decorator (identifier)) definition: (function_definition name: (identifier) parameters: (parameters) body: (block (return_statement (string))))) (decorated_definition (decorator (identifier)) definition: (function_definition name: (identifier) parameters: (parameters (identifier)) body: (block (return_statement (string))))) (class_definition name: (identifier) body: (block (function_definition name: (identifier) parameters: (parameters (identifier)) body: (block (pass_statement))))) (function_definition name: (identifier) parameters: (parameters) body: (block (function_definition name: (identifier) parameters: (parameters) body: (block (pass_statement))) (return_statement (identifier)))))
[(<Node type=function_definition, start_point=(1, 0), end_point=(2, 8)>,
  'function.def'),
 (<Node type=function_definition, start_point=(4, 0), end_point=(5, 16)>,
  'function.def'),
 (<Node type=function_definition, start_point=(8, 0), end_point=(9, 24)>,
  'function.def'),
 (<Node type=function_definition, start_point=(12, 0), end_point=(13, 32)>,
  'function.def'),
 (<Node type=function_definition, start_point=(16, 4), end_point=(17, 12)>,
  'function.def'),
 (<Node type=function_definition, start_point=(19, 0), end_point=(22, 25)>,
  'function.def'),
 (<Node type=function_definition, start_point=(20, 4), end_point=(21, 12)>,
  'function.def')]
```

[child ⬇️](#a426c1c6-3cc5-43bc-9db1-738bf0b27f63)

---

(main branch ⎇)
###### a426c1c6-3cc5-43bc-9db1-738bf0b27f63
[parent ⬆️](#79c0cb78-cd7a-49be-a928-4d619fa5b831)
