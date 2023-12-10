# Create Panel layout and display
layout = pn.Column(time_slider, pn.pane.Matplotlib(fig))
layout.servable()
== Output ==
Column
    [0] IntSlider(end=49, name='Time Step')
    [1] Matplotlib(Figure)


==== Cell ID: 783ce84e-72eb-4dea-98b5-92a0b7214ed6
Cell Type: code
Cell State: finished_with_no_error
== Source ==
