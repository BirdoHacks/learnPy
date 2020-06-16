# import as needed while writing the functions
# these are what I might use, but use what makes sense to you
import numpy as np
import matplotlib.pyplot as plt

    # V is the incremented voltage, which is also tabulated in data.csv
def invSqrtV(V):
    return 1/(np.sqrt(V))

# D is the observed diameter at a given voltage, which is tabulated in data.csv
def sinTheta(D, L):             # can be D1 or D2, works for both
    t = 1/2*(np.arctan(D/2/L))  # this the 'Bragg Angle'
    return np.sin(t)            # gives radians, not degrees
    
def getValues(D, L, V):
    Voltage = invSqrtV(V)
    sinAngle = sinTheta(D, L)
    return Voltage, sinAngle

def linFit(V, t):
    slope = np.polyfit(V,t,1)[0]
    return slope    

h = 6.626070040e-34  # Planck's constant - J*s
e = 1.6021766208e-19 # charge of electron - C
m_e = 9.10938356e-31 # mass of electron - kg

def getD(s):
    d = h/(2*s*np.sqrt(2*e*m_e))
    return d

#def deriveFromData(args):
    # write code here that should be run when you call 'deriveFromData()'

#def calcD1(args):
    # write code here that calculates d1

#def calcD2(args):
    # write code here that calculates d2

