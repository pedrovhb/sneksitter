# Function to generate semi-random synthetic data with branching
def generate_branching_data(n_points, n_branches):
    data = {'x': [], 'y': [], 'branch': []}
    x, y = 0, 0
    for i in range(n_points):
        for j in range(n_branches):
            dx, dy = np.random.randn(), np.random.randn()
            new_x, new_y = x + dx, y + dy
            data['x'].append(new_x)
            data['y'].append(new_y)
            data['branch'].append(j)
        x, y = new_x, new_y
    return data

