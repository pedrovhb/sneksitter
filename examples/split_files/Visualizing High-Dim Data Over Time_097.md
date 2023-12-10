# Function to generate more synthetic data with multiple branches
def generate_synthetic_data(n_points=200, n_branches=5):
    data = []
    for branch in range(n_branches):
        x, y = 0, 0
        for point in range(n_points):
            dx, dy = random.uniform(-1, 1), random.uniform(-1, 1)
            x += dx
            y += dy
            data.append({'x': x, 'y': y, 'time': point, 'branch': branch})
    return pd.DataFrame(data)

