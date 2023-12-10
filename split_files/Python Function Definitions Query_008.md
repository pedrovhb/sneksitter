---
file: /home/pedro/Documents/chatgpt_export/Markdown/Python Function Definitions Query.md
heading_stack: <root> -> af63b3c6-b4b9-47f8-92c5-59f5b08603e7 -> System -> dcabf22d-92d0-449e-8686-2c7e43e2f39c -> System -> aaa22690-6d8e-4504-a70b-5fbe6251733f -> User -> 1f1162d3-3417-4658-af1b-8a20004d7c71 -> Assistant
---
# Assistant

Certainly. In Tree-sitter, you can use queries to capture nodes of interest in the syntax tree. Here's a Tree-sitter query that should capture Python function definitions, along with their decorators if present:

```scheme
; Capture function definition and its name
(function_definition
  name: (identifier) @function.name) @function.definition

; Capture decorators if present
(
  (decorator)+
  .
  (function_definition)
) @function.with-decorators

; Optionally, capture the individual decorators
(decorator
  name: [
    (dotted_name (identifier) @decorator.name)
    (call_expression
      function: (dotted_name (identifier) @decorator.name)
    )
  ]
) @decorator
```

In this query:

- `@function.definition` captures the function definition.
- `@function.name` captures the function's name.
- `@function.with-decorators` captures function definitions that have one or more decorators.
- `@decorator` captures individual decorators.
- `@decorator.name` captures the name of each decorator.

The query uses Tree-sitter's S-expression-based query language, making it relatively straightforward to specify complex patterns in the syntax tree. Would you like more details on any specific part?

---
