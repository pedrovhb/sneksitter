---
file: /home/pedro/Documents/chatgpt_export/Markdown/Initialize Python Parser & Language.md
heading_stack: <root> -> 7deaf15e-dcb4-475b-bbae-9fde5f9b50d7 -> System -> 5a6cae08-3bad-4a1b-92fc-266c59c03560 -> System -> aaa2ddfa-521c-405d-b9e3-227ffc2bcaac -> User -> 6d8915d9-494c-4acc-8597-98c9519f6c8f -> Assistant -> 4aca064a-e9f9-44da-95a8-6f7790f3618d -> Tool -> 07a91a45-2df0-4247-a7c5-eed4c1d80d2b -> Assistant -> a2864381-72df-4235-b645-de3388a504fd -> Assistant -> 5241b676-ecc5-41db-bbd9-f39e12b4d5a1 -> Tool -> b69e85ff-b1d6-4f22-bd95-b04a7e6ce8ee -> Assistant -> 1ebaf51c-ef90-4949-b253-25e3ee987df6 -> Tool -> 381527fc-babd-4be9-969a-d2ebed211701 -> Assistant -> f601a97e-f099-45d4-be5f-598badf44a95 -> Assistant -> 83fd203e-51af-4b0c-81a1-92af3cbedb35 -> Tool -> Initialize the Python parser -> Initialize the Python language -> 84085495-982f-479e-8504-be9132565200 -> Assistant -> 112ef432-f042-4644-8473-d144a0323889 -> Tool -> Initialize the Python parser -> Initialize the Python language -> 22effdc1-4c81-4317-91f1-b4bd610aa167 -> Assistant -> aaa2384a-7544-4fc6-8884-faf486622cf7 -> User -> 15e08f20-977e-499c-bfea-715ce1340cc0 -> Assistant -> fa9b0b83-b196-476f-b7ab-5bf63b9791f9 -> Tool -> f1156b46-ce25-4151-91fa-5a8141140ed2 -> Assistant -> f91742da-795a-4e45-9cf6-bf02109c0188 -> Tool -> 22676854-cd22-4df5-8f29-984c26bf0c71 -> Assistant -> aaa2fdf0-aa28-4ae5-a22c-078f41d33d1a -> User -> 7db55174-8c04-4801-b8e1-84002b6ddfaa -> Assistant -> a61ef022-1744-476d-8329-9c9411e7a815 -> Tool -> Sample Python code to parse -> Parse the sample code -> Populate the graph from the parsed tree -> c1d5451e-6317-4afb-9720-e520d2a9785f -> Assistant -> abd939df-a4e5-4f2c-8d25-4b8e518e0494 -> Assistant
---
# Assistant

{
  "file_id": "99f2106d-9319-41f8-b8ed-8dce97f756ef",
  "cell_type": "code",
  "source": [
    "def populate_graph_from_tree(tree, graph=None, parent=None):",
    "    if graph is None:",
    "        graph = nx.DiGraph()",
    "    \n",
    "    cursor = tree.walk()",
    "    \n",
    "    def _traverse(cursor, parent):",
    "        node_id = id(cursor.node)",
    "        graph.add_node(node_id, type=cursor.node.type)",
    "        \n",
    "        if parent is not None:",
    "            edge_attrs = {}",
    "            if hasattr(cursor, 'current_field_name') and cursor.current_field_name:",
    "                edge_attrs['field_name'] = cursor.current_field_name",
    "            graph.add_edge(parent, node_id, **edge_attrs)",
    "        \n",
    "        if cursor.goto_first_child():",
    "            _traverse(cursor, node_id)",
    "            while cursor.goto_next_sibling():",
    "                _traverse(cursor, node_id)",
    "        cursor.goto_parent()",
    "    \n",
    "    _traverse(cursor, parent)",
    "    return graph"
  ],
  "and_run": true
}

[child ⬇️](#d5796adb-2f66-48ac-87fa-bf75a1fa6415)

---

(main branch ⎇)
###### d5796adb-2f66-48ac-87fa-bf75a1fa6415
[parent ⬆️](#abd939df-a4e5-4f2c-8d25-4b8e518e0494)