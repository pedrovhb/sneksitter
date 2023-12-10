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

[child ⬇️](#3aca2368-9fa3-4c73-a9d7-1a195ceca202)

---

(main branch ⎇)
###### 3aca2368-9fa3-4c73-a9d7-1a195ceca202
[parent ⬆️](#c0b2fed6-0fe7-4952-a701-180e261cffd1)
