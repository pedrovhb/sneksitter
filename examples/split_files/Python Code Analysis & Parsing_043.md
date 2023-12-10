# Assistant

{
  "file_id": "1239fdfa-f7ef-4d30-9dbb-5f6f61637677",
  "cell_type": "code",
  "source": [
    "# Test the Function model with a sample function parsed by tree_sitter",
    "from tree_sitter import Language, Parser",
    "\n",
    "# Load the Python language parser",
    "Language.build_library('build/my-languages.so', ['tree-sitter-python'])",
    "PYTHON_LANGUAGE = Language('build/my-languages.so', 'python')",
    "parser = Parser()",
    "parser.set_language(PYTHON_LANGUAGE)",
    "\n",
    "# Sample Python function",


---

(main branch ⎇)
###### b9f81089-4c76-418f-8750-210c56227b66
[parent ⬆️](#aaa29624-745c-4d6f-afdf-2a7394441c24)
