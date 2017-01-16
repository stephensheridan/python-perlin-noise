"""
Author: Stephen Sheridan
Simple 1D Perlin noise generator using 
Caseman's Python Perlin noise gen lib
https://github.com/caseman/noise
"""
from noise import pnoise1
import matplotlib.pyplot as plt

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

for x in range(N):
	# Use 1d pnoise1 to generate noise value
	pvalues.append(pnoise1(base))
	# Incerement base by step to get next noise value
	base = base + step

# Plot the values we got
plt.plot(pvalues)
plt.ylabel('Perlin Noise')
plt.show()