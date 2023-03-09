# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 02:43:08 2023

@author: DECLINE
"""
import matplotlib.pyplot as plt
import numpy as np

g=9.81
m=0.1 # kg
rho=1.2
Cd=0.47
A=np.pi*(0.02**2)
v0=np.linspace(10,24,6)
theta=85


def forces(v, y):
    Fg=m*g                   # gravity
    Fd=0.5*rho*Cd*A*v**2     # drag
    Fy=-Fg-Fd                # total
    return Fy


def trajectoire(v0, theta):
    vx=v0*np.cos(theta*np.pi/180)
    vy=v0*np.sin(theta*np.pi/180)
    x,y= [0],[0]
    dt=0.001
    while y[-1]>=0:
        v=np.sqrt(vx**2 + vy**2)
        Fd=0.5*rho*Cd*A*v**2
        Fy=forces(v, y[-1])
        ax=-Fd/m*np.cos(np.arctan2(vy, vx))
        ay=Fy/m
        vx+=ax*dt
        vy+=ay*dt
        x.append(x[-1]+vx*dt)
        y.append(y[-1]+vy*dt)
    return x, y


for i in v0:
    
    x,y=trajectoire(i,theta)
    plt.plot(x,y,label=str('v0 = '+str(i))+' m/s')
plt.xlabel('Distance (m)')
plt.ylabel('Hauteur (m)')
plt.title('Trajectory in free fall with air resistance')
plt.legend()
plt.show()