# Assistant

{
  "file_id": "1239fdfa-f7ef-4d30-9dbb-5f6f61637677",
  "cell_type": "code",
  "and_run": true,
  "source": [
    "# Fixing the TypeError by ensuring all elements are strings",
    "def reconstruct_function(function: Function) -> str:",
    "    parameter_strs = []",
    "    for param in function.parameters:",
    "        param_str = param.name",
    "        if param.type:",
    "            param_str += f': {param.type}'",
    "        if param.default:",
    "            param_str += f' = {param.default.decode(\"utf-8\")}'",
    "        parameter_strs.append(param_str)",
    "    parameters = ', '.join(parameter_strs)",
    "    \n",
    "    return_type = f' -> {function.return_type.decode(\"utf-8\")}' if function.return_type else ''",
    "    docstring = f'\"\"\"{function.docstring.decode(\"utf-8\")}\"\"\"' if function.docstring else ''",
    "    body = function.body.decode('utf-8') if function.body else ''",
    "    \n",
    "    return f'def {function.name}({parameters}){return_type}:' + '\\n' + docstring + '\\n' + body",
    "\n",
    "# Test the reconstruction method",
    "reconstructed_code = reconstruct_function(parsed_function)",
    "print(reconstructed_code)"
  ]
}

[child ⬇️](#991cfbc3-7f47-44e5-9069-8ea6481923ba)

---

(main branch ⎇)
###### 991cfbc3-7f47-44e5-9069-8ea6481923ba
[parent ⬆️](#10c79000-b2ba-45fd-828c-f425da5bc856)
