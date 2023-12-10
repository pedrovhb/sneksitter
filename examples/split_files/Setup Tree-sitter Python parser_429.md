# Tool

```python
(module (decorated_definition (decorator (identifier)) definition: (function_definition name: (identifier) parameters: (parameters) body: (block (pass_statement)))) (decorated_definition (decorator (call function: (identifier) arguments: (argument_list (string) (integer)))) definition: (function_definition name: (identifier) parameters: (parameters) body: (block (pass_statement)))) (decorated_definition (decorator (identifier)) (decorator (identifier)) definition: (function_definition name: (identifier) parameters: (parameters) body: (block (pass_statement)))) (decorated_definition (decorator (call function: (identifier) arguments: (argument_list (string) (integer)))) (decorator (identifier)) definition: (function_definition name: (identifier) parameters: (parameters) body: (block (pass_statement)))))
[(<Node type=identifier, start_point=(1, 1), end_point=(1, 17)>, 'decorator'),
 (<Node type=identifier, start_point=(2, 4), end_point=(2, 15)>,
  'function.name'),
 (<Node type=identifier, start_point=(9, 1), end_point=(9, 11)>, 'decorator'),
 (<Node type=identifier, start_point=(10, 1), end_point=(10, 11)>,
  'decorator'),
 (<Node type=identifier, start_point=(11, 4), end_point=(11, 23)>,
  'function.name'),
 (<Node type=identifier, start_point=(15, 1), end_point=(15, 17)>,
  'decorator'),
 (<Node type=identifier, start_point=(16, 4), end_point=(16, 29)>,
  'function.name')]
```

[child ⬇️](#5af620cc-ae1a-4260-928d-7499ddca7d59)

---

(main branch ⎇)
###### 5af620cc-ae1a-4260-928d-7499ddca7d59
[parent ⬆️](#98f33520-5d16-4d85-9646-8833303506f3)
