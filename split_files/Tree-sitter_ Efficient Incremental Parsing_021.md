---
file: /home/pedro/Documents/chatgpt_export/Markdown/Tree-sitter_ Efficient Incremental Parsing.md
heading_stack: <root> -> 012b00ed-acef-415a-85a3-0bbbcc736d60 -> System -> 3432677d-89e7-4f05-8a14-86a65e6e5caf -> System -> aaa2c029-cc12-4907-ae68-01b934f5d1be -> User -> 4e51a3d9-7fcd-432b-8926-7cd5d892246f -> Assistant -> Incremental Parsing -> Parsing Algorithm -> Error Recovery -> Grammar Definition -> Language Agnostic -> Real-world Use Cases -> Conclusion -> aaa2d86d-31e7-4fae-8bf8-c834b3aef56b -> User -> e7d59657-1891-40a5-8e8c-7aaa8a004343 -> Assistant -> Nodes -> Rules
---
### Rules

Each node is associated with a parsing rule that describes how to recognize it in the source code. Rules can be simple or complex, involving sequences, choices, repetitions, and references to other rules.

```json
{
  "rules": {
    "function_declaration": {
      "type": "seq",
      "members": [
        {"type": "string", "value": "def"},
        {"type": "pattern", "value": "[a-zA-Z_][a-zA-Z_0-9]*"},
        {"type": "string", "value": "("},
        {"type": "string", "value": ")"},
        {"type": "string", "value": ":"}
      ]
    }
  }
}
```

