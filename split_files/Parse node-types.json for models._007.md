---
file: /home/pedro/Documents/chatgpt_export/Markdown/Parse node-types.json for models..md
heading_stack: <root> -> 484de9b7-6d66-4eed-a655-00940b23dffd -> System -> 40bb608e-2dfa-4a1b-a046-7b8d340b36c3 -> System -> aaa2de54-e0e3-4848-813c-de80cbe3e253 -> User -> Basic Info
---
#### Basic Info                                               
Every object in this array has these two entries:
                                                              -   `"type"` - A string that indicates which grammar rule the node represents. This corresponds to the `ts_node_type` function described above.                                           -   `"named"` - A boolean that indicates whether this kind of node corresponds to a rule name in the grammar or just a string literal. See above for more info.                                                                                         Examples:

```                                                           {
  "type": "string_literal",
  "named": true
}
{                                                               "type": "+",
  "named": false
}
```                                                           
Together, these two fields constitute a unique identifier for a node type; no two top-level objects in the `node-types.json` should have the same values for both `"type"` and `"named"`.

