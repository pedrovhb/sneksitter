---
file: /home/pedro/Documents/chatgpt_export/Markdown/Visualizing High-Dim Data Over Time.md
heading_stack: <root> -> e110a479-ffc2-4603-acbd-8237df32e573 -> System -> 7809300d-2e24-4429-a8c5-1f29ad85f9b2 -> System -> aaa2edfe-1989-493a-b69e-725783a32255 -> User -> 234b6612-41b7-4bfd-8027-9ecdc361bb01 -> Assistant -> 1. Animated Scatter Plots -> 2. Parallel Coordinates -> 3. Radial Layouts -> 4. Heatmaps -> 5. Glyph-based Techniques -> 6. Contour Plots -> 7. Network Graphs -> 8. Dimensionality Reduction + Animation -> 9. Small Multiples -> 10. Interactive Sliders -> aaa22307-4fa3-446b-9c7f-3f0538f60a97 -> User -> f81c7bf5-9c63-4fea-a261-1ea9c74b7383 -> Assistant -> d1413c97-d50f-47ea-9c76-d74385d4606a -> Tool -> 9251f206-140d-42e0-b72c-441a67c48571 -> Assistant -> a2b7a96f-23c0-479e-a50c-88c49ffb6591 -> Tool -> f4171e67-0150-49f1-b7ab-8bb4db769da2 -> Assistant -> 4fdeae90-3b2f-459b-b5e3-878449789bb4 -> Assistant -> 49e42c0c-e493-4cec-9f46-86bd9ae45623 -> Tool -> 6dca96a7-4149-4f6b-8daa-0d1770f1e42b -> Assistant -> 87ae73a2-ed65-4827-9f73-8575518cde36 -> Tool -> b8b87e10-ed55-407b-8cf7-9a293091d5bc -> Assistant -> 91b3c3b2-7d21-4d58-9cd3-1794186263b0 -> Tool -> 4d48d409-b039-4710-a14f-02fc6c931f17 -> Assistant -> a3e9a1cd-aadb-46bc-b082-86d15a475628 -> Assistant -> af4dac37-61a9-4cc8-bc37-a2235be2a318 -> Tool -> Generate synthetic data -> Initialize the plot -> Update function for animation -> Create animation -> 38688101-5119-4b30-91a2-7d76437b00d4 -> Assistant -> aaa2f7e6-af87-490e-83ff-d24cae0d9c3f -> User -> ce478bcc-f11c-4cf2-ba62-3e81532f092b -> Assistant -> 76f8b881-69fa-4fab-8a88-7d1c058c7956 -> Tool -> 2b0ba511-bf76-40e6-a620-05917852811e -> Assistant -> 4e398860-deca-47d8-bed1-ff4841b8b1bf -> Tool -> b8adf63d-b670-4f70-97cf-4af1db868dd0 -> Assistant -> ee36a5ef-1dc7-4f9c-b179-e12464e80627 -> Tool -> Create a Panel widget for the slider -> Function to update the plot based on the slider -> Attach the update function to the slider -> Create Panel layout and display -> 8cbd6d53-a6ce-468d-8884-51b5622a982a -> Assistant -> aaa224c0-ae2d-44ce-a88f-091366dfd296 -> User -> 995b5533-9e30-42f0-8f04-79f17247305f -> Assistant -> 89fc1077-a36b-4caa-9a14-aa5e3ff53678 -> Assistant -> 8d9c34f1-81cf-4f03-9bed-8f5c7888eaeb -> Tool -> Function to generate semi-random synthetic data with branching -> Generate the data -> a43f4cd5-3207-467e-a1bd-6e53490b88aa -> Assistant -> aaa27efc-c28c-43f2-aeaf-4582a914d51e -> User -> 0f0c72a9-993a-4da8-afd4-dc64c48ca9f2 -> Assistant -> 6997dea5-66c0-451f-8e80-cf000c3cb893 -> Tool -> e022d770-834e-41a4-b000-63b502ef8e34 -> Assistant -> 8df274c4-d73c-4596-afe7-822731180cd8 -> Tool -> Function to generate more synthetic data with multiple branches -> Generate synthetic data -> Dataframe Summary -> Column Information -> Categorical Summary -> Sample Data (5x4) -> d78d0ccf-f48f-46f4-a1c4-82b5b5c96057 -> Assistant -> aaa26ac7-7b6c-498e-8514-34764ad576bb -> User -> 1684cd7d-5505-4299-a1a7-624beb9f404b -> Assistant -> 20f6c19a-4a19-4670-9777-1cdcd6e5581f -> Tool -> Function to update the plot based on the slider and new data -> Initialize the plot -> Create a Panel widget for the slider -> Create Panel layout and display -> 9fbd9773-2a04-481d-8173-13908049342d -> Assistant -> aaa26888-b2c7-45e0-8b49-c93ebceab32e -> User -> 27a6f62b-9c54-4e65-bda8-ad9758e8fd3b -> Assistant -> aaa27178-8852-4701-a636-5e272aa2af8f -> User -> ca6cf67b-cf6b-4bfb-b60c-2b1330b9d4d6 -> Assistant -> b5ac7335-0af8-46f0-a941-ffe9138b112a -> Tool -> Generate synthetic data -> Initialize the plot -> Update function for animation -> Create animation
---
# Create animation
ani = FuncAnimation(fig, update, frames=range(n_points), blit=True)
plt.show()
== Output ==
Embed: ![](https://app.noteable.io/gate/api/o/73594df8-a407-4102-9131-402036bbedb6.png)


==== Cell ID: 3cbccc0c-0336-4efe-af4c-21a48ebbc407
Cell Type: code
Cell State: finished_with_no_error
== Source ==
!pip install -q panel

==== Cell ID: 35aa700f-d7fc-469b-9a2d-18a8eeaee673
Cell Type: code
Cell State: finished_with_no_error
== Source ==
import panel as pn
pn.extension()
== Output ==
Output text was too long to stream back, user can view it in the UI

==== Cell ID: 2064f39c-f0e8-4ae7-ba36-c168a8042ff4
Cell Type: code
Cell State: finished_with_no_error
== Source ==
