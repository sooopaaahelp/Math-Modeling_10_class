from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.gca(projection='3d')

phi = np.linspace(0, 2 * np.pi, 100)
theta = np.linspace(0, np.pi, 100)

x = 10 * np.outer(np.cos(phi), np.cos(theta))
y = 10 * np.outer(np.cos(phi), np.sin(theta))
z = np.outer((phi)**2)
ax.plot_suface(x, y, z, color='b')
plt.show()