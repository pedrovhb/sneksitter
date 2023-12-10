# Assistant

{
  "file_id": "1239fdfa-f7ef-4d30-9dbb-5f6f61637677",
  "cell_type": "code",
  "and_run": true,
  "source": [
    "# Fixing the AttributeError by removing unnecessary decode calls",
    "def reconstruct_function(function: Function) -> str:",
    "    parameter_strs = []",
    "    for param in function.parameters:",
    "        param_str = param.name",
    "        if param.type:",
    "            param_str += f': {param.type}'",
    "        if param.default:",
    "            param_str += f' = {param.default}'",
    "        parameter_strs.append(param_str)",
    "    parameters = ', '.join(parameter_strs)",
    "    \n",
    "    return_type = f' -> {function.return_type}' if function.return_type else ''",
    "    docstring = f'\"\"\"{function.docstring}\"\"\"' if function.docstring else ''",
    "    body = function.body if function.body else ''",
    "    \n",
    "    return f'def {function.name}({parameters}){return_type}:' + '\\n' + docstring + '\\n' + body",
    "\n",
    "# Test the reconstruction method",
    "reconstructed_code = reconstruct_function(parsed_function)",
    "print(reconstructed_code)"
  ]
}

[child ⬇️](#5a29d225-7376-443d-a3da-d61d80dbedf9)

---

(main branch ⎇)
###### 5a29d225-7376-443d-a3da-d61d80dbedf9
[parent ⬆️](#d76f1615-9cad-4986-a824-82f84504a93d)
