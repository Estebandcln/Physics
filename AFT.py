# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 09:22:31 2021

@author: DECLINE
"""

import cantera as ct
import numpy as np
import matplotlib.pyplot as plt

# Adiabatic Flame Temperature

# The Species objects are defined in the GRI 3.0 mechanism
species = {S.name: S for S in ct.Species.listFromFile('gri30.xml')}

# IdealGas object with species representing complete combustion
complete_species = [species[S] for S in ('CH4', 'O2', 'N2', 'CO2', 'H2O', 'AR')]
gas1 = ct.Solution(thermo='IdealGas', species=complete_species)

phi = np.linspace(0.5, 2, 100)
T_complete = np.zeros(phi.shape)
for i in range(len(phi)):
    gas1.TP = 300, ct.one_atm
    gas1.set_equivalence_ratio(phi[i], 'CH4', 'O2:1')
    gas1.equilibrate('HP')
    T_complete[i] = gas1.T    

plt.plot(phi, T_complete, label='without N2')
plt.title(label='Adiabatic Flame Temperature')
plt.xlabel('Equivalence Ratio')
plt.ylabel('Temperature, K')
plt.legend()

phi = np.linspace(0.5, 2, 100)
T_complete = np.zeros(phi.shape)
for i in range(len(phi)):
    gas1.TP = 300, ct.one_atm
    gas1.set_equivalence_ratio(phi[i], 'CH4', 'O2:1, N2:3.76')
    gas1.equilibrate('HP')
    T_complete[i] = gas1.T    

plt.plot(phi, T_complete, label='with N2')
plt.xlabel('Equivalence Ratio')
plt.ylabel('Temperature, K')
plt.legend()