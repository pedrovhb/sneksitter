---
file: /home/pedro/Documents/chatgpt_export/Markdown/Parse node-types.json for models..md
heading_stack: <root> -> 484de9b7-6d66-4eed-a655-00940b23dffd -> System -> 40bb608e-2dfa-4a1b-a046-7b8d340b36c3 -> System -> aaa2de54-e0e3-4848-813c-de80cbe3e253 -> User -> Basic Info -> Internal Nodes -> Task -> 9387b9ba-fae2-448c-b4df-a2a1a946c3b6 -> Tool -> b6a63d27-6380-4d59-9ae7-88eabcad6cff -> Assistant -> Key Components: -> Observations: -> Examples: -> aaa2bc1e-c7a6-4ef9-8020-e692c381a096 -> User -> 3682d6bc-a0f0-4628-af8b-6b87bf5ae291 -> Assistant -> 4e945266-3138-47a1-8055-825076720fed -> Tool -> 29f0d10f-1f29-4fa2-9f0a-94ab3ada303e -> Assistant -> d82f3fa2-d61e-4b62-9791-4fa5d90fd3d8 -> Tool -> 9d0513e1-7bb4-44d8-ba04-4017488bd7b5 -> Assistant -> 5687973b-f6b4-44dd-8753-d874c792849a -> Assistant -> aaa2f83c-9b8f-4200-aaf4-8f3ee7735d09 -> User -> 5a29425e-53e2-4952-b620-5a7c0b6b440a -> Assistant -> 078cb5a0-cad0-41fa-9128-9a1ccd758aad -> Tool -> 04fdd7fe-79e6-4377-8b0c-c0a74491dfa4 -> Assistant -> aaa2125e-286f-4a91-b0de-1d02b611af03 -> User -> 230aa5aa-41ed-44a7-8b5e-da0ee141b9b1 -> Assistant -> 6187af27-e71d-4c9e-b986-24776b23b1e0 -> Tool -> 146e447e-973f-42b9-b6c1-d43b5932c1d9 -> Assistant -> 861b740c-d72a-4285-a88e-a9d9e14a7be3 -> Assistant -> aaa257df-7e8f-4589-83a8-2bc5efadf708 -> User -> dd745f2e-985c-421f-a601-e6aec7acec08 -> Assistant -> 56b0e5ff-e78a-4fef-a0fb-34ad9c90e3a2 -> Tool -> 0b3a9a0b-715e-427b-a82a-637f80259d88 -> Assistant -> 883f97f1-c528-4d32-98df-fd6f13c0e613 -> Assistant -> 846f0d62-58f5-4d2d-852b-bae243578c50 -> Tool -> f977b04d-50ea-4234-a9f6-4edad18ac7c7 -> Assistant -> 63de661d-7ce6-42ef-97d4-486bb77df05c -> Assistant -> 7cd14f83-02f1-43d9-bd11-544417540b3d -> Tool -> 7d9e09ca-f434-4128-837e-c7092ebc1cc2 -> Assistant -> aaa2b595-8594-475d-aee6-27644f6fd586 -> User -> 537da754-8eff-473d-9902-f57a00d76d3d -> Assistant -> c3433625-b20b-4ced-a2b4-2bed2a6283e8 -> Assistant -> 2ff00ce9-0cba-42fc-a7f9-b9cbe86cf49a -> Assistant -> 092e59a4-c0d7-4b75-9d9c-3bdeedde0f9c -> Assistant -> 940ca50a-6ed9-403a-ba42-acdc7648254b -> Tool -> af960d3f-566c-4f4c-96e9-597b5c831648 -> Assistant -> 3ac6792a-0f25-41a2-b97d-31be31a5ef0a -> Assistant -> 58bd6eff-aafe-4f64-b04f-160e2031fa8c -> Tool -> c8aac6b4-1627-4c3c-be9b-d5aac4438cd2 -> Assistant -> bd332479-9ba5-45fd-ac6f-1ccdf893396c -> Assistant -> d64af5a7-a490-4f2b-a2a7-0f4be3fabc0d -> Tool -> c8643eb8-4420-4018-914d-29027a358eb9 -> Assistant -> da593c97-fd66-4e32-ab25-3aa57c354ac6 -> Assistant -> aaa29143-037b-408b-b7cf-62d4d400dc72 -> User
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

