---
file: /home/pedro/Documents/chatgpt_export/Markdown/Tree-sitter_ Efficient Incremental Parsing.md
heading_stack: <root> -> 012b00ed-acef-415a-85a3-0bbbcc736d60 -> System -> 3432677d-89e7-4f05-8a14-86a65e6e5caf -> System -> aaa2c029-cc12-4907-ae68-01b934f5d1be -> User -> 4e51a3d9-7fcd-432b-8926-7cd5d892246f -> Assistant -> Incremental Parsing -> Parsing Algorithm -> Error Recovery -> Grammar Definition -> Language Agnostic -> Real-world Use Cases -> Conclusion -> aaa2d86d-31e7-4fae-8bf8-c834b3aef56b -> User -> e7d59657-1891-40a5-8e8c-7aaa8a004343 -> Assistant -> Nodes -> Rules -> Precedence and Associativity -> Extras and Inline Rules
---
### Extras and Inline Rules

The grammar can specify 'extras' like whitespace or comments that can appear between any two tokens but don't affect the syntax tree. Inline rules are rules that aren't named and don't appear in the final syntax tree, often used for more complex pattern matching.

```json
{
  "extras": [
    {"type": "pattern", "value": "\\s+"},
    {"type": "pattern", "value": "//.*?\\n"}
  ]
}
```

