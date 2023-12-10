# Create animation
ani = FuncAnimation(fig, update, frames=range(n_points), blit=True)
plt.show()
== Output ==
Embed: ![](https://app.noteable.io/gate/api/o/73594df8-a407-4102-9131-402036bbedb6.png)


==== Cell ID: 3cbccc0c-0336-4efe-af4c-21a48ebbc407
Cell Type: code
Cell State: finished_with_no_error
== Source ==
!pip install -q panel

==== Cell ID: 35aa700f-d7fc-469b-9a2d-18a8eeaee673
Cell Type: code
Cell State: finished_with_no_error
== Source ==
import panel as pn
pn.extension()
== Output ==
Output text was too long to stream back, user can view it in the UI

==== Cell ID: 2064f39c-f0e8-4ae7-ba36-c168a8042ff4
Cell Type: code
Cell State: finished_with_no_error
== Source ==
