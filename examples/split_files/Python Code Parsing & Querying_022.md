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
