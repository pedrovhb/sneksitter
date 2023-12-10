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

[child ⬇️](#e21695f3-3745-4434-ba96-4d32c8b5511e)

---

(main branch ⎇)
###### e21695f3-3745-4434-ba96-4d32c8b5511e
[parent ⬆️](#86ce0f65-7231-4632-8f2a-2903b5d0eb33)
