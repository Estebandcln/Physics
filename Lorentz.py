# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 22:29:09 2023

@author: DECLINE
"""

import matplotlib.pyplot as plt
import numpy as np


plt.close('all')
plt.figure(1)
c = 299792458 # m/s
v = np.linspace(0,c,200)
gamma = []
t2 = []
for i in range(len(v)):
    gamma.append(1/np.sqrt(1-v[i]**2/c**2))
    t1 = 24 # h
    t2.append(t1*gamma[i])

print(t2)
plt.plot(v, gamma)
plt.xlabel("v")
plt.ylabel("Gamma")
plt.grid()
plt.show()

plt.figure(2)
beta = []
for i in range(len(v)):
    beta.append(np.sqrt(1-v[i]**2/c**2))

plt.plot(v/c, beta)
plt.xlabel("v/c")
plt.ylabel("Beta")
plt.grid()



a = "rrr"
b = "ttt"
c = [a,b]
l = []
for i in range(len(c)):
    l.append(c[i])