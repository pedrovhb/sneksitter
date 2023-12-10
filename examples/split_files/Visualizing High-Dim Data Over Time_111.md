# Function to update the plot based on the slider and new data
def update_plot(event):
    current_time = time_slider.value
    filtered_data = synthetic_data[synthetic_data['time'] <= current_time]
    sc.set_offsets(filtered_data[['x', 'y']].values)
    sc.set_array(filtered_data['branch'].values)
    plt.draw()

