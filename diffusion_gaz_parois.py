# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 20:32:11 2023

@author: DECLINE
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.text import TextPath
from matplotlib.markers import MarkerStyle
import matplotlib.animation as animation

n = 500 # Number of particules
L = 10  # Lenght of the box
dt = 0.01  # Time step
v = 3  # Average velocity
m = 1  # Particule mass
sigma = 1e-3  # Distribution density

x = np.random.randn(n)*sigma+L/2
y = np.random.randn(n)*sigma+L/2
vx = np.random.randn(n)*v
vy = np.random.randn(n)*v

heart = TextPath((0, 0), "♥")
h = MarkerStyle(heart)
sun = TextPath((0, 0), "☀")
s = MarkerStyle(sun)
star = TextPath((0, 0), "★")
st = MarkerStyle(star)

col = []
"""
for i in range(n):
    if np.sqrt(vx[i]**2+vy[i]**2)<2:
        col.append('#fcfce8')
    elif np.sqrt(vx[i]**2+vy[i]**2)<3:
        col.append('#ededaf')
    elif np.sqrt(vx[i]**2+vy[i]**2)<4:
        col.append('#ffff00')
    elif np.sqrt(vx[i]**2+vy[i]**2)<5:
        col.append('#f2d307')
    elif np.sqrt(vx[i]**2+vy[i]**2)<6:
        col.append('#ffc108')
    else:
        col.append('#ffa808')
        
"""
for i in range(n):
    if np.sqrt(vx[i]**2+vy[i]**2)<1:
        col.append('#6f00ff')
    elif np.sqrt(vx[i]**2+vy[i]**2)<2:
        col.append('#0400ff')
    elif np.sqrt(vx[i]**2+vy[i]**2)<3:
        col.append('#14fbff')
    elif np.sqrt(vx[i]**2+vy[i]**2)<4:
        col.append('#0feb07')
    elif np.sqrt(vx[i]**2+vy[i]**2)<5:
        col.append('#fbff00')
    elif np.sqrt(vx[i]**2+vy[i]**2)<6:
        col.append('orange')
    else:
        col.append('r')

fig, ax = plt.subplots(facecolor='black')
scat = ax.scatter(x, y, s=500, c=col, marker=st)

def update_positions(x, y, vx, vy, L, dt):
    x += vx*dt
    y += vy*dt

    for i in range(n):
        if x[i]<0 or x[i]>L:
            vx[i] = -vx[i]
        if y[i]<0 or y[i]>L:
            vy[i] = -vy[i]
    
    return x, y, vx, vy

def animate(frame):
    global x, y, vx, vy
    x, y, vx, vy = update_positions(x, y, vx, vy, L, dt)
    scat.set_offsets(np.c_[x, y])
    scat.set_color(col)
    return scat,

ax.set_axis_off()
plt.xlim(0, L)
plt.ylim(0, L)
ani = animation.FuncAnimation(fig, animate, frames=400, interval=5, blit=True)
#ani.save('bigbang.gif', writer='imagemagick', fps=60)
plt.show()