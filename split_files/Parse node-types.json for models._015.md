---
file: /home/pedro/Documents/chatgpt_export/Markdown/Parse node-types.json for models..md
heading_stack: <root> -> 484de9b7-6d66-4eed-a655-00940b23dffd -> System -> 40bb608e-2dfa-4a1b-a046-7b8d340b36c3 -> System -> aaa2de54-e0e3-4848-813c-de80cbe3e253 -> User -> Basic Info -> Internal Nodes -> Task -> 9387b9ba-fae2-448c-b4df-a2a1a946c3b6 -> Tool -> b6a63d27-6380-4d59-9ae7-88eabcad6cff -> Assistant -> Key Components: -> Observations:
---
### Observations:

- A node can either have a `fields` property, a `children` property, or both. These properties specify the internal structure of the node.
- The `fields` object contains key-value pairs, where keys are field names and values are "child type" objects.
- The `children` object is similar to a "child type" object, but applies to all named children without fields.
- Supertype nodes contain a `subtypes` property, which is an array of node types that the supertype can wrap.
  
