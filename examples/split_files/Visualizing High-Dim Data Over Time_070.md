# Function to update the plot based on the slider
def update_plot(event):
    current_time = time_slider.value
    sc.set_offsets(np.c_[x[:current_time+1], y[:current_time+1]])
    plt.draw()

