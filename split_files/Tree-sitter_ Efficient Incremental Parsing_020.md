---
file: /home/pedro/Documents/chatgpt_export/Markdown/Tree-sitter_ Efficient Incremental Parsing.md
heading_stack: <root> -> 012b00ed-acef-415a-85a3-0bbbcc736d60 -> System -> 3432677d-89e7-4f05-8a14-86a65e6e5caf -> System -> aaa2c029-cc12-4907-ae68-01b934f5d1be -> User -> 4e51a3d9-7fcd-432b-8926-7cd5d892246f -> Assistant -> Incremental Parsing -> Parsing Algorithm -> Error Recovery -> Grammar Definition -> Language Agnostic -> Real-world Use Cases -> Conclusion -> aaa2d86d-31e7-4fae-8bf8-c834b3aef56b -> User -> e7d59657-1891-40a5-8e8c-7aaa8a004343 -> Assistant -> Nodes
---
### Nodes

The most fundamental part of a Tree-sitter grammar is the definition of nodes, which represent syntactical constructs in the language. Nodes can be named or anonymous. Named nodes usually represent larger constructs like functions, loops, or classes. Anonymous nodes are often used for transient syntactic elements.

```json
{
  "name": "my_language",
  "nodes": [
    {"kind": "named", "name": "function_declaration"},
    {"kind": "anonymous"}
  ]
}
```

