### Simplified API Methods

1. **`match`**: Starts matching a new node. Can take optional capture names.
    - `match(node_type: str, capture: str = None) -> 'QueryBuilder'`

2. **`child`**: Adds a child node to the current node. Can take optional field names and capture names.
    - `child(node_type: str, field: str = None, capture: str = None) -> 'QueryBuilder'`

3. **`or_`**: Signifies the end of a pattern and the start of an alternative pattern.
    - `or_() -> 'QueryBuilder'`

4. **`start_anchor`, `end_anchor`**: Adds anchors. No need for separate methods for different anchor types.
    - `start_anchor() -> 'QueryBuilder'`
    - `end_anchor() -> 'QueryBuilder'`

5. **`wildcard`**: Adds a wildcard to the current node.
    - `wildcard() -> 'QueryBuilder'`

6. **`predicate`**: Adds a predicate to the current node.
    - `predicate(name: str, *args) -> 'QueryBuilder'`

7. **`build`**: Validates and constructs the final query.
    - `build() -> str`

