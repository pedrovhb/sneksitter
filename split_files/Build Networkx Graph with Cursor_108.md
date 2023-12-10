---
file: /home/pedro/Documents/chatgpt_export/Markdown/Build Networkx Graph with Cursor.md
heading_stack: <root> -> 9454ce70-1f14-454c-b6d4-dc8e17388ae1 -> System -> cdc1e4df-6ed9-4474-aa70-316fd1d37354 -> System -> aaa2cfbd-357a-4571-8976-96badef48d18 -> User -> 660d2f56-57b7-4db7-a86f-6e27fd55def8 -> Assistant -> aaa2f53f-301b-417c-b7ee-ff3a213ff44f -> User -> f88bf305-bb2b-49d3-8c39-93884f395670 -> Assistant -> d19608c1-cf76-442e-8eab-86807320e37d -> Tool -> 6cb2143c-6833-483e-81c3-0d5c2c20c84a -> Assistant -> 51b0898f-7e88-4c13-b0c8-bbb7f8e79c51 -> Assistant -> fb7ae9bc-bb46-4c32-94d3-47dc0b2b5997 -> Tool -> e5bdaef0-5f8e-4822-829f-4a51aeb66212 -> Assistant -> ea55d543-5d28-4b1c-b826-048e5193a24e -> Assistant -> e11edf56-3f99-4581-a686-28205d3be656 -> Tool -> aaa2e899-d049-4567-ab73-9a0e30522e4a -> User -> e1eb96c2-6182-4f3d-9618-2090742a1ed5 -> Assistant -> 7ef60a9c-7eed-44d5-aa0f-3d90f7804b36 -> Tool -> 15b380ed-29fa-4b8e-91d1-18b9badf7375 -> Assistant -> 63125128-93cd-4245-85ed-4eb855b0d5d9 -> Tool -> 28322e40-fbc3-4697-b889-7bfc1cbd6646 -> Assistant -> aaa255bd-d556-491e-8170-56c47b45a097 -> User -> 320c67ff-0dfb-4c38-b56e-34468a3d105e -> Assistant -> afd3d6ea-3a9c-438a-9953-a86948012f11 -> Tool -> 607cc351-d587-4de9-8b81-48f78baa6808 -> Assistant -> 32520129-56ad-4b4c-aa5c-70a535c8d810 -> Tool -> 12bc79e2-6ccb-4f09-9cb2-4fa39aae46de -> Assistant -> 22aec5e1-4da7-49b8-8f82-256fcf4a7ac6 -> Assistant -> faa4b10f-1700-4da1-9d1a-92c8719a53cc -> Tool -> e10976ff-6dfc-4df1-bd25-e3e4eec6241a -> Assistant -> e0c0ab3e-0cba-4dcf-9ec0-3d480613825d -> Tool -> 1d103013-56f3-4295-9547-11bef7cac8b9 -> Assistant -> aaa262dc-9989-484c-b5ab-bdbc4e761f45 -> User -> cdbb92c6-377f-421a-b673-0bdfea10504f -> Assistant -> f76c5d36-6a88-44a7-b955-65eae7dbef08 -> Tool -> 9bd2af72-9be2-483d-b788-68d422a1f433 -> Assistant -> dcfc9cf8-8c16-419a-a476-65daf2156b3c -> Assistant -> 8c1d94ee-4c46-4273-a873-c859316d0ad4 -> Tool -> a9b8b5ac-12ca-451a-be14-5d5aa1e6a6a9 -> Assistant -> aaa27046-aa7d-42b1-bda5-49edff9ef608 -> User -> d3ca0b62-1b60-4edd-820b-0376f55b4896 -> Assistant -> e1a86ecb-1e50-4d6b-9ea2-06390d9446e9 -> Tool -> 7c36299d-8af3-4e2c-83d7-5c7f5ae46a85 -> Assistant -> aaa233bc-fd2f-4faf-b551-50ef9a41d783 -> User -> c4d619a2-5669-46f9-b948-50e49398f1c1 -> Assistant -> 1e0c0e07-80ab-4b21-838c-7df360a7e7c8 -> Tool -> 69ca6803-f43d-4d8a-9b79-a665cf2d0964 -> Assistant -> f33c840c-59c8-4d1e-8df8-77183cd953a0 -> Assistant -> 2c9a88bd-a70f-4c0d-9169-dc26079bfb73 -> Tool -> 6cb6c862-79a5-4da9-a5aa-1ef86261f6a8 -> Assistant -> df41959c-33c6-4fbc-a9a7-a55a70874aff -> Assistant -> aaa243d4-390a-4862-8109-5f7362392f42 -> User -> 3c2c8c23-6b76-4a71-99b8-2ed2fa1bf114 -> Assistant -> 54e5c197-56c2-4cf1-8477-95b874b2b4eb -> Tool -> b830fd78-f106-47c5-bde8-7035cbe92411 -> Assistant -> feeb1ccc-5e41-42e9-8845-3fbac9a4e49a -> Assistant
---
# Assistant

```python
# Convert NetworkX node IDs to strings to match Pydot's behavior
G_node_id_str = nx.relabel_nodes(G_node_id, {node: str(node) for node in G_node_id.nodes()})

# Convert to Pydot for visualization
pydot_graph_node_id_str = to_pydot(G_node_id_str)
pydot_graph_node_id_str.set('rankdir', 'TB')
pydot_graph_node_id_str.set('concentrate', True)
pydot_graph_node_id_str.set_node_defaults(shape='box', style='rounded')

# Add labels
for node in pydot_graph_node_id_str.get_nodes():
    node.set_label(G_node_id_str.nodes[node.get_name().strip('"')]['label'])

# Generate a visualization
png_image_node_id_str = pydot_graph_node_id_str.create_png(prog='dot')

# Display the image
image_node_id_str = Image.open(BytesIO(png_image_node_id_str))
display(image_node_id_str)
```

[child ⬇️](#9d1018db-d191-45cb-9435-73ed55044396)

---

(main branch ⎇)
###### 9d1018db-d191-45cb-9435-73ed55044396
[parent ⬆️](#feeb1ccc-5e41-42e9-8845-3fbac9a4e49a)
