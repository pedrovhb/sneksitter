---
file: /home/pedro/Documents/chatgpt_export/Markdown/Explore Python Syntax Graphviz.md
heading_stack: <root> -> 5d11d6a6-248f-4f42-87c7-2cfeefdc5887 -> System -> 68c39207-346e-47cf-8c4c-5f153f2ac305 -> System -> aaa27992-bb31-4d04-9962-3478d816a032 -> User
---
# User

Please set up the environment and explore the syntax of Python by creating a graphviz visualizations with interfaces such as -

[1]: from tree_sitter_languages import get_language

In [2]: lang = get_language("python")

In [3]: lang.lookahead_iterator?
Signature: lang.lookahead_iterator(state: int) -> Optional[tree_sitter.LookaheadIterator]
Docstring:
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
File:      ~/.cache/pypoetry/virtualenvs/codecranker-plugin-bovwu0sq-py3.10/lib/python3.10/site-packages/tree_sitter/__init__.py
Type:      method

In [4]: lang.next_state?
Signature: lang.next_state(state: int, id: int) -> int
Docstring:
Get the next parse state. Combine this with
[`lookahead_iterator`](Language.lookahead_iterator) to
generate completion suggestions or valid symbols in error nodes.
File:      ~/.cache/pypoetry/virtualenvs/codecranker-plugin-bovwu0sq-py3.10/lib/python3.10/site-packages/tree_sitter/__init__.py
Type:      method

In [5]: lang.field_name_for_id(1)
Out[5]: 'alias'

In [6]: lang.node_kind_for_id(1)
Out[6]: 'identifier'
In [8]: [(lang.field_name_for_id(l), lang.node_kind_for_id(l))
   ...:  for l in lang.lookahead_iterator(1)]
Out[8]:

[
    (None, 'end'),
    ('alias', 'identifier'),
    ('argument', 'import'),
    ('attribute', 'from'),
    ('cause', '('),
    ('definition', '*'),
    ('function', 'print'),
    ('key', 'assert'),
    ('module_name', 'match'),
    ('name', 'return'),
    ('object', 'del'),
    ('operator', 'raise'),
    ('operators', 'pass'),
    ('parameters', 'break'),
    ('pattern', 'continue'),
    ('return_type', 'if'),
    ('type', 'async'),
    ('value', 'for'),
    (None, 'while'),
    (None, 'try'),
    (None, 'with'),
    (None, 'def'),
    (None, 'global'),
...

(Note the import from tree_sitter_languages, not the usual ts)

[child ⬇️](#b6e4ecf9-36bd-4820-af58-e4a9f1f5464f)

---

(main branch ⎇)
###### b6e4ecf9-36bd-4820-af58-e4a9f1f5464f
[parent ⬆️](#aaa27992-bb31-4d04-9962-3478d816a032)
