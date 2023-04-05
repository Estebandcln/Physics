# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 00:06:37 2023

@author: DECLINE
"""

import matplotlib.pyplot as plt
import numpy as np

# N-parts wall

T_i = 20  # Internal environment temperature (°C)
T_f = 15  # External environment temperature (°C)
S = 10  # Wall area (m²)

# Materials thermal conductivity lambda

l_Cu = 398 #W/(m.°C)
l_Pb = 34.3 #W/(m.°C)
l_Al = 226 #W/(m.°C)
l_SS = 13.4 #W/(m.°C)
l_gl = 1.05 #W/(m.°C)
l_oak = 0.16 #W/(m.°C)

# Fluids thermal convection coefficient h

h_air = 10 #W/(m.°C)
h_water = 75 #W/(m.°C)

# Tchickness

e_Cu = 1 #m
e_Pb = 0.5 #m
e_Al = 0.1 #m
e_SS = 0.6 #m
e_gl = 0.4 #m
e_oak = 1 #m
e_air = 0.5 #m
e_water = 0.5 #m

# Wall composition

f = ['Air', 'Water'] # Fluids
m = ['Air', 'Water', 'Copper', 'Lead', 'Aluminum', 'Stained steel', 'Glass', 'Oak'] # Layers materials
wall = ['Water', 'Lead', 'Aluminum', 'Lead', 'Copper', 'Air']
N = []

for i in wall:
    for j in range(len(m)):
        if i == m[j]:
            N.append(j)

coeff = [h_air, h_water, l_Cu, l_Pb, l_Al, l_SS, l_gl, l_oak]
e = [e_air, e_water, e_Cu, e_Pb, e_Al, e_SS, e_gl, e_oak]

# Thermal resistance

R_th = []
R_tot = 0 # °C/W

for i in N:
    if m[i] in f:
        
        R_th.append(1/(coeff[i]*S)) # Fluid = convection
        R_tot += 1/(coeff[i]*S)
        
    else:
        
        R_th.append(e[i]/(coeff[i]*S)) # Material = conduction
        R_tot += e[i]/(coeff[i]*S)

phi = np.abs((T_i-T_f))/(R_tot)

T_list = [T_i] # Internal environment, internal surface, n layers, external surface, external environment
a = 0

if T_i>T_f:    
    for i in N:
        if m[i] in f:
            if len(T_list)<2:

                T_list.append(T_i-phi/(S*coeff[0]))
                print(T_i,coeff[0],T_i-phi/(S*coeff[0]),a,i)
                a += 1
                
            else:
               
                T_list.append(T_f+phi/(S*coeff[1]))
                print(T_f,coeff[1],T_f+phi/(S*coeff[1]),a,i)
                a += 1
                
        else:
            T_list.append(T_list[a]-phi*e[i]/(S*coeff[i]))
            print(T_list[a],e[i],coeff[i],T_list[a]-phi*e[i]/(S*coeff[i]),a,i)
            a += 1
else:

    for i in N:
        if i in f:
            if len(T_list)<2:

                T_list.append(T_i+phi/(S*coeff[0]))
                print(T_i,coeff[0],T_i-phi/(S*coeff[0]),a,i)
                a += 1
                
            else:
               
                T_list.append(T_f-phi/(S*coeff[1]))
                print(T_f,coeff[1],T_f+phi/(S*coeff[1]),a,i)
                a += 1
                
        else:
            T_list.append(T_list[a]+phi*e[i]/(S*coeff[i]))
            print(T_list[a],e[i],coeff[i],T_list[a]-phi*e[i]/(S*coeff[i]),a,i)
            a += 1
            
k1 = T_list[-1]
print(T_list)
T_list.remove(k1)
print(T_list)
k2 = (k1+T_list[-1])/2
T_list.remove(T_list[-1])
print(T_list)
T_list.append(k2)
print(T_list)
T_list.append(T_f)
print(T_list)

x_list = [0]
b = 0

for i in N:
    x_list.append(e[i]+x_list[b])
    b += 1

x_max = x_list[-1]

#x = np.linspace(0, x_max, len(T_list))
plt.plot(x_list, T_list, label = 'Temperature', c='r')
plt.legend()
plt.title('Temperature profile')
plt.xlabel('Wall thickness (m)')
plt.ylabel('Temperature within the wall (°C)')

x_list.remove(x_list[0])
x_list.remove(x_list[-1])
for i in x_list:
    
    plt.axvline(x=i, c='k', linewidth=1)