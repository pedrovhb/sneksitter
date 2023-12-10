---
file: /home/pedro/Documents/chatgpt_export/Markdown/Advanced Graphviz Features Demo.md
heading_stack: <root> -> b6f0250c-2c29-48e9-9697-052895061fac -> System -> c0382b3d-5622-418c-82c6-9718652426a2 -> System -> aaa25ba6-dd5e-4b1d-a80b-8cfeb32cd076 -> User -> 2dfbde17-251d-4960-802d-72d431931ba2 -> Assistant -> aaa29eee-17fd-487c-9deb-9b0f300cc79d -> User -> 899b2696-4470-4399-bbbf-d405265e6076 -> Assistant -> 1. Cluster Subgraphs -> aaa2a038-fe85-4b61-ac93-315b624f7960 -> User -> 247dcca5-8dcd-41d5-99b5-0f9c27db63cd -> Assistant -> 9a45f68f-3816-4a98-9de0-66386b0eb41d -> Tool -> 1c9f4085-df27-4ed2-bfd8-547cd8e5e1e2 -> Assistant -> aaa27f58-1e05-4376-b04e-3e4cacc7d472 -> User -> 3be2e9af-c5c5-49aa-8a0b-8ad2b0f975b6 -> Assistant -> 5111d7fb-a43d-460d-bed5-a40ddc510dc8 -> Tool -> 50b0868d-0be4-447b-a431-af11411e85e8 -> Assistant -> aaa2d875-c964-4e5d-a5b3-2ebbbdafad2a -> User -> b92aec5b-e020-4ae3-8ff0-0974f1614b07 -> Assistant -> 49a3bc25-0285-4ece-b65d-ce82f416f859 -> Tool -> ef91a623-a39f-4548-b0ad-48f0b5c96030 -> Assistant -> aaa2c84d-8fc9-4e41-b1a1-fe4a3eada151 -> User -> 23c6542f-8569-4f57-b2be-e524ad5ccd3d -> Assistant -> a5919e32-7b77-40d0-b209-b614fb566858 -> Tool -> 745c5813-312a-4906-9321-b0fe412a7b76 -> Assistant -> aaa21b4b-34b3-45c4-96f0-53f36b37d583 -> User -> 8e144ddf-3c9f-4599-a480-e8830fb235f9 -> Assistant -> 3839d5f4-f3d7-4162-8533-4101ce44fa43 -> Tool -> 1cf12e0f-14a2-4fee-a61f-2cd969ff35a1 -> Assistant -> aaa2d8fa-6d82-4a65-8fdd-90f2c097a310 -> User -> eb70e0da-e84f-450f-91ab-5d177513a2da -> Assistant -> aaa20318-635e-412b-b4e2-6a63f688d7d9 -> User -> 90db216e-2a39-45cb-8765-ee389c0e1183 -> Assistant
---
# Assistant

```python
# Initialize DOT string for the example combining all advanced features
dot_combined = """
digraph G {
  // Clusters
  subgraph cluster_0 {
    label="Cluster 0";
    style=filled;
    color=lightgrey;
    a0 -> a1 [id=edge1, label="Solid", style=solid];
    a1 -> a2 [id=edge2, label="Dashed", style=dashed];
    a2 -> a3 [id=edge3, label="Dotted", style=dotted];
  }
  subgraph cluster_1 {
    label="Cluster 1";
    color=blue;
    b0 -> b1 -> b2 -> b3;
  }

  // Nodes and Edges
  start [shape=Mdiamond, label=<<FONT POINT-SIZE="24">Start</FONT>>];
  end [shape=Msquare, label=<<I>End</I>>];
  
  // Directed and Undirected Edges
  start -> a0;
  start -> b0;
  a1 -> b3;
  b2 -> a3;
  a3 -> a0;
  a3 -> end;
  b3 -> end;
  a3 -> b2 [constraint=false];
}

"""
# Render the graph in different layouts
layouts = ['dot', 'neato', 'twopi', 'circo', 'fdp']

# Generate the images
images = []
for layout in layouts:
    output_file = f"/mnt/data/combined_example_{layout}.png"
    graph = pgv.AGraph(string=dot_combined)
    graph.layout(prog=layout)
    graph.draw(output_file)
    images.append(Image(output_file))

images
```

[child ⬇️](#f52d810e-d9c3-406f-942d-d4f1e6a1b038)

---

(main branch ⎇)
###### f52d810e-d9c3-406f-942d-d4f1e6a1b038
[parent ⬆️](#90db216e-2a39-45cb-8765-ee389c0e1183)
