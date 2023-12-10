# Assistant

{
  "file_id": "1239fdfa-f7ef-4d30-9dbb-5f6f61637677",
  "cell_type": "code",
  "and_run": true,
  "source": [
    "# Fixing the TypeError by decoding param.name",
    "def reconstruct_function(function: Function) -> str:",
    "    parameter_strs = []",
    "    for param in function.parameters:",
    "        param_str = param.name.decode('utf-8')",
    "        if param.type:",
    "            param_str += f': {param.type.decode('utf-8')}'",
    "        if param.default:",
    "            param_str += f' = {param.default.decode('utf-8')}'",
    "        parameter_strs.append(param_str)",
    "    parameters = ', '.join(parameter_strs)",
    "    \n",
    "    return_type = f' -> {function.return_type.decode('utf-8')}' if function.return_type else ''",
    "    docstring = f'\"\"\"{function.docstring.decode('utf-8')}\"\"\"' if function.docstring else ''",
    "    body = function.body.decode('utf-8') if function.body else ''",
    "    \n",
    "    return f'def {function.name.decode('utf-8')}({parameters}){return_type}:' + '\\n' + docstring + '\\n' + body",
    "\n",
    "# Test the reconstruction method",
    "reconstructed_code = reconstruct_function(parsed_function)",
    "print(reconstructed_code)"
  ]
}

[child ⬇️](#ada7f916-430e-4b6c-9b3c-d2e0ed8345a9)

---

(main branch ⎇)
###### ada7f916-430e-4b6c-9b3c-d2e0ed8345a9
[parent ⬆️](#61be0dfc-54f7-40ec-a213-b7e0dbe90e6c)
