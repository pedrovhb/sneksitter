# Assistant

The generated regular expressions and example strings for a subset of SQLite rules don't seem to be as informative as expected. Most of the values are empty, which suggests that the rules for these specific keywords (`ABORT`, `ACTION`, `ADD`, etc.) might be terminal symbols that are not defined further in the grammar. Therefore, they don't have more complex structures to represent.

The rule `sql_stmt_list` does have a generated regular expression, but it's largely empty choices, indicating that the specific `SYMBOL`s it refers to are not further defined in the grammar, at least for the depth we have traversed. 

This could be an artifact of the limited depth of recursion (`max_depth=5`) or might require more intricate handling of the grammar rules, especially for symbols that are defined recursively.

Would you like to adjust the depth or focus on specific, more complex rules for a more insightful result?

[child 1 ⬇️](#aaa205dd-eef7-4543-bbf5-c598be1a2d42) | [child 2 ⬇️](#aaa2e1ff-2cd0-4fa8-8c6c-95847f33dd54)

---

(other branch ⎇)
###### aaa205dd-eef7-4543-bbf5-c598be1a2d42
[parent ⬆️](#11749c64-f95c-4162-ad1e-ebd18c2c7be9)
