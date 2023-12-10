# Assistant

{
  "file_id": "1239fdfa-f7ef-4d30-9dbb-5f6f61637677",
  "cell_type": "code",
  "and_run": true,
  "source": [
    "# Re-run the test for the Function model using the existing parser object",
    "tree = parser.parse(bytes(test_code, 'utf8'))",
    "root_node = tree.root_node",
    "function_node = [n for n in root_node.children if n.type == 'function_definition'][0]",
    "\n",
    "parsed_function = Function.from_node(function_node)",
    "parsed_function.dict()"
  ]
}

[child ⬇️](#4d468123-cf5b-4e33-8917-3ec219ef5cc3)

---

(main branch ⎇)
###### 4d468123-cf5b-4e33-8917-3ec219ef5cc3
[parent ⬆️](#8d1dee8c-f6e2-4f2d-bcee-5ae6fcbc0fa6)
