# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 17:56:53 2022

@author: DECLINE
"""


from math import *

eps=8.8542E-12   # Vacuum permittivity (m^-3*kg^-1*s^4*A^2)
k=1.3807E-23     # Boltzmann constant (m^2*kg*s^-2*K^-1)
e=1.6022E-19     # Elementary charge (C)
me=9.1094E-31    # Electron mass (kg)

#T in eV, n in m-3
#debye in m, omega in rad.s-1

T=100
n=10**15

#Debye length
def debye(T,n):
  return round(sqrt(eps*T/(n*e)),6)

#frequency
def plomega(T,n):
  return int(sqrt(n*e*e/(eps*me)))
  
# plasma parameter
def pllambda(T,n):
  return int(n*4*pi*(debye(T,n)**3))
  
#number of particles in a Debye cube
def plNd(T,n):
  return int(n*(debye(T,n)**3))
  
print('Debye length =',debye(T,n),',frequency =',plomega(T,n),',plasma parameter =',pllambda(T,n),'and nb of part in 1 $m^3$ =',plNd(T,n))
  
  
  
  
        