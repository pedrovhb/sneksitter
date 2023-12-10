---
file: /home/pedro/Documents/chatgpt_export/Markdown/Advanced Graphviz Features Demo.md
heading_stack: <root> -> b6f0250c-2c29-48e9-9697-052895061fac -> System -> c0382b3d-5622-418c-82c6-9718652426a2 -> System -> aaa25ba6-dd5e-4b1d-a80b-8cfeb32cd076 -> User -> 2dfbde17-251d-4960-802d-72d431931ba2 -> Assistant -> aaa29eee-17fd-487c-9deb-9b0f300cc79d -> User -> 899b2696-4470-4399-bbbf-d405265e6076 -> Assistant -> 1. Cluster Subgraphs
---
### 1. Cluster Subgraphs

Cluster subgraphs allow you to group nodes together visually, often with a bounding box and label. They are prefixed with `subgraph cluster`.

Here's a simple example:

```dot
digraph G {
  // Define Nodes
  A [label="A"]
  B [label="B"]
  C [label="C"]
  D [label="D"]
  E [label="E"]

  // Define Edges
  A -> B
  B -> C
  D -> E

  // Cluster Subgraph
  subgraph cluster_1 {
    label = "Cluster 1";
    A -> B -> C;
  }

  subgraph cluster_2 {
    label = "Cluster 2";
    D -> E;
  }
}
```

Copy this DOT code into a file and run `dot -Tpng <filename.dot> -o output.png` to visualize the graph.

Would you like to proceed to the next feature?

---

(main branch ⎇)
###### aaa2a038-fe85-4b61-ac93-315b624f7960
[parent ⬆️](#2dfbde17-251d-4960-802d-72d431931ba2)
