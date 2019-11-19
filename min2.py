import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
fig=plt.figure()

N_x=np.linspace(-5,5,100)
N_y=2*N_x**2+2*N_x+4

anim_list=[]
for i in range(0,100,1):
    anim_object,=plt.plot(N_x[i],N_y[i],'o',color='r')
    anim_list.append([anim_object])
ani = ArtistAnimation(fig, anim_list, interval=50) 
ani.save ('ani.gif')   
    

