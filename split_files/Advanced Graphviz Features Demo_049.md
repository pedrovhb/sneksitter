---
file: /home/pedro/Documents/chatgpt_export/Markdown/Advanced Graphviz Features Demo.md
heading_stack: <root> -> b6f0250c-2c29-48e9-9697-052895061fac -> System -> c0382b3d-5622-418c-82c6-9718652426a2 -> System -> aaa25ba6-dd5e-4b1d-a80b-8cfeb32cd076 -> User -> 2dfbde17-251d-4960-802d-72d431931ba2 -> Assistant -> aaa29eee-17fd-487c-9deb-9b0f300cc79d -> User -> 899b2696-4470-4399-bbbf-d405265e6076 -> Assistant -> 1. Cluster Subgraphs -> aaa2a038-fe85-4b61-ac93-315b624f7960 -> User -> 247dcca5-8dcd-41d5-99b5-0f9c27db63cd -> Assistant -> 9a45f68f-3816-4a98-9de0-66386b0eb41d -> Tool -> 1c9f4085-df27-4ed2-bfd8-547cd8e5e1e2 -> Assistant -> aaa27f58-1e05-4376-b04e-3e4cacc7d472 -> User -> 3be2e9af-c5c5-49aa-8a0b-8ad2b0f975b6 -> Assistant -> 5111d7fb-a43d-460d-bed5-a40ddc510dc8 -> Tool -> 50b0868d-0be4-447b-a431-af11411e85e8 -> Assistant -> aaa2d875-c964-4e5d-a5b3-2ebbbdafad2a -> User -> b92aec5b-e020-4ae3-8ff0-0974f1614b07 -> Assistant -> 49a3bc25-0285-4ece-b65d-ce82f416f859 -> Tool -> ef91a623-a39f-4548-b0ad-48f0b5c96030 -> Assistant -> aaa2c84d-8fc9-4e41-b1a1-fe4a3eada151 -> User -> 23c6542f-8569-4f57-b2be-e524ad5ccd3d -> Assistant -> a5919e32-7b77-40d0-b209-b614fb566858 -> Tool -> 745c5813-312a-4906-9321-b0fe412a7b76 -> Assistant -> aaa21b4b-34b3-45c4-96f0-53f36b37d583 -> User -> 8e144ddf-3c9f-4599-a480-e8830fb235f9 -> Assistant
---
# Assistant

```python
# Initialize DOT string for the fifth example: HTML-like Labels
dot_html_labels = """
digraph G {
  node1 [label=<<TABLE><TR><TD>Cell 1</TD><TD>Cell 2</TD></TR></TABLE>>];
  node2 [label=<<FONT POINT-SIZE="24">Large Font</FONT>>];
  node3 [label=<<I>Italic</I>>];

  node1 -> node2 -> node3;
}
"""
# Render the graph
render_dot(dot_html_labels, "/mnt/data/html_labels_example.png")
```

[child ⬇️](#3839d5f4-f3d7-4162-8533-4101ce44fa43)

---

(main branch ⎇)
###### 3839d5f4-f3d7-4162-8533-4101ce44fa43
[parent ⬆️](#8e144ddf-3c9f-4599-a480-e8830fb235f9)
