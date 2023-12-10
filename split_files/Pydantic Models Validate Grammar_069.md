---
file: /home/pedro/Documents/chatgpt_export/Markdown/Pydantic Models Validate Grammar.md
heading_stack: <root> -> 061eaf6e-d372-4cb3-89fb-2c4a94f643f6 -> System -> cc0cd000-c5d4-4660-bc2e-8fe013b3c090 -> System -> aaa29d07-977b-4c5b-84ea-2dbd6660aa55 -> User -> Basic Info -> Internal Nodes -> Task -> a59e5ca8-0836-43aa-95ae-557da12f334d -> Tool -> df057f39-09fe-452a-a373-0e8af0517ed8 -> Assistant -> eac7e948-a00f-48dc-9291-b50e427443d8 -> Tool -> 269ca8b2-1769-4ac8-8a5d-deb74bea2c07 -> Assistant -> f12a4d59-1929-403d-abba-eb91897bd209 -> Assistant -> 7a1efd11-fe1f-45ce-8b70-9980dd6701b5 -> Tool -> d2cd1215-a1ae-4c2a-b2e0-8fdba68f2e90 -> Assistant -> a37fa0ec-cfd0-4c94-9569-4b2f95e88c3b -> Assistant -> 2cc0efdf-d6d5-4231-bbfc-49f199cba9b3 -> Tool -> 1a5fb753-2396-462e-8a40-245073e84638 -> Assistant -> aaa214e6-f126-4374-aa7a-a864d4a4a650 -> User -> c9a1a2b6-9829-4136-84a4-7fb52290ecc2 -> Assistant -> 0aac7ebc-176b-4f59-8385-8754815705e0 -> Tool -> 90c0afda-35b5-4d6c-b767-652a10ec7009 -> Assistant -> aaa251f8-f462-4594-a7f4-5110ef19aa88 -> User -> 6f4a1dde-3ce3-4099-8dba-56f8f2ecce2e -> Assistant -> 06d698da-0d98-48ba-8744-ea08aeb456a5 -> Tool -> 91c2c938-df80-4721-9821-48906b31862c -> Assistant -> aaa2bc5d-a4c0-4982-907a-b33f5407edf6 -> User -> a2c08485-4965-42e5-9297-a02f55ebe428 -> Assistant -> adbaeae2-7686-4bd8-a984-217f8adb12f8 -> Tool -> 8fd7c313-58e6-4151-b647-c80fa34c4a77 -> Assistant -> aaa23544-1053-4bfa-8cd2-0ee10a09de03 -> User -> e3569785-9e36-4f56-b9f4-aac6c4ece636 -> Assistant -> bff1d3d5-822f-4a91-a2d9-475d5930d718 -> Tool -> b9a775e9-19be-40dd-8b3e-e0052d643237 -> Assistant -> b2094f78-f968-4f15-b6e8-00bbbaeae587 -> Assistant -> ecb86225-1d3e-4cae-9dd8-85be28ea1405 -> Tool -> f25a9b3e-1b38-47e9-9018-42bb6bf7bb6a -> Assistant -> aaa20921-bbd5-452a-ad2c-99306efcc68e -> User
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

