# Assistant

{
  "file_id": "aacf3eb0-48c4-4f60-ba99-3bb3015acb26",
  "source": [
    "# Create a Panel widget for the slider\n",
    "time_slider = pn.widgets.IntSlider(name='Time Step', start=0, end=n_points-1, step=1, value=0)\n",
    "\n",
    "# Function to update the plot based on the slider\n",
    "def update_plot(event):\n",
    "    current_time = time_slider.value\n",
    "    sc.set_offsets(np.c_[x[:current_time+1], y[:current_time+1]])\n",
    "    plt.draw()\n",
    "\n",
    "# Attach the update function to the slider\n",
    "time_slider.param.watch(update_plot, 'value')\n",
    "\n",
    "# Create Panel layout and display\n",
    "layout = pn.Column(time_slider, pn.pane.Matplotlib(fig))\n",
    "layout.servable()"
  ],
  "cell_type": "code",
  "and_run": true
}

[child ⬇️](#ee36a5ef-1dc7-4f9c-b179-e12464e80627)

---

(main branch ⎇)
###### ee36a5ef-1dc7-4f9c-b179-e12464e80627
[parent ⬆️](#b8adf63d-b670-4f70-97cf-4af1db868dd0)
