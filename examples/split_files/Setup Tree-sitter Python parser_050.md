# Assistant

Here's a summarized YAML representation of the Tree-Sitter query language:

```yaml
Query:
  Description: "Consists of one or more patterns to match nodes in a syntax tree."
  Pattern:
    S-expression: "(node_type (child_node) (child_node))"
    Description: "Matches a node and optionally its children."

Fields:
  Basic: "(parent_node field: (child_node))"
  Negated: "(parent_node !field)"
  
AnonymousNodes:
  Syntax: '"name"'
  Example: '"!="'
  
Captures:
  Syntax: "@capture_name"
  Description: "Associates names with specific nodes for later reference."

QuantificationOperators:
  Plus: "(node)+"
  Star: "(node)*"
  Optional: "(node)?"
  
Grouping:
  Syntax: "( (node) (node) )"
  
Alternations:
  Syntax: "[ (node1) (node2) ]"
  
Wildcard:
  Named: "(_)"
  Anonymous: "_"
  
Anchors:
  FirstChild: "(parent_node . (child_node))"
  LastChild: "(parent_node (child_node) .)"
  Sibling: "(parent_node (child1) . (child2))"
  
Predicates:
  Supported:
    - eq?: "Direct match"
    - match?: "Regex match"
    - any-of?: "List match"
  Negation: "not-"
  Quantified: "any-"

QueryAPI:
  Create: "ts_query_new(language, source, source_len, error_offset, error_type)"
  Execute: "ts_query_cursor_exec(cursor, query, node)"
  Iterate:
    - TSQueryCapture
    - TSQueryMatch
    - "ts_query_cursor_next_match(cursor, match)"
```

This should give you a quick reference for constructing and executing Tree-Sitter queries. Let me know if you need more details.

[child 1 ⬇️](#aaa2bf74-6601-4af7-bc2d-ab12017d2dac) | [child 2 ⬇️](#aaa29063-77a1-4d2e-bd50-f6ee519da7f6)

---

(other branch ⎇)
###### aaa2bf74-6601-4af7-bc2d-ab12017d2dac
[parent ⬆️](#0ca77f9c-ecfc-4df4-be6b-ec2c96eb4460)
