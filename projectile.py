# -*- coding: utf-8 -*-
"""
Created on Thu May 12 21:49:39 2022

@author: DECLINE
"""

import matplotlib.pyplot as plt
import numpy as np
'''

x0, y0, v0, theta0 = 0, 0, 200, 45
g=9.80665
mu=0.02
h=0.001
tlist=[]
ylist=[]

y=[0,0,np.cos(theta0)*v0,np.sin(theta0)*v0]
t=0
k1=[]
k2=[]
k3=[]
k4=[]
def f(y,t):
    return [y[2],y[3],-mu*y[2]*np.sqrt(y[2]**2+y[3]**2),-mu*y[3]*np.sqrt(y[2]**2+y[3]**2)-g]
while t<=10:
    t+=h

    for i in range(len(y)):
        k1=f(y,t)
        k2.append(f(y[i]+h*k1[i]/2,t+h/2))
        k3.append(f(y[i]+h*k2[i]/2,t+h/2))
        k4.append(f(y[i]+h*k3[i],t+h))
    y+=(h/6)*(k1+2*k2+2*k3+k4)
    tlist.append(t)
    ylist.append(y)
plt.figure(1)
plt.plot(tlist,ylist,c='b',linestyle=':')
plt.legend()

'''
t=0
x0,y0,v0,theta0=0,0,200,45
g=9.80665
mu=0.02
h=0.01
tlist=[]
ulist=[]

u=[0,0,np.cos(theta0)*v0,np.sin(theta0)*v0]
u1=u[0]
u2=u[1]
u3=u[2]
u4=u[3]

def f(u,t):
    return [u[2],u[3],-mu*u[2]*np.sqrt(u[2]**2+u[3]**2),-mu*u[3]*np.sqrt(u[2]**2+u[3]**2)-g]



while t<=10:
    t+=h
    k11=f(u,t)[0]
    k12=k11+h*k11/2
    k13=k12+h*k12/2
    k14=k13+h*k13/2
    
    k21=f(u,t)[1]
    k22=k21+h*k21/2
    k23=k22+h*k22/2
    k24=k23+h*k23/2
    
    k31=f(u,t)[2]
    k32=k31+h*k31/2
    k33=k32+h*k32/2
    k34=k33+h*k33/2
    
    k41=f(u,t)[3]
    k42=k41+h*k41
    k43=k42+h*k42
    k44=k43+h*k43
    
    u1+=(h/6)*(k11+2*k12+2*k13+k14)
    u2+=(h/6)*(k21+2*k22+2*k23+k24)
    u3+=(h/6)*(k31+2*k32+2*k33+k34)
    u4+=(h/6)*(k41+2*k42+2*k43+k44)
    u=[u1,u2,u3,u4]
    
    print(t,u)
    tlist.append(t)
    ulist.append(u)
plt.figure(1)
plt.plot(tlist,ulist)