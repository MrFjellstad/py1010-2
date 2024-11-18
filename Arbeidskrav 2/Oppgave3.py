"""
Et program med en funksjon som regner om fra grader til radianer.
"""
import numpy as np

v_grad =  float(input('Skriv inn gradtallet:' ))

v_rad = v_grad*np.pi/180

print (f'{v_grad} grader = {v_rad:.2f} radianer')

# Eller med numpy
v_rad2 = np.deg2rad(v_grad)

print (f'{v_grad} grader = {v_rad2:.2f} radianer')
