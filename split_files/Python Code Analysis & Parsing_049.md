---
file: /home/pedro/Documents/chatgpt_export/Markdown/Python Code Analysis & Parsing.md
heading_stack: <root> -> 22b00ae7-9cb2-4df5-9eee-d07991dcb909 -> System -> 20ebaef2-02d6-4890-a642-e0f29f17805b -> System -> aaa2cafe-8b89-4a61-8a81-7ae5b849a3d4 -> User -> 9440ae93-53d9-4599-a08c-4f481da5db27 -> Assistant -> 57cd8fdb-661b-4e6a-89bc-77d3c8237b3f -> Tool -> 79181316-3c09-4844-8300-7e43ccd3f8a1 -> Assistant -> Cell 1 -> Cell 2 -> Observations: -> aaa2a124-a531-49d7-abf1-6bff71ae059e -> User -> f39d6ca7-8490-47d0-87ef-7295db56ee72 -> Assistant -> 4638e5fb-7316-4f3d-875b-e70772997c48 -> Tool -> c7d28657-3cf6-4f25-9465-6819041068f4 -> Assistant -> aaa21996-ce1a-4550-baea-bb77183194f1 -> User -> b2c70be9-2d0f-428b-be57-aef658e7da45 -> Assistant -> c4c27846-6e0a-47d8-8aab-ab14fbda0d8c -> Tool -> 56e7d34d-e69e-4f12-a83a-9bfce90dab6d -> Assistant -> aaa2d7f7-f073-4437-9fa5-f2e4d2fd83dd -> User -> 738131a3-930b-4da1-95c9-a56e3496cbea -> Assistant -> c88ab4d2-a949-405a-8f74-6e29ce5f2dfc -> Tool -> b6950cd6-4256-4e9b-9ab2-ca473b944965 -> Assistant -> aaa29624-745c-4d6f-afdf-2a7394441c24 -> User -> 8e63ce50-c453-4807-a071-c3cb79eb658b -> Assistant -> b9f81089-4c76-418f-8750-210c56227b66 -> Assistant -> aaa27d57-5c65-4afc-9489-d3fa7a6d1b5c -> User -> bf43acdd-782e-46ef-9189-1ac85f454a68 -> Assistant
---
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
