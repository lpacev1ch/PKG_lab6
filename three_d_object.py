import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def create_letter_A():
    vertices = np.array([
        [0, 0, 0], [1, 0, 0], [1, 2, 0], [0, 2, 0],  # Bottom rectangle
        [0.5, 1, 0], [0.5, 1.5, 0],  # Inner A bar
    ])
    
    edges = [
        [vertices[0], vertices[1], vertices[2], vertices[3]],
        [vertices[0], vertices[1], vertices[4]],
        [vertices[1], vertices[2], vertices[5]],
    ]
    
    return vertices, edges

def plot_3d(vertices, edges):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    for edge in edges:
        ax.add_collection3d(Poly3DCollection([edge], facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
    
    ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], c='r', marker='o')
    plt.show()

vertices, edges = create_letter_A()
plot_3d(vertices, edges)
