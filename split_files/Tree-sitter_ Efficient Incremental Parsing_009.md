---
file: /home/pedro/Documents/chatgpt_export/Markdown/Tree-sitter_ Efficient Incremental Parsing.md
heading_stack: <root> -> 012b00ed-acef-415a-85a3-0bbbcc736d60 -> System -> 3432677d-89e7-4f05-8a14-86a65e6e5caf -> System -> aaa2c029-cc12-4907-ae68-01b934f5d1be -> User -> 4e51a3d9-7fcd-432b-8926-7cd5d892246f -> Assistant -> Incremental Parsing
---
### Incremental Parsing

One of Tree-sitter's standout features is incremental parsing. This means that when a small change is made to the source code, Tree-sitter doesn't re-parse the entire text; it only updates the portions of the tree that are affected. This is crucial for editor integrations where real-time feedback is needed.

