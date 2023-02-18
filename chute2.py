import matplotlib.pyplot as plt
from math import cos, sin, pi


g=9.80665
v=24
alpha=60
x0=0
y0=0
h=0.01
r=21.35e-3
Cx=0.45
rho=1.3
S=pi*r**2
Ff=1/2*Cx*rho*S

""" #laminaire
eta=0.018e-3
k=6*pi*eta*r
"""


x=x0
y=y0
t=0
vx=v*cos(alpha*pi/180)
vy=v*sin(alpha*pi/180)


xlist=[]
ylist=[]

i=0

while y>=0:
    x=x+vx*h
    y=y+vy*h
    t=t+h
    vx=vx-Ff*h*vx**2
    vy=vy-h*(g+Ff*vy**2)

    xlist.append(x)
    ylist.append(y)

    i=i+1


plt.title('Chute libre')

plt.plot(xlist, ylist, 'c', linewidth=3,linestyle=':')

plt.show()
