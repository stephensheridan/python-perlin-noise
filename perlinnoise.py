"""
Author: Stephen Sheridan
Simple 1D Perlin noise generator using 
Casey Duncan's Python Perlin noise gen lib
https://github.com/caseman/noise
"""
from noise import pnoise1
from numpy import interp
import matplotlib.pyplot as plt
import sys
import time

# Pick a base point in time. We can move forward in time to 
# geberate more perlin noise
base = 6 
# Pick a time step to move forward by. The bigger the step the bigger
# the jump in noise values
step = 0.01
# Store some perlin noise values
pvalues = []
# Generate N perlin noise values from base with time step
N = 1000
# Set the required output range for interpolation [MIN, MAX]
outRange = [0,100]

for x in range(N):
	# Use 1d pnoise1 to generate noise value
	pval = pnoise1(base)
	# Store and move on
	pvalues.append(interp(pval, [-1,1], outRange))
	# Incerement base by step to get next noise value
	base = base + step

# Plot the values we got
plt.plot(pvalues)
plt.ylabel('Perlin Noise')
plt.xlabel('Time Step')
plt.show()


