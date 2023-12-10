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

[child ⬇️](#bbbccfcc-3c77-4250-8aaa-eb36e219c74f)

---

(main branch ⎇)
###### bbbccfcc-3c77-4250-8aaa-eb36e219c74f
[parent ⬆️](#852834df-3c42-4961-afeb-c3521c594fbb)
