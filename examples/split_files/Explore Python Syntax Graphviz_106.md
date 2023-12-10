# Tool

```python
Help on method next_state in module tree_sitter:

next_state(state: int, id: int) -> int method of tree_sitter.Language instance
    Get the next parse state. Combine this with
    [`lookahead_iterator`](Language.lookahead_iterator) to
    generate completion suggestions or valid symbols in error nodes.

Help on method field_name_for_id in module tree_sitter:

field_name_for_id(field_id: int) -> Union[str, NoneType] method of tree_sitter.Language instance
    Get the name of the field for the given numerical id.

Help on method lookahead_iterator in module tree_sitter:

lookahead_iterator(state: int) -> Union[tree_sitter.LookaheadIterator, NoneType] method of tree_sitter.Language instance
    Create a new lookahead iterator for this language and parse state.
    
    This returns `None` if state is invalid for this language.
    
    Iterating `LookaheadIterator` will yield valid symbols in the given
    parse state. Newly created lookahead iterators will return the `ERROR`
    symbol from `LookaheadIterator.current_symbol`.
    
    Lookahead iterators can be useful to generate suggestions and improve
    syntax error diagnostics. To get symbols valid in an ERROR node, use the
    lookahead iterator on its first leaf node state. For `MISSING` nodes, a
    lookahead iterator created on the previous non-extra leaf node may be
    appropriate.

{'next_state': None, 'field_name_for_id': None, 'lookahead_iterator': None}
```

[child ⬇️](#e7131f24-8d71-40a0-b483-6b63a6a3f184)

---

(other branch ⎇)
###### e7131f24-8d71-40a0-b483-6b63a6a3f184
[parent ⬆️](#b868be6e-d1b4-48d9-87d7-0a038be88429)
