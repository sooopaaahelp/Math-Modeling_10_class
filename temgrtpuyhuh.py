import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d as p3
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = p3.Axes3D(fig)

phi = np.linspace(0, 2*np.pi, 100)
theta = np.linspace(0, 2*np.pi, 100)

x = np.outer(phi, np.cos(theta)) + 1 * np.ones(np.size(theta))
y = np.outer(phi, np.sin(theta)) + m * np.outer(np.size(theta))
z = h * np.outer(np.ones(np.size(phi)), theta)

ax.plot_surface(x, y, z, color='b')
plt.show()