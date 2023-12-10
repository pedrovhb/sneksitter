---
file: /home/pedro/Documents/chatgpt_export/Markdown/Visualización de velocidad en mapa de pista.md
heading_stack: <root> -> 78e04d7c-a1af-446f-8b7d-dce4ea62bb0e -> System -> 5c500c9e-5861-4d6b-b085-4ff313388901 -> System -> aaa2f7d7-fe29-46a2-bcb1-effe5e4a42cc -> User -> First, we define some variables that allow us to conveniently control what -> we want to plot. -> Next, we load the session and select the desired data. -> Get telemetry data -> Now, we create a set of line segments so that we can color them -> individually. This creates the points as a N x 1 x 2 array so that we can -> stack points  together easily to get the segments. The segments array for -> line collection needs to be (numlines) x (points per line) x 2 (for x and y) -> After this, we can actually plot the data. -> We create a plot with title and adjust some setting to make it look good. -> Adjust margins and turn of axis -> After this, we plot the data itself. -> Create background track line -> Create a continuous norm to map from data points to colors -> Set the values used for colormapping
---
# Set the values used for colormapping
lc.set_array(color)

