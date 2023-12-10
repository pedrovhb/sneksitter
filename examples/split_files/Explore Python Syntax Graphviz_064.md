# Assistant

```python
# Importing the necessary method to get the SQLite parser
from tree_sitter_languages import get_parser

# Initializing the SQLite parser
sqlite_parser = get_parser("sqlite")

# Exploring the syntax of SQLite by using the lookahead_iterator method
sqlite_lookahead_iterator_output = [(sqlite_parser.field_name_for_id(l), sqlite_parser.node_kind_for_id(l))
                                    for l in sqlite_parser.lookahead_iterator(1)]

sqlite_lookahead_iterator_output
```

[child ⬇️](#82ee9c8b-dd73-4204-a9c0-1f13781867c5)

---

(main branch ⎇)
###### 82ee9c8b-dd73-4204-a9c0-1f13781867c5
[parent ⬆️](#3e6567d5-9f63-4ad4-9d82-ffc5dcb63414)
