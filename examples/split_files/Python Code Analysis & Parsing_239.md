# Assistant

{
  "file_id": "1239fdfa-f7ef-4d30-9dbb-5f6f61637677",
  "cell_type": "code",
  "and_run": true,
  "source": [
    "# Fixing the SyntaxError by properly escaping quotes inside f-strings",
    "def reconstruct_function(function: Function) -> str:",
    "    parameter_strs = []",
    "    for param in function.parameters:",
    "        param_str = param.name.decode('utf-8')",
    "        if param.type:",
    "            param_str += f': {param.type.decode(\"utf-8\")}'",
    "        if param.default:",
    "            param_str += f' = {param.default.decode(\"utf-8\")}'",
    "        parameter_strs.append(param_str)",
    "    parameters = ', '.join(parameter_strs)",
    "    \n",
    "    return_type = f' -> {function.return_type.decode(\"utf-8\")}' if function.return_type else ''",
    "    docstring = f'\"\"\"{function.docstring.decode(\"utf-8\")}\"\"\"' if function.docstring else ''",
    "    body = function.body.decode('utf-8') if function.body else ''",
    "    \n",
    "    return f'def {function.name.decode(\"utf-8\")}({parameters}){return_type}:' + '\\n' + docstring + '\\n' + body",
    "\n",
    "# Test the reconstruction method",
    "reconstructed_code = reconstruct_function(parsed_function)",
    "print(reconstructed_code)"
  ]
}

[child ⬇️](#7c370c83-c811-47d0-b83a-af62d04f5715)

---

(main branch ⎇)
###### 7c370c83-c811-47d0-b83a-af62d04f5715
[parent ⬆️](#ab7f5bf4-2319-450a-a2d9-0b878778f4ca)
