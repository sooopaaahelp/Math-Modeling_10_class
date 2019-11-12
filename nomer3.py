import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation 
fig,ax=plt.subplots()
anime,=plt.plot([],[],marker='o', color='r')
def cikl(R,t):
    x=R*(t-np.sin(t))
    y=R*(1-np.cos(t))
    return x,y
def astr (R, t):
    x=R*np.cos(t)**3
    y=R*np.sin(t)**3
    return x,y
ax.set_xlim(-2*np.pi,2*np.pi)
ax.set_ylim(-2*np.pi,2*np.pi)
def animat(i):
    anime.set_data(astr(3, i))

ani=FuncAnimation(fig,
                  animat,
                  frames=np.arange(-2*np.pi,2*np.pi,0.1),
                  interval=300)
ani.save('anime_0.gif')
        