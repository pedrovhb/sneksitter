# Tool

```python
{'next_state': '\n        Get the next parse state. Combine this with\n        [`lookahead_iterator`](Language.lookahead_iterator) to\n        generate completion suggestions or valid symbols in error nodes.\n        ',
 'field_name_for_id': 'Get the name of the field for the given numerical id.',
 'lookahead_iterator': '\n        Create a new lookahead iterator for this language and parse state.\n\n        This returns `None` if state is invalid for this language.\n\n        Iterating `LookaheadIterator` will yield valid symbols in the given\n        parse state. Newly created lookahead iterators will return the `ERROR`\n        symbol from `LookaheadIterator.current_symbol`.\n\n        Lookahead iterators can be useful to generate suggestions and improve\n        syntax error diagnostics. To get symbols valid in an ERROR node, use the\n        lookahead iterator on its first leaf node state. For `MISSING` nodes, a\n        lookahead iterator created on the previous non-extra leaf node may be\n        appropriate.\n        '}
```

[child ⬇️](#a977dc7f-83c5-402b-9c99-f27d287568a5)

---

(main branch ⎇)
###### a977dc7f-83c5-402b-9c99-f27d287568a5
[parent ⬆️](#853a1fb2-23ab-404d-aac4-35a12bf2dc27)
