---
file: /home/pedro/Documents/chatgpt_export/Markdown/Visualización de velocidad en mapa de pista.md
heading_stack: <root> -> 78e04d7c-a1af-446f-8b7d-dce4ea62bb0e -> System -> 5c500c9e-5861-4d6b-b085-4ff313388901 -> System -> aaa2f7d7-fe29-46a2-bcb1-effe5e4a42cc -> User -> First, we define some variables that allow us to conveniently control what -> we want to plot. -> Next, we load the session and select the desired data. -> Get telemetry data -> Now, we create a set of line segments so that we can color them -> individually. This creates the points as a N x 1 x 2 array so that we can -> stack points  together easily to get the segments. The segments array for -> line collection needs to be (numlines) x (points per line) x 2 (for x and y) -> After this, we can actually plot the data. -> We create a plot with title and adjust some setting to make it look good. -> Adjust margins and turn of axis -> After this, we plot the data itself. -> Create background track line -> Create a continuous norm to map from data points to colors -> Set the values used for colormapping -> Merge all line segments together -> Finally, we create a color bar as a legend. -> Show the plot -> b927de9a-7f9a-4aba-8adf-f9e7b0133fbf -> Assistant -> c19ab3a1-77f1-4a7a-9182-2d92a1573eff -> Tool -> 2de8fe53-34d1-4446-9e7d-662b4f25807b -> Assistant -> 6ff0a0e5-121d-4355-b88d-70019241a78a -> Assistant -> 9c1df759-1b7c-4cfe-b8d4-a254b4687c45 -> Tool -> edef5e2a-f7a3-4c6f-8888-ceae0e7d3065 -> Assistant -> bb152ae4-06c9-42b7-9b29-13983eeecbfb -> Tool -> 1baca0b9-77dc-4feb-8d20-93bf3d732edd -> Assistant -> f2bbe088-c1ec-4063-becb-47b7c53fcded -> Assistant -> 276aa8fd-1749-48dc-a59f-b87b75a6f0b0 -> Tool -> Define variables for the plot -> Load the session and select the desired data -> Get telemetry data -> Create a set of line segments for individual coloring -> Create the plot -> Plot the data -> Create a color bar as a legend -> Show the plot -> 6bc105d3-615d-429e-b477-567b9e114cd2 -> Assistant -> aaa29b67-daf6-42d4-9679-ac7ae525be35 -> User -> a0307879-dd50-4770-b718-38184779d7ef -> Assistant -> 7f898c30-18df-4cc9-afb5-da7dbf5bf042 -> Tool -> Import additional modules for analysis -> Load the session again to get data for all drivers -> Get lap data for all drivers -> Filter out laps that are not representative (e.g., in/out laps) -> Get the list of teams -> Initialize dictionaries to store speed ranges and sector times for each team -> Loop through each team to collect data -> Convert the collected data to DataFrames for easier analysis -> Sort the DataFrames
---
# Sort the DataFrames
df_speed_ranges = df_speed_ranges.sort_values(by='AvgSpeedRange', ascending=False)
df_sector_times = df_sector_times.sort_values(by=['Sector1', 'Sector2', 'Sector3'])
df_speed_ranges, df_sector_times
== Output ==
core           INFO     Loading data for Italian Grand Prix - Race [v3.1.2]                                             
req            INFO     Using cached data for session_info                                                              
req            INFO     Using cached data for driver_info                                                               
req            INFO     Using cached data for session_status_data                                                       
req            INFO     Using cached data for lap_count                                                                 
req            INFO     Using cached data for track_status_data                                                         
req            INFO     Using cached data for _extended_timing_data                                                     
req            INFO     Using cached data for timing_app_data                                                           
core           INFO     Processing timing data...                                                                       
req            INFO     Using cached data for car_data                                                                  
req            INFO     Using cached data for position_data                                                             
req            INFO     Using cached data for weather_data                                                              
req            INFO     Using cached data for race_control_messages                                                     
core           INFO     Finished loading data for 20 drivers: ['3', '4', '77', '16', '11', '55', '18', '14', '63', '31',
 '6', '5', '99', '88', '47', '9', '44', '33', '10', '22']
```
{ 'ename': 'TypeError',
  'evalue': 'Invalid comparison between dtype=timedelta64[ns] and str'}
```



[child ⬇️](#e2e15bbb-e42a-4af1-a938-65c4a470230a)

---

(main branch ⎇)
###### e2e15bbb-e42a-4af1-a938-65c4a470230a
[parent ⬆️](#7f898c30-18df-4cc9-afb5-da7dbf5bf042)
