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
