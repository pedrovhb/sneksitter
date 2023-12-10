---
file: /home/pedro/Documents/chatgpt_export/Markdown/Parse node-types.json for models..md
heading_stack: <root> -> 484de9b7-6d66-4eed-a655-00940b23dffd -> System -> 40bb608e-2dfa-4a1b-a046-7b8d340b36c3 -> System -> aaa2de54-e0e3-4848-813c-de80cbe3e253 -> User -> Basic Info -> Internal Nodes -> Task -> 9387b9ba-fae2-448c-b4df-a2a1a946c3b6 -> Tool -> b6a63d27-6380-4d59-9ae7-88eabcad6cff -> Assistant -> Key Components:
---
### Key Components:

1. **Basic Info**:
    - `type`: A string indicating the grammar rule the node represents.
    - `named`: A boolean indicating whether this node corresponds to a rule name in the grammar or just a string literal.

2. **Internal Nodes**:
    - `fields`: An object describing the possible fields the node can have.
        - Each field is an object with the following keys:
            - `required`: A boolean indicating if at least one node in this set is always required.
            - `multiple`: A boolean indicating if multiple nodes in this set are allowed.
            - `types`: An array of objects with keys `type` and `named`, similar to the Basic Info.
    - `children`: Similar to `fields` but describes all possible _named_ children without fields.

3. **Supertype Nodes**:
    - `subtypes`: An array of objects specifying the types of nodes that this ‘supertype’ node can wrap.

