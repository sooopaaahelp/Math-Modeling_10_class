import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation 
fig,ax=plt.subplots()
anime,=plt.plot([],[],marker='0', color='r')
def cikl(R,t):
    x=R*(t-np.sin(t))
    y=R*(1-np.cos(t))
    return x,y
def astr (R, t):
    x=R*np.cos(t)**3
    y=R*np.sin(t)**3
    return x,y
ax.set_xlim(-5,100)
ax.set_ylim(-10,100)
def animat(i):
    anime.set_data(astr(1, i))
    anime.set_data(cikl(1, i))
ani=FuncAnimation(fig,
                  animat,
                  frames=100,
                  interval=300)
ani.save('anime_0.gif')
        