---
file: /home/pedro/Documents/chatgpt_export/Markdown/Advanced Graphviz Features Demo.md
heading_stack: <root> -> b6f0250c-2c29-48e9-9697-052895061fac -> System -> c0382b3d-5622-418c-82c6-9718652426a2 -> System -> aaa25ba6-dd5e-4b1d-a80b-8cfeb32cd076 -> User -> 2dfbde17-251d-4960-802d-72d431931ba2 -> Assistant -> aaa29eee-17fd-487c-9deb-9b0f300cc79d -> User -> 899b2696-4470-4399-bbbf-d405265e6076 -> Assistant -> 1. Cluster Subgraphs -> aaa2a038-fe85-4b61-ac93-315b624f7960 -> User -> 247dcca5-8dcd-41d5-99b5-0f9c27db63cd -> Assistant
---
# Assistant

```python
# Importing the pygraphviz library to work with graphviz in Python
import pygraphviz as pgv
from IPython.display import Image

# Function to render a graph from DOT format to PNG
def render_dot(dot_string, output_file):
    graph = pgv.AGraph(string=dot_string)
    graph.layout(prog='dot')
    graph.draw(output_file)
    return Image(output_file)

# Initialize DOT string for the first example: Cluster Subgraphs
dot_cluster = """
digraph G {
  subgraph cluster_0 {
    label="Cluster 0";
    style=filled;
    color=lightgrey;
    a0 -> a1 -> a2 -> a3;
  }
  subgraph cluster_1 {
    label="Cluster 1";
    color=blue;
    b0 -> b1 -> b2 -> b3;
  }
  start -> a0;
  start -> b0;
  a1 -> b3;
  b2 -> a3;
  a3 -> a0;
  a3 -> end;
  b3 -> end;

  start [shape=Mdiamond];
  end [shape=Msquare];
}
"""
# Render the graph
render_dot(dot_cluster, "/mnt/data/cluster_example.png")
```

[child ⬇️](#9a45f68f-3816-4a98-9de0-66386b0eb41d)

---

(main branch ⎇)
###### 9a45f68f-3816-4a98-9de0-66386b0eb41d
[parent ⬆️](#247dcca5-8dcd-41d5-99b5-0f9c27db63cd)
