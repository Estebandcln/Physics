# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 00:06:37 2023

@author: DECLINE
"""

import matplotlib.pyplot as plt
import numpy as np

# N-parts wall

T_i = 20  # Internal environment temperature (°C)
T_f = 12  # External environment temperature (°C)
S = 100  # Wall area (m²)

# Materials thermal conductivity lambda

l_Cu = 398 #W/(m.°C)
l_Pb = 34.3 #W/(m.°C)
l_Al = 226 #W/(m.°C)
l_Wf = 0.04 #W/(m.°C)
l_Gw = 0.036 #W/(m.°C)
l_gl = 1.05 #W/(m.°C)
l_oak = 0.16 #W/(m.°C)

# Fluids thermal convection coefficient h

h_air = 10 #W/(m.°C)
h_water = 75 #W/(m.°C)

# Tchickness

e_Cu = 1 #m
e_Pb = 0.5 #m
e_Al = 1 #m
e_Wf = 0.03 #m
e_Gw = 0.05 #m 
e_gl = 0.01 #m
e_oak = 0.1 #m
e_air = 0.5 #m
e_water = 0.5 #m

# Wall composition

f = ['Air', 'Water'] # Fluids
m = ['Air', 'Water', 'Copper', 'Lead', 'Aluminum', 'Wood fiber', 'Glass wool', 'Glass', 'Oak'] # Layers materials
wall = ['Air', 'Glass wool', 'Water'] # Input you wall here
N1= [] # Ordered materials and fluids from the inside to the outside

for i in wall:
    for j in range(len(m)):
        if i == m[j]:
            N1.append(j)

coeff = [h_air, h_water, l_Cu, l_Pb, l_Al, l_Wf, l_Gw, l_gl, l_oak]
e = [e_air, e_water, e_Cu, e_Pb, e_Al, e_Wf, e_Gw, e_gl, e_oak]

# Thermal resistance

R_th = []
R_tot = 0 # °C/W

for i in N1:
    if m[i] in f:
        
        R_th.append(1/(coeff[i]*S)) # Fluid = convection
        R_tot += 1/(coeff[i]*S)
        
    else:
        
        R_th.append(e[i]/(coeff[i]*S)) # Material = conduction
        R_tot += e[i]/(coeff[i]*S)

phi = np.abs(round(((T_i-T_f))/(R_tot),4))

T_list1 = [T_i] # Internal environment, internal surface, n layers, external surface, external environment
a = 0

if T_i>T_f:    
    for i in N1:
        if m[i] in f:
            if len(T_list1)<2:

                T_list1.append(round(T_i-phi/(S*coeff[i]),5))
                print(T_i,coeff[i],T_i-phi/(S*coeff[i]),a,i)
                a += 1
                
            else:
               
                T_list1.append(round(T_f+phi/(S*coeff[i]),5))
                print(T_f,coeff[i],T_f+phi/(S*coeff[i]),a,i)
                a += 1
                
        else:
            T_list1.append(round(T_list1[a]-phi*e[i]/(S*coeff[i]),5))
            print(T_list1[a],e[i],coeff[i],T_list1[a]-phi*e[i]/(S*coeff[i]),a,i)
            a += 1
else:
    for i in N1:
        if m[i] in f:
            if len(T_list1)<2:

                T_list1.append(round(T_i+phi/(S*coeff[i]),5))
                print(T_i,coeff[i],T_i-phi/(S*coeff[i]),a,i)
                a += 1
                
            else:
               
                T_list1.append(round(T_f-phi/(S*coeff[i]),5))
                print(T_f,coeff[i],T_f+phi/(S*coeff[i]),a,i)
                a += 1
                
        else:
            T_list1.append(round(T_list1[a]+phi*e[i]/(S*coeff[i]),5))
            print(T_list1[a],e[i],coeff[i],T_list1[a]-phi*e[i]/(S*coeff[i]),a,i)
            a += 1
            
k1 = T_list1[-1]
print(T_list1)
T_list1.remove(k1)
print(T_list1)
k2 = (k1+T_list1[-1])/2
T_list1.remove(T_list1[-1])
print(T_list1)
T_list1.append(k2)
print(T_list1)
T_list1.append(T_f)
print(T_list1)

x_list1 = [0]
b = 0

for i in N1:
    x_list1.append(e[i]+x_list1[b])
    b += 1

x_max = x_list1[-1]

plt.figure(1)

#x = np.linspace(0, x_max, len(T_list))
plt.plot(x_list1, T_list1, label = 'Temperature', c='r')
plt.legend()
plt.title('Temperature profile')
plt.xlabel('Wall thickness (m)')
plt.ylabel('Temperature throughout the wall (°C)')

del x_list1[0]
del x_list1[-1]
for i in x_list1:
    
    plt.axvline(x=i, c='k', linewidth=1)
    
    

############################## From the outside #############################

N2 = []
N = N1.copy()
for i in range(len(N1)):
    N2.append(N1[-1])
    del N1[-1] 
    
T_list2 = [T_f] # External environment, external surface, n layers, internal surface, internal environment
a = 0

if T_i>T_f:    
    for i in N2:
        if m[i] in f:
            if len(T_list2)<2:

                T_list2.append(round(T_f+phi/(S*coeff[i]),5))
                print(T_f,coeff[i],T_f+phi/(S*coeff[i]),a,i)
                a += 1
                
            else:
               
                T_list2.append(round(T_i-phi/(S*coeff[i]),5))
                print(T_i,coeff[i],T_i-phi/(S*coeff[i]),a,i)
                a += 1
                
        else:
            T_list2.append(round(T_list2[a]+phi*e[i]/(S*coeff[i]),5))
            print(T_list2[a],e[i],coeff[i],T_list2[a]+phi*e[i]/(S*coeff[i]),a,i)
            a += 1
else:
    for i in N2:
        if m[i] in f:
            if len(T_list2)<2:

                T_list2.append(round(T_f-phi/(S*coeff[i]),5))
                print(T_f,coeff[i],T_f+phi/(S*coeff[i]),a,i)
                a += 1
                
            else:
               
                T_list2.append(round(T_i+phi/(S*coeff[i]),5))
                print(T_i,coeff[i],T_i-phi/(S*coeff[i]),a,i)
                a += 1
                
        else:
            T_list2.append(round(T_list2[a]-phi*e[i]/(S*coeff[i]),5))
            print(T_list2[a],e[i],coeff[i],T_list2[a]+phi*e[i]/(S*coeff[i]),a,i)
            a += 1
            
k1 = T_list2[-1]
print(T_list2)
T_list2.remove(k1)
print(T_list2)
k2 = (k1+T_list2[-1])/2
T_list2.remove(T_list2[-1])
print(T_list2)
T_list2.append(k2)
print(T_list2)
T_list2.append(T_i)
print(T_list2)

x_list2 = [0]
b = 0

for i in N:
    x_list2.append(e[i]+x_list2[b])
    print(e[i]+x_list2[b])
    b += 1

T_list2.reverse()
x_max = x_list2[-1]

plt.figure(2)
#x = np.linspace(0, x_max, len(T_list))
plt.plot(x_list2, T_list2, label = 'Temperature', c='r')
plt.legend()
plt.title('Temperature profile')
plt.xlabel('Wall thickness (m)')
plt.ylabel('Temperature throughout the wall (°C)')

del x_list2[0]
del x_list2[-1]
for i in x_list2:

    plt.axvline(x=i, c='k', linewidth=1)

# Mean value? List of the converged values

x_list = [0]
c = 0

for i in N:
    x_list.append(e[i]+x_list[c])
    print(e[i]+x_list[c])
    c += 1

a = 0
b = 0
h = 1e-3
T_list = []
for i in range(len(T_list1)):
    if np.abs(round(T_list1[i]-T_list2[i],5))<0.1:
        a += 1
        T_list.append(T_list1[i])
    else:
        b += 1
        T = np.abs(T_list1[i]-T_list2[i])
        print("T",T)
        while T>0.1:
            T_list1[i] = round(T_list1[i]*(1+h),5)
            T_list2[i] = round(T_list2[i]*(1+h),5)
            T = np.abs(round(T_list1[i]-T_list2[i],5))

        T_list.append(T)

plt.figure(3)

plt.plot(x_list, T_list, label = 'Temperature', c='r')
plt.legend()
plt.title('Temperature profile')
plt.xlabel('Wall thickness (m)')
plt.ylabel('Temperature throughout the wall (°C)')

print(x_list)
del x_list[0]
del x_list[-1]
print(x_list)
for i in x_list:
    
    plt.axvline(x=i, c='k', linewidth=1)
