---
file: /home/pedro/Documents/chatgpt_export/Markdown/Parse node-types.json for models..md
heading_stack: <root> -> 484de9b7-6d66-4eed-a655-00940b23dffd -> System -> 40bb608e-2dfa-4a1b-a046-7b8d340b36c3 -> System -> aaa2de54-e0e3-4848-813c-de80cbe3e253 -> User
---
# User

Static Node Types                                             -----------------                                             
In languages with static typing, it can be helpful for syntax trees to provide specific type information about individual syntax nodes. Tree-sitter makes this information available via a generated file called `node-types.json`. This _node types_ file provides structured data about every possible syntax node in a grammar.                                                  
You can use this data to generate type declarations in statically-typed programming languages. For example, GitHub’s Semantic uses these node types files to generate Haskell data types for every possible syntax node, which allows for code analysis algorithms to be structurally verified by the Haskell type system.

The node types file contains an array of objects, each of which describes a particular type of syntax node using the following entries:

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

