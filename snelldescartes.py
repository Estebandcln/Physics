# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 01:01:31 2022

@author: DECLINE
"""

import matplotlib.pyplot as plt
from math import sin, asin, pi


# 22° and 46° halos

n1=1.00026                         # air
n2=1.31                            # ice

# 22° halo

theta1=[i for i in range(0,91)]
theta2=[]
theta3=[]
theta4=[]

for i in theta1:
    theta2.append((180/pi)*asin(sin(i*pi/180)*(n1/n2)))

for i in theta2:
    theta3.append(60-i)

for i in theta3:
    if sin(i*pi/180)*(n2/n1)<1:
        theta4.append((180/pi)*asin(sin(i*pi/180)*(n2/n1)))
    else:
        theta4.append(0)

halo22=[]
thetatot=[]
for i in range(len(theta4)):
    if theta1[i]+theta4[i]-60<0:
        thetatot.append(0)
    else:
        thetatot.append(theta1[i]+theta4[i]-60)
    halo22.append(22)

thetamax=[]
thetamin=[]
maxi=0
mini=90
tmin=0
for i in range(len(thetatot)):
    if thetatot[i]!=0 and thetatot[i]<=mini:
        mini=thetatot[i]
    if thetatot[i]>=maxi:
        maxi=thetatot[i]

# Same length to plot
for i in range(len(thetatot)):
    thetamin.append(mini)
    thetamax.append(maxi)

# Incident angle for the first non null value
for i in range(len(thetatot)):
    if thetatot[i]!=0:
        tmin=theta1[i]
        break
        

plt.plot(theta1,thetatot,label="Possible angles",color='m')
plt.plot(theta1,halo22,label="22°",c='c',linestyle='-.')
plt.plot(theta1,thetamax,label=str(round(thetamax[0],4))+"°",c='k',linestyle=':')
plt.plot(theta1,thetamin,label=str(round(thetamin[0],4))+"°",c='r',linestyle=':')
plt.axvline(x=tmin,label="$theta_{i_{min}}$ = "+str(round(tmin,4))+"°",c='b',linestyle=':')
plt.xlabel('Incident angle')
plt.ylabel('Total angle')
plt.title("22° halo")
plt.legend()
plt.xlim(0,90)
plt.ylim(0,90)
plt.show()

# 46° halo

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
    if sin(i*pi/180)*(n2/n1)<1 and sin(i*pi/180)*(n2/n1)>-1:
        alpha4.append((180/pi)*asin(sin(i*pi/180)*(n2/n1)))
    else:
        alpha4.append(0)

halo46=[]
alphatot=[]
for i in range(len(alpha4)):
    if alpha1[i]+alpha4[i]-90<0:
        alphatot.append(0)
    else:
        alphatot.append(alpha1[i]+alpha4[i]-90)
    halo46.append(46)
    
alphamax=[]
alphamin=[]
maxi=0
mini=90
amin=0
for i in range(len(alphatot)):
    if alphatot[i]!=0 and alphatot[i]<=mini:
        mini=alphatot[i]
    if alphatot[i]>=maxi:
        maxi=alphatot[i]
        
# Same length to plot
for i in range(len(alphatot)):
    alphamin.append(mini)
    alphamax.append(maxi)
    
# Incident angle for the first non null value
for i in range(len(alphatot)):
    if alphatot[i]!=0:
        amin=alpha1[i]
        break

plt.plot(alpha1,alphatot,label="Possible angles",color='m')
plt.plot(alpha1,halo46,label="46°",c='c',linestyle='-.')
plt.plot(alpha1,alphamax,label=str(round(alphamax[0],4))+"°",c='k',linestyle=':')
plt.plot(alpha1,alphamin,label=str(round(alphamin[0],4))+"°",c='r',linestyle=':')
plt.axvline(x=amin,label="$alpha_{i_{min}}$ = "+str(round(amin,4))+"°",c='b',linestyle=':')
plt.xlabel('Incident angle')
plt.ylabel('Total angle '+str(chr(945)))
plt.title("46° halo")
plt.legend()
plt.xlim(0,90)
plt.ylim(0,90)
plt.show()

r22=(43.4383+21.8136)/2
w22=43.4383-21.8136
r46=(57.747+45.6613)/2
w46=57.747-45.6613

halo_22=plt.Circle((90,90),r22,color='c',fill=False,linewidth=w22)
halo_46=plt.Circle((90,90),r46,color='blue',fill=False,linewidth=w46)
sun=plt.Circle((90,90),5,color='gold')

fig, ax = plt.subplots()
ax.add_patch(halo_22)
ax.add_patch(halo_46)
ax.add_patch(sun)
ax.set_aspect('equal', adjustable='box')
plt.title("Both halos around the Sun")
plt.xlim(0,180)
plt.ylim(0,180)
plt.show()
