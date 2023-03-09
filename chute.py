# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 05:34:29 2021

@author: DECLINE
"""

import numpy as np
import matplotlib.pyplot as plt



g=9.80665
v0=np.linspace(10,24,6)
theta=85
h=0
plt.figure(1,dpi=300)
for j in range(len(v0)):
    
    y=[]
    y0=h
    i=0
    while y0>=0:
        i+=0.01
        y0=-1/2*(g/v0[j]**2)*(i**2)*(1+np.tan(theta*np.pi/180)**2)+i*np.tan(theta*np.pi/180)+h
        if y0>=0:
            y.append(y0)
    x=np.linspace(0,i,len(y))
    plt.plot(x,y,label=str('v0 = '+str(v0[j]))+' m/s')
    plt.title('Free fall')
    plt.xlabel('time (s)')
    plt.ylabel('height (m)')
    plt.legend()