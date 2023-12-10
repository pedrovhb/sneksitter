# Tool

```python
(['sql_stmt_list',
  'ABORT',
  'ACTION',
  'ADD',
  'AFTER',
  'ALL',
  'ALTER',
  'ALWAYS',
  'ANALYZE',
  'AND'],
 [{'type': 'SEQ',
   'members': [{'type': 'CHOICE',
     'members': [{'type': 'SYMBOL', 'name': 'sql_stmt'}, {'type': 'BLANK'}]},
    {'type': 'REPEAT',
     'content': {'type': 'SEQ',
      'members': [{'type': 'STRING', 'value': ';'},
       {'type': 'CHOICE',
        'members': [{'type': 'SYMBOL', 'name': 'sql_stmt'},
         {'type': 'BLANK'}]}]}}]}])
```

[child ⬇️](#18640d90-4b55-4261-8724-cda538740a88)

---

(main branch ⎇)
###### 18640d90-4b55-4261-8724-cda538740a88
[parent ⬆️](#c10c55e3-10ed-493c-b42f-70b822c66364)
