import matplotlib.pyplot as plt
import numpy as np


g=9.80665
v0=np.linspace(10,24,6)     #m/s
theta=85                    #deg
x0=0
y0=0
h=0.01
r=21.35e-3
Cx=0.45
rho=1.3
S=np.pi*r**2
Ff=1/2*Cx*rho*S

""" #laminaire
eta=0.018e-3
k=6*pi*eta*r
"""

for i in v0:
    
    x=x0
    y=y0
    t=0
    vx=i*np.cos(theta*np.pi/180)
    vy=i*np.sin(theta*np.pi/180)
    
    xlist=[]
    ylist=[]
    
    k=0
    
    while y>=0:
        x=x+vx*h
        y=y+vy*h
        t=t+h
        vx=vx-Ff*h*vx**2
        vy=vy-h*(g+Ff*vy**2)
    
        xlist.append(x)
        ylist.append(y)
    
        k+=1
    
    plt.title('Free fall')
    plt.plot(xlist, ylist,label=str('v0 = '+str(i))+' m/s')
    plt.xlabel('time (s)')
    plt.ylabel('height (m)')
    plt.legend()
