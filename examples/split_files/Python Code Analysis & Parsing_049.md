# Assistant

{
  "file_id": "1239fdfa-f7ef-4d30-9dbb-5f6f61637677",
  "cell_type": "code",
  "source": [
    "# Test the Function model using the existing parser object",
    "test_code = \"\"\"\n",
    "def example_function(param1: int, param2: str = 'default') -> None:\n",
    "    '''This is a docstring.'''\n",
    "    print(param1, param2)\n",
    "\"\"\"\n",
    "\n",
    "tree = parser.parse(bytes(test_code, 'utf8'))",
    "root_node = tree.root_node",
    "function_node = [n for n in root_node.children if n.type == 'function_definition'][0]",
    "\n",
    "parsed_function = Function.from_node(function_node)",
    "parsed_function.dict()"
  ]
}

[child ⬇️](#c20c6649-739b-4ec4-8885-46c3be7a10b1)

---

(main branch ⎇)
###### c20c6649-739b-4ec4-8885-46c3be7a10b1
[parent ⬆️](#bf43acdd-782e-46ef-9189-1ac85f454a68)
