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

# 22° halo (deflection through hexagonal column crystals' side faces with wedge angles of 60°)

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
maxi22=0
mini22=90
tmin=0
for i in range(len(thetatot)):
    if thetatot[i]!=0 and thetatot[i]<=mini22:
        mini22=thetatot[i]
    if thetatot[i]>=maxi22:
        maxi22=thetatot[i]

# Same length to plot
for i in range(len(thetatot)):
    thetamin.append(mini22)
    thetamax.append(maxi22)

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
plt.ylabel('Total angle '+str(chr(952)))
plt.title("22° halo")
plt.legend()
plt.xlim(0,90)
plt.ylim(0,90)
plt.show()

# 46° halo (rays traversing a side face and an end face of hexagonal column crystals)

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
maxi46=0
mini46=90
amin=0
for i in range(len(alphatot)):
    if alphatot[i]!=0 and alphatot[i]<=mini46:
        mini46=alphatot[i]
    if alphatot[i]>=maxi46:
        maxi46=alphatot[i]
        
# Same length to plot
for i in range(len(alphatot)):
    alphamin.append(mini46)
    alphamax.append(maxi46)
    
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

fig, ax = plt.subplots()

halo22_1=plt.Circle((90,90),mini22,color='c',fill=False)
halo22_2=plt.Circle((90,90),maxi22,color='c',fill=False)
halo46_1=plt.Circle((90,90),mini46,color='blue',fill=False)
halo46_2=plt.Circle((90,90),maxi46,color='blue',fill=False)
sun=plt.Circle((90,90),5,color='gold')

ax.add_patch(halo22_1)
ax.add_patch(halo22_2)
ax.add_patch(halo46_1)
ax.add_patch(halo46_2)
ax.add_patch(sun)
ax.set_aspect('equal', adjustable='box')
plt.title("Both halos around the Sun")
plt.xlim(0,180)
plt.ylim(0,180)
plt.show()

fig, ax = plt.subplots()

r22=(43.4383+21.8136)/2
#w22=43.4383-21.8136
r46=(57.747+45.6613)/2
#w46=57.747-45.6613

h22=plt.Circle((90,90),r22,color='c',fill=False,linewidth=28)
h46=plt.Circle((90,90),r46,color='blue',fill=False,linewidth=15)
sun=plt.Circle((90,90),5,color='gold')

ax.add_patch(h22)
ax.add_patch(h46)
ax.add_patch(sun)
ax.set_aspect('equal', adjustable='box')
plt.title("Both halos around the Sun")
plt.xlim(0,180)
plt.ylim(0,180)
plt.show()


# 120° parhelia (two internal hexagonal plate crystal reflections (two adjacent side faces))

beta1=[i for i in range(0,91)]
beta2=[]
beta3=[i for i in range(0,91)]
beta4=[]
beta5=[]
beta6=[]

for i in beta1:
    beta2.append((180/pi)*asin(sin(i*pi/180)*(n1/n2)))
    
for i in beta3:
    beta4.append(120-i)

for i in beta2:
    beta5.append(i)

for i in beta5:
    beta6.append((180/pi)*asin(sin(i*pi/180)*(n2/n1)))
    
halo120=[]
betatot=[]
for i in range(len(beta4)):
    betatot.append(beta3[i]+beta4[i]-60)
    halo120.append(120)
 
betamax=[]
betamin=[]
maxi120=0
mini120=90
bmin=0
for i in range(len(betatot)):
    if betatot[i]!=0 and betatot[i]<=mini120:
        mini120=betatot[i]
    if betatot[i]>=maxi120:
        maxi120=betatot[i]
        
# Same length to plot
for i in range(len(betatot)):
    betamin.append(mini120)
    betamax.append(maxi120)
    
# Incident angle for the first non null value
for i in range(len(betatot)):
    if betatot[i]!=0:
        bmin=beta1[i]
        break

plt.plot(beta1,betatot,label="Possible angles",color='m')
plt.plot(beta1,halo46,label="120°",c='c',linestyle='-.')
plt.plot(beta1,betamax,label=str(round(betamax[0],4))+"°",c='k',linestyle=':')
plt.plot(beta1,betamin,label=str(round(betamin[0],4))+"°",c='r',linestyle=':')
plt.axvline(x=bmin,label="$beta_{i_{min}}$ = "+str(round(bmin,4))+"°",c='b',linestyle=':')
plt.xlabel('Incident angle')
plt.ylabel('Total angle '+str(chr(945)))
plt.title("120° parhelia")
plt.legend()
plt.xlim(0,90)
plt.ylim(0,90)
plt.show()

#44° parhelia ("sundogs of sundogs" = double deflection in hexagonal plate crystals)

gamma1=[i for i in range(0,91)]
gamma2=[]
gamma3=[]
gamma4=[]

for i in gamma1:
    gamma2.append((180/pi)*asin(sin(i*pi/180)*(n1/n2)))
    
for i in gamma2:
    gamma3.append(60-i)

for i in gamma3:
    if sin(i*pi/180)*(n2/n1)<1:
        gamma4.append((180/pi)*asin(sin(i*pi/180)*(n2/n1)))
    else:
        gamma4.append(0)
        
halo44 =[]
gammatot=[]
for i in range(len(gamma1)):
    if gamma1[i]-gamma2[i]+gamma4[i]-gamma3[i]<0:
        gammatot.append(0)
    else:
        gammatot.append(2*(gamma1[i]-gamma2[i]+gamma4[i]-gamma3[i]))
    halo44.append(44)

gammamax=[]
gammamin=[]
maxi44=0
mini44=90
gmin=0
for i in range(len(gammatot)):
    if gammatot[i]!=0 and gammatot[i]<=mini44:
        mini44=gammatot[i]
    if gammatot[i]>=maxi44:
        maxi44=gammatot[i]
        
# Same length to plot
for i in range(len(gammatot)):
    gammamin.append(mini44)
    gammamax.append(maxi44)
    
# Incident angle for the first non null value
for i in range(len(gammatot)):
    if gammatot[i]!=0:
        gmin=gamma1[i]
        break

plt.plot(gamma1,gammatot,label="Possible angles",color='m')
plt.plot(gamma1,halo44,label="44°",c='c',linestyle='-.')
plt.plot(gamma1,gammamax,label=str(round(gammamax[0],4))+"°",c='k',linestyle=':')
plt.plot(gamma1,gammamin,label=str(round(gammamin[0],4))+"°",c='r',linestyle=':')
plt.axvline(x=gmin,label="$gamma_{i_{min}}$ = "+str(round(gmin,4))+"°",c='b',linestyle=':')
plt.xlabel('Incident angle')
plt.ylabel('Total angle '+str(chr(947)))
plt.title("44° parhelia")
plt.legend()
plt.xlim(0,90)
plt.ylim(0,90)
plt.show()

