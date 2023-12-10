---
file: /home/pedro/Documents/chatgpt_export/Markdown/Parse node-types.json for models..md
heading_stack: <root> -> 484de9b7-6d66-4eed-a655-00940b23dffd -> System -> 40bb608e-2dfa-4a1b-a046-7b8d340b36c3 -> System -> aaa2de54-e0e3-4848-813c-de80cbe3e253 -> User -> Basic Info -> Internal Nodes -> Task -> 9387b9ba-fae2-448c-b4df-a2a1a946c3b6 -> Tool -> b6a63d27-6380-4d59-9ae7-88eabcad6cff -> Assistant -> Key Components: -> Observations: -> Examples:
---
### Examples:

1. **Basic Node**:
    ```json
    {
      "type": "string_literal",
      "named": true
    }
    ```

2. **Node with Fields**:
    ```json
    {
      "type": "method_definition",
      "named": true,
      "fields": {
        "body": {
          "multiple": false,
          "required": true,
          "types": [{"type": "statement_block", "named": true}]
        }
      }
    }
    ```

3. **Node with Children**:
    ```json
    {
      "type": "array",
      "named": true,
      "children": {
        "multiple": true,
        "required": false,
        "types": [{"type": "_expression", "named": true}]
      }
    }
    ```

4. **Supertype Node**:
    ```json
    {
      "type": "_declaration",
      "named": true,
      "subtypes": [
        {"type": "class_declaration", "named": true},
        {"type": "function_declaration", "named": true}
      ]
    }
    ```

To summarize, the schema consists of nested objects that describe the tree-like structure of the language's syntax nodes, including the relationships between different types of nodes and their potential children. Nodes may be simple types with no children, or complex types with nested structures. Additionally, supertype nodes act as a way to group related node types, reducing repetition. We can now proceed to create Python dataclasses to represent this schema.

[child ⬇️](#aaa2bc1e-c7a6-4ef9-8020-e692c381a096)

---

(other branch ⎇)
###### aaa2bc1e-c7a6-4ef9-8020-e692c381a096
[parent ⬆️](#b6a63d27-6380-4d59-9ae7-88eabcad6cff)
