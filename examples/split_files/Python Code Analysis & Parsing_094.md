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

[child ⬇️](#51cb4061-e6af-44b2-a166-8f5743c955ed)

---

(main branch ⎇)
###### 51cb4061-e6af-44b2-a166-8f5743c955ed
[parent ⬆️](#02dc68b7-ca2f-49dd-bb6c-9316d2f77b27)
