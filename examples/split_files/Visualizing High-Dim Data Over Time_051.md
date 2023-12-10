# Update function for animation
def update(frame):
    sc.set_offsets(np.c_[x[:frame+1], y[:frame+1]])
    return sc,

