import matplotlib.pyplot as plt

def visualize(grid, path, start, goal):
    plt.imshow(grid, cmap='gray_r')

    if path:
        x, y = zip(*path)
        plt.plot(y, x)

    plt.scatter(start[1], start[0], marker='o')
    plt.scatter(goal[1], goal[0], marker='x')

    plt.title("Autonomous Navigation")
    plt.show()