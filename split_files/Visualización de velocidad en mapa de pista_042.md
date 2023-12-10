---
file: /home/pedro/Documents/chatgpt_export/Markdown/Visualización de velocidad en mapa de pista.md
heading_stack: <root> -> 78e04d7c-a1af-446f-8b7d-dce4ea62bb0e -> System -> 5c500c9e-5861-4d6b-b085-4ff313388901 -> System -> aaa2f7d7-fe29-46a2-bcb1-effe5e4a42cc -> User -> First, we define some variables that allow us to conveniently control what -> we want to plot. -> Next, we load the session and select the desired data. -> Get telemetry data -> Now, we create a set of line segments so that we can color them -> individually. This creates the points as a N x 1 x 2 array so that we can -> stack points  together easily to get the segments. The segments array for -> line collection needs to be (numlines) x (points per line) x 2 (for x and y) -> After this, we can actually plot the data. -> We create a plot with title and adjust some setting to make it look good. -> Adjust margins and turn of axis -> After this, we plot the data itself. -> Create background track line -> Create a continuous norm to map from data points to colors -> Set the values used for colormapping -> Merge all line segments together -> Finally, we create a color bar as a legend. -> Show the plot -> b927de9a-7f9a-4aba-8adf-f9e7b0133fbf -> Assistant -> c19ab3a1-77f1-4a7a-9182-2d92a1573eff -> Tool -> 2de8fe53-34d1-4446-9e7d-662b4f25807b -> Assistant -> 6ff0a0e5-121d-4355-b88d-70019241a78a -> Assistant -> 9c1df759-1b7c-4cfe-b8d4-a254b4687c45 -> Tool -> edef5e2a-f7a3-4c6f-8888-ceae0e7d3065 -> Assistant -> bb152ae4-06c9-42b7-9b29-13983eeecbfb -> Tool -> 1baca0b9-77dc-4feb-8d20-93bf3d732edd -> Assistant -> f2bbe088-c1ec-4063-becb-47b7c53fcded -> Assistant
---
# Assistant

{
  "file_id": "02803ead-5e04-4944-95f6-a54bc71a7d6d",
  "cell_type": "code",
  "source": [
    "# Define variables for the plot",
    "year = 2021",
    "wknd = 14",
    "ses = 'R'",
    "driver = 'HAM'",
    "colormap = mpl.cm.plasma",
    
    "# Load the session and select the desired data",
    "session = ff1.get_session(year, wknd, ses)",
    "weekend = session.event",
    "session.load()",
    "lap = session.laps.pick_driver(driver).pick_fastest()",
    
    "# Get telemetry data",
    "x = lap.telemetry['X']",
    "y = lap.telemetry['Y']",
    "color = lap.telemetry['Speed']",
    
    "# Create a set of line segments for individual coloring",
    "points = np.array([x, y]).T.reshape(-1, 1, 2)",
    "segments = np.concatenate([points[:-1], points[1:]], axis=1)",
    
    "# Create the plot",
    "fig, ax = plt.subplots(sharex=True, sharey=True, figsize=(12, 6.75))",
    "fig.suptitle(f'{weekend.name} {year} - {driver} - Speed', size=24, y=0.97)",
    "plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.12)",
    "ax.axis('off')",
    
    "# Plot the data",
    "ax.plot(lap.telemetry['X'], lap.telemetry['Y'], color='black', linestyle='-', linewidth=16, zorder=0)",
    "norm = plt.Normalize(color.min(), color.max())",
    "lc = LineCollection(segments, cmap=colormap, norm=norm, linestyle='-', linewidth=5)",
    "lc.set_array(color)",
    "line = ax.add_collection(lc)",
    
    "# Create a color bar as a legend",
    "cbaxes = fig.add_axes([0.25, 0.05, 0.5, 0.05])",
    "normlegend = mpl.colors.Normalize(vmin=color.min(), vmax=color.max())",
    "legend = mpl.colorbar.ColorbarBase(cbaxes, norm=normlegend, cmap=colormap, orientation='horizontal')",
    
    "# Show the plot",
    "plt.show()"
  ],
  "and_run": true
}

[child ⬇️](#276aa8fd-1749-48dc-a59f-b87b75a6f0b0)

---

(main branch ⎇)
###### 276aa8fd-1749-48dc-a59f-b87b75a6f0b0
[parent ⬆️](#f2bbe088-c1ec-4063-becb-47b7c53fcded)
