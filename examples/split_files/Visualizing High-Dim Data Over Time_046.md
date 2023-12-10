# Assistant

{
  "file_id": "aacf3eb0-48c4-4f60-ba99-3bb3015acb26",
  "source": [
    "# Generate synthetic data\n",
    "np.random.seed(0)\n",
    "n_points = 50\n",
    "x = np.cumsum(np.random.randn(n_points))\n",
    "y = np.cumsum(np.random.randn(n_points))\n",
    "\n",
    "# Initialize the plot\n",
    "fig, ax = plt.subplots()\n",
    "sc = ax.scatter([], [])\n",
    "\n",
    "# Update function for animation\n",
    "def update(frame):\n",
    "    sc.set_offsets(np.c_[x[:frame+1], y[:frame+1]])\n",
    "    return sc,\n",
    "\n",
    "# Create animation\n",
    "ani = FuncAnimation(fig, update, frames=range(n_points), blit=True)\n",
    "plt.show()"
  ],
  "cell_type": "code",
  "and_run": true
}

[child ⬇️](#af4dac37-61a9-4cc8-bc37-a2235be2a318)

---

(main branch ⎇)
###### af4dac37-61a9-4cc8-bc37-a2235be2a318
[parent ⬆️](#a3e9a1cd-aadb-46bc-b082-86d15a475628)
