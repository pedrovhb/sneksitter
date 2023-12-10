---
file: /home/pedro/Documents/chatgpt_export/Markdown/Tree-sitter_ Efficient Incremental Parsing.md
heading_stack: <root> -> 012b00ed-acef-415a-85a3-0bbbcc736d60 -> System -> 3432677d-89e7-4f05-8a14-86a65e6e5caf -> System -> aaa2c029-cc12-4907-ae68-01b934f5d1be -> User -> 4e51a3d9-7fcd-432b-8926-7cd5d892246f -> Assistant -> Incremental Parsing -> Parsing Algorithm -> Error Recovery -> Grammar Definition -> Language Agnostic -> Real-world Use Cases -> Conclusion -> aaa2d86d-31e7-4fae-8bf8-c834b3aef56b -> User -> e7d59657-1891-40a5-8e8c-7aaa8a004343 -> Assistant -> Nodes -> Rules -> Precedence and Associativity
---
### Precedence and Associativity

The grammar can specify precedence and associativity rules to resolve ambiguities. For example, in arithmetic expressions, multiplication often has higher precedence than addition.

```json
{
  "rules": {
    "expression": {
      "type": "choice",
      "members": [
        {"type": "pattern", "value": "[0-9]+"},
        {
          "type": "seq",
          "members": [
            {"type": "rule", "name": "expression"},
            {"type": "string", "value": "+"},
            {"type": "rule", "name": "expression"}
          ],
          "precedence": 1
        },
        {
          "type": "seq",
          "members": [
            {"type": "rule", "name": "expression"},
            {"type": "string", "value": "*"},
            {"type": "rule", "name": "expression"}
          ],
          "precedence": 2
        }
      ]
    }
  }
}
```

