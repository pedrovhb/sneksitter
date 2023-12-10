### Composing Complex Queries

Tree-Sitter queries can have complex nested structures. To handle this, we can introduce methods like `start_group` and `end_group` in `QueryBuilder` to demarcate where a group of nodes starts and ends.

