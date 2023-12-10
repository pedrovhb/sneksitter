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

[child ⬇️](#1212270f-c102-4519-962f-5fd0a77512dc)

---

(main branch ⎇)
###### 1212270f-c102-4519-962f-5fd0a77512dc
[parent ⬆️](#c649201f-1195-41af-be28-44c1bc8fadbf)
