---
file: /home/pedro/Documents/chatgpt_export/Markdown/Visualizing High-Dim Data Over Time.md
heading_stack: <root> -> e110a479-ffc2-4603-acbd-8237df32e573 -> System -> 7809300d-2e24-4429-a8c5-1f29ad85f9b2 -> System -> aaa2edfe-1989-493a-b69e-725783a32255 -> User -> 234b6612-41b7-4bfd-8027-9ecdc361bb01 -> Assistant -> 1. Animated Scatter Plots -> 2. Parallel Coordinates -> 3. Radial Layouts -> 4. Heatmaps -> 5. Glyph-based Techniques -> 6. Contour Plots -> 7. Network Graphs -> 8. Dimensionality Reduction + Animation -> 9. Small Multiples -> 10. Interactive Sliders -> aaa22307-4fa3-446b-9c7f-3f0538f60a97 -> User -> f81c7bf5-9c63-4fea-a261-1ea9c74b7383 -> Assistant -> d1413c97-d50f-47ea-9c76-d74385d4606a -> Tool -> 9251f206-140d-42e0-b72c-441a67c48571 -> Assistant -> a2b7a96f-23c0-479e-a50c-88c49ffb6591 -> Tool -> f4171e67-0150-49f1-b7ab-8bb4db769da2 -> Assistant -> 4fdeae90-3b2f-459b-b5e3-878449789bb4 -> Assistant -> 49e42c0c-e493-4cec-9f46-86bd9ae45623 -> Tool -> 6dca96a7-4149-4f6b-8daa-0d1770f1e42b -> Assistant -> 87ae73a2-ed65-4827-9f73-8575518cde36 -> Tool -> b8b87e10-ed55-407b-8cf7-9a293091d5bc -> Assistant -> 91b3c3b2-7d21-4d58-9cd3-1794186263b0 -> Tool -> 4d48d409-b039-4710-a14f-02fc6c931f17 -> Assistant -> a3e9a1cd-aadb-46bc-b082-86d15a475628 -> Assistant -> af4dac37-61a9-4cc8-bc37-a2235be2a318 -> Tool -> Generate synthetic data -> Initialize the plot -> Update function for animation -> Create animation -> 38688101-5119-4b30-91a2-7d76437b00d4 -> Assistant -> aaa2f7e6-af87-490e-83ff-d24cae0d9c3f -> User -> ce478bcc-f11c-4cf2-ba62-3e81532f092b -> Assistant -> 76f8b881-69fa-4fab-8a88-7d1c058c7956 -> Tool -> 2b0ba511-bf76-40e6-a620-05917852811e -> Assistant -> 4e398860-deca-47d8-bed1-ff4841b8b1bf -> Tool -> b8adf63d-b670-4f70-97cf-4af1db868dd0 -> Assistant -> ee36a5ef-1dc7-4f9c-b179-e12464e80627 -> Tool -> Create a Panel widget for the slider -> Function to update the plot based on the slider -> Attach the update function to the slider -> Create Panel layout and display -> 8cbd6d53-a6ce-468d-8884-51b5622a982a -> Assistant -> aaa224c0-ae2d-44ce-a88f-091366dfd296 -> User -> 995b5533-9e30-42f0-8f04-79f17247305f -> Assistant -> 89fc1077-a36b-4caa-9a14-aa5e3ff53678 -> Assistant
---
# Assistant

{
  "file_id": "aacf3eb0-48c4-4f60-ba99-3bb3015acb26",
  "source": [
    "# Function to generate semi-random synthetic data with branching\n",
    "def generate_branching_data(n_points, n_branches):\n",
    "    data = {'x': [], 'y': [], 'branch': []}\n",
    "    x, y = 0, 0\n",
    "    for i in range(n_points):\n",
    "        for j in range(n_branches):\n",
    "            dx, dy = np.random.randn(), np.random.randn()\n",
    "            new_x, new_y = x + dx, y + dy\n",
    "            data['x'].append(new_x)\n",
    "            data['y'].append(new_y)\n",
    "            data['branch'].append(j)\n",
    "        x, y = new_x, new_y\n",
    "    return data\n",
    "\n",
    "# Generate the data\n",
    "branching_data = generate_branching_data(50, 2)\n",
    "branching_data"
  ],
  "cell_type": "code",
  "and_run": true
}

[child ⬇️](#8d9c34f1-81cf-4f03-9bed-8f5c7888eaeb)

---

(main branch ⎇)
###### 8d9c34f1-81cf-4f03-9bed-8f5c7888eaeb
[parent ⬆️](#89fc1077-a36b-4caa-9a14-aa5e3ff53678)
