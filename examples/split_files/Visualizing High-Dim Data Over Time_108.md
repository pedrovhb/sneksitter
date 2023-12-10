# Assistant

{
  "file_id": "aacf3eb0-48c4-4f60-ba99-3bb3015acb26",
  "source": [
    "# Function to update the plot based on the slider and new data\n",
    "def update_plot(event):\n",
    "    current_time = time_slider.value\n",
    "    filtered_data = synthetic_data[synthetic_data['time'] <= current_time]\n",
    "    sc.set_offsets(filtered_data[['x', 'y']].values)\n",
    "    sc.set_array(filtered_data['branch'].values)\n",
    "    plt.draw()\n",
    "\n",
    "# Initialize the plot\n",
    "fig, ax = plt.subplots()\n",
    "sc = ax.scatter([], [], c=[], cmap='viridis')\n",
    "\n",
    "# Create a Panel widget for the slider\n",
    "time_slider = pn.widgets.IntSlider(name='Time Step', start=0, end=200, step=1, value=0)\n",
    "time_slider.param.watch(update_plot, 'value')\n",
    "\n",
    "# Create Panel layout and display\n",
    "layout = pn.Column(time_slider, pn.pane.Matplotlib(fig))\n",
    "layout.servable()"
  ],
  "cell_type": "code",
  "and_run": true
}

[child ⬇️](#20f6c19a-4a19-4670-9777-1cdcd6e5581f)

---

(main branch ⎇)
###### 20f6c19a-4a19-4670-9777-1cdcd6e5581f
[parent ⬆️](#1684cd7d-5505-4299-a1a7-624beb9f404b)
