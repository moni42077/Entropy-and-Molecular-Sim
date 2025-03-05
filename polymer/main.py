import numpy as np
from scipy import constants
import sympy as sp

def e_a(theta):
    return -k * (theta-theta0)**2 / 2

theta0 = np.deg2rad(112)
k = 65
T = 300
beta= sp.Symbol('b') #1 / (constants.Boltzmann * T)
nom = 0.
denom = 0.

for theta in np.linspace(0.1,2*np.pi,100):
    nom += -e_a(theta) * sp.exp(-beta * e_a(theta))
    denom += sp.exp(-beta * e_a(theta))

z = nom/denom
z_val =  z.subs(beta, 1/(constants.Boltzmann * T))


e =  1/ z_val * sp.diff(z,beta)
e_val = e.subs(beta, 1/(constants.Boltzmann * T))

print(z_val)
print(e_val)
print(-constants.Boltzmann * T * np.log(z_val))
