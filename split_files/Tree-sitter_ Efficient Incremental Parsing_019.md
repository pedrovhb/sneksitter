---
file: /home/pedro/Documents/chatgpt_export/Markdown/Tree-sitter_ Efficient Incremental Parsing.md
heading_stack: <root> -> 012b00ed-acef-415a-85a3-0bbbcc736d60 -> System -> 3432677d-89e7-4f05-8a14-86a65e6e5caf -> System -> aaa2c029-cc12-4907-ae68-01b934f5d1be -> User -> 4e51a3d9-7fcd-432b-8926-7cd5d892246f -> Assistant -> Incremental Parsing -> Parsing Algorithm -> Error Recovery -> Grammar Definition -> Language Agnostic -> Real-world Use Cases -> Conclusion -> aaa2d86d-31e7-4fae-8bf8-c834b3aef56b -> User -> e7d59657-1891-40a5-8e8c-7aaa8a004343 -> Assistant
---
# Assistant

The JSON grammar files in Tree-sitter define the rules and constructs for parsing a particular language. These files serve as the blueprint for generating the parser. Understanding the structure of a Tree-sitter JSON grammar file involves breaking down its key components:

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

### External Tokens

Tree-sitter allows you to define tokens in external scanner code (usually in C). This is often used for parsing constructs that can't be easily described using CFGs, like string interpolation.

```json
{
  "externals": [
    {"type": "named", "name": "interpolated_string"}
  ]
}
```

### Summary

A Tree-sitter JSON grammar file serves as a comprehensive specification for parsing a language, encompassing nodes, rules, precedence, associativity, extras, and potentially external tokens. It is transformed into a state machine for efficient parsing.

[child ⬇️](#aaa2c506-af4f-4894-a109-af6bcd0e29dc)

---

(main branch ⎇)
###### aaa2c506-af4f-4894-a109-af6bcd0e29dc
[parent ⬆️](#e7d59657-1891-40a5-8e8c-7aaa8a004343)
