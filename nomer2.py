import matplotlib.pyplot as plt
import numpy as np
from numpy  import sin, cos
t=np.arange(-2*np.pi, 2*np.pi, 0.1)
R=5.5
x=R*(cos(t))**3
y=R*(sin(t))**3
plt.xlim(-20,20)
plt.ylim(-20,20)
plt.plot(x,y)
plt.show()