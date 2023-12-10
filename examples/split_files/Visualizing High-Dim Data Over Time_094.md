# Assistant

{
  "file_id": "aacf3eb0-48c4-4f60-ba99-3bb3015acb26",
  "source": [
    "import random\n",
    "import pandas as pd\n",
    "\n",
    "# Function to generate more synthetic data with multiple branches\n",
    "def generate_synthetic_data(n_points=200, n_branches=5):\n",
    "    data = []\n",
    "    for branch in range(n_branches):\n",
    "        x, y = 0, 0\n",
    "        for point in range(n_points):\n",
    "            dx, dy = random.uniform(-1, 1), random.uniform(-1, 1)\n",
    "            x += dx\n",
    "            y += dy\n",
    "            data.append({'x': x, 'y': y, 'time': point, 'branch': branch})\n",
    "    return pd.DataFrame(data)\n",
    "\n",
    "# Generate synthetic data\n",
    "synthetic_data = generate_synthetic_data()\n",
    "synthetic_data.head()"
  ],
  "cell_type": "code",
  "and_run": true
}

[child ⬇️](#8df274c4-d73c-4596-afe7-822731180cd8)

---

(main branch ⎇)
###### 8df274c4-d73c-4596-afe7-822731180cd8
[parent ⬆️](#e022d770-834e-41a4-b000-63b502ef8e34)
