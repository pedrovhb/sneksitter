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

[child ⬇️](#0984e606-f068-488f-8e66-be8faa5e434f)

---

(main branch ⎇)
###### 0984e606-f068-488f-8e66-be8faa5e434f
[parent ⬆️](#a61846b8-a985-4822-90f9-542a675ed326)
