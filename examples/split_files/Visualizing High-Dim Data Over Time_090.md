# Assistant

{
  "file_id": "d9e7a4e0-3a9f-4d5a-9f7b-2d4e0f4f0c5e",
  "cell_id": "generate_synthetic_data",
  "source": [
    "import random\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
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
  "and_run": true
}

[child ⬇️](#6997dea5-66c0-451f-8e80-cf000c3cb893)

---

(main branch ⎇)
###### 6997dea5-66c0-451f-8e80-cf000c3cb893
[parent ⬆️](#0f0c72a9-993a-4da8-afd4-dc64c48ca9f2)
