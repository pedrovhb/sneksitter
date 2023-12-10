# Create a Panel widget for the slider
time_slider = pn.widgets.IntSlider(name='Time Step', start=0, end=200, step=1, value=0)
time_slider.param.watch(update_plot, 'value')

