# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 01:01:31 2022

@author: DECLINE
"""

import matplotlib.pyplot as plt
from math import sin, asin, pi

theta1=[i for i in range(0,91)]
n1=1.00026
n2=1.30

theta2=[]
theta3=[]
theta4=[]


for i in theta1:
    theta2.append((180/pi)*asin(sin(i*pi/180)*(n1/n2)))

#plt.plot(theta1,theta2)
#plt.xlabel('theta1')
#plt.ylabel('theta2')
#plt.xlim(0,90)
#plt.ylim(0,90)
#plt.show()

for i in theta2:
    theta3.append(60-i)

for i in theta3:
    if sin(i*pi/180)*(n2/n1)<1:
        theta4.append((180/pi)*asin(sin(i*pi/180)*(n2/n1)))
    else:
        theta4.append(0)

#plt.plot(theta1,theta4)
#plt.xlabel('theta1')
#plt.ylabel('theta4')
#plt.xlim(0,90)
#plt.ylim(0,90)
#plt.show()

halo22=[]
thetatot=[]
for i in range(len(theta4)):
    thetatot.append(theta1[i]+theta4[i]-60)
    halo22.append(22)

thetamin=[]
for i in range(len(theta4)):
    thetamin.append(min(thetatot[20:]))
    
plt.plot(theta1,thetatot,label="Angles possibles",color='m')
plt.plot(theta1,halo22,label="22°",c='c',linestyle='-.')
plt.plot(theta1,thetamin,label=round(thetamin[1],5),c='r',linestyle=':')
plt.xlabel('theta1')
plt.ylabel('theta4')
plt.title("Halo de 22°")
plt.legend()
plt.xlim(0,90)
plt.ylim(0,90)
plt.show()



##################################

alpha1=[]
alpha2=[]
alpha3=[]
alpha4=[]

alpha1=[i for i in range(0,91)]
for i in alpha1:
    alpha2.append((180/pi)*asin(sin(i*pi/180)*(n1/n2)))


for i in alpha2:
    alpha3.append(90-i)

for i in alpha3:
    if sin(i*pi/180)*(n2/n1)<1:
        alpha4.append((180/pi)*asin(sin(i*pi/180)*(n2/n1)))
    else:
        alpha4.append(0)

plt.plot(alpha1,alpha4)
plt.xlabel('alpha1')
plt.ylabel('alpha4')
plt.xlim(0,90)
plt.ylim(0,90)
plt.show()


halo46=[]
alphatot=[]
for i in range(len(alpha4)):
    alphatot.append(alpha1[i]-alpha4[i])
    halo46.append(46)
plt.plot(alpha1,alphatot,label="Angles possibles",color='m')
plt.plot(alpha1,halo46,label="46°",c='c',linestyle=':')
plt.xlabel('alpha1')
plt.ylabel('alpha4')
plt.title("Halo de 46°")
plt.legend()
plt.xlim(0,90)
plt.ylim(0,90)
plt.show()