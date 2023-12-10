---
file: /home/pedro/Documents/chatgpt_export/Markdown/Pydantic Models Validate Grammar.md
heading_stack: <root> -> 061eaf6e-d372-4cb3-89fb-2c4a94f643f6 -> System -> cc0cd000-c5d4-4660-bc2e-8fe013b3c090 -> System -> aaa29d07-977b-4c5b-84ea-2dbd6660aa55 -> User -> Basic Info -> Internal Nodes
---
#### Internal Nodes                                           
Many syntax nodes can have _children_. The node type object describes the possible children that a node can have using the following entries:

-   `"fields"` - An object that describes the possible fields that the node can have. The keys of this object are field names, and the values are _child type_ objects, described below.
-   `"children"` - Another _child type_ object that describes all of the node’s possible _named_ children _without_ fields.

A _child type_ object describes a set of child nodes using the following entries:

-   `"required"` - A boolean indicating whether there is always _at least one_ node in this set.
-   `"multiple"` - A boolean indicating whether there can be _multiple_ nodes in this set.                                  -   `"types"`\- An array of objects that represent the possible types of nodes in this set. Each object has two keys: `"type"` and `"named"`, whose meanings are described above.
                                                              Example with fields:

```
{
  "type": "method_definition",
  "named": true,
  "fields": {
    "body": {                                                       "multiple": false,
      "required": true,
      "types": [{ "type": "statement_block", "named": true }]
    },                                                            "decorator": {
      "multiple": true,                                             "required": false,
      "types": [{ "type": "decorator", "named": true }]
    },
    "name": {
      "multiple": false,                                            "required": true,
      "types": [
        { "type": "computed_property_name", "named": true },
        { "type": "property_identifier", "named": true }
      ]
    },
    "parameters": {
      "multiple": false,                                            "required": true,
      "types": [{ "type": "formal_parameters", "named": true }]
    }                                                           }
}                                                             ```                                                           
Example with children:                                        
```
{
  "type": "array",
  "named": true,                                                "fields": {},
  "children": {
    "multiple": true,
    "required": false,
    "types": [
      { "type": "_expression", "named": true },                     { "type": "spread_element", "named": true }
    ]                                                           }
}
```

#### Supertype Nodes

In Tree-sitter grammars, there are usually certain rules that represent abstract _categories_ of syntax nodes (e.g. “expression”, “type”, “declaration”). In the `grammar.js` file, these are often written as hidden rules whose definition is a simple `choice` where each member is just a single symbol.                                                                        Normally, hidden rules are not mentioned in the node types file, since they don’t appear in the syntax tree. But if you add a hidden rule to the grammar’s `supertypes` list, then it _will_ show up in the node types file, with the following special entry:
                                                              -   `"subtypes"` - An array of objects that specify the _types_ of nodes that this ‘supertype’ node can wrap.               
Example:                                                                                                                    ```                                                           {                                                               "type": "_declaration",
  "named": true,
  "subtypes": [                                                   { "type": "class_declaration", "named": true },               { "type": "function_declaration", "named": true },
    { "type": "generator_function_declaration", "named": true },
    { "type": "lexical_declaration", "named": true },
    { "type": "variable_declaration", "named": true }
  ]
}
```

Supertype nodes will also appear elsewhere in the node types file, as children of other node types, in a way that corresponds with how the supertype rule was used in the grammar. This can make the node types much shorter and easier to read, because a single supertype will take the place of multiple subtypes. 
Example:

```
{
  "type": "export_statement",
  "named": true,
  "fields": {
    "declaration": {
      "multiple": false,
      "required": false,
      "types": [{ "type": "_declaration", "named": true }]        },
    "source": {
      "multiple": false,
      "required": false,
      "types": [{ "type": "string", "named": true }]
    }
  }
}
```

