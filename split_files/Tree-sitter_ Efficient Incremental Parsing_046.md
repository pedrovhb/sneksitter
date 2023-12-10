---
file: /home/pedro/Documents/chatgpt_export/Markdown/Tree-sitter_ Efficient Incremental Parsing.md
heading_stack: <root> -> 012b00ed-acef-415a-85a3-0bbbcc736d60 -> System -> 3432677d-89e7-4f05-8a14-86a65e6e5caf -> System -> aaa2c029-cc12-4907-ae68-01b934f5d1be -> User -> 4e51a3d9-7fcd-432b-8926-7cd5d892246f -> Assistant -> Incremental Parsing -> Parsing Algorithm -> Error Recovery -> Grammar Definition -> Language Agnostic -> Real-world Use Cases -> Conclusion -> aaa2d86d-31e7-4fae-8bf8-c834b3aef56b -> User -> e7d59657-1891-40a5-8e8c-7aaa8a004343 -> Assistant -> Nodes -> Rules -> Precedence and Associativity -> Extras and Inline Rules -> External Tokens -> Summary -> aaa2c506-af4f-4894-a109-af6bcd0e29dc -> User -> 61074e26-28a5-4990-9528-4641aa89b5be -> Assistant -> JSON -> Markdown -> TOML (Tom's Obvious, Minimal Language) -> Regular Expressions -> YAML (Yet Another Markup Language) -> INI (Initialization File Format) -> GraphQL -> Shell Script (Bash, sh) -> aaa21ec8-2708-4f8c-a47a-4cbca90d051d -> User -> d92102d3-60a8-4331-94d3-0a8c3c435284 -> Assistant -> How it Would Work -> Python Pseudo-Code -> Potential Utility -> aaa25a12-a418-4b95-a984-731ddb388361 -> User
---
# User

Here's a file for you to mv to cwd and import. You'll then be able to use pretty much any language with tree-sitter, but note that you'll instead import from tree_sitter_languages as such:

(e.g. Python, Markdown, Prolog) via the following:

```
import tree_sitter_languages

parser = tree_sitter_languages.get_parser("python")
...  # use as normal, e.g. tree = parser.parse(...), cursor = tree.walk(), cursor.go to first child, parent, next sibling, etc)
```

[child ⬇️](#77071470-a92f-4b71-8c38-ec2fd3782d9f)

---

(main branch ⎇)
###### 77071470-a92f-4b71-8c38-ec2fd3782d9f
[parent ⬆️](#aaa25a12-a418-4b95-a984-731ddb388361)