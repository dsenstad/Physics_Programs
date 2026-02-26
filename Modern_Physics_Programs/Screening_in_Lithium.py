import random
import math

#Hydrogen atom's 2s radial probability density
def P_2s(r):
    return ((1/8) * r**2 * (2 - r)**2 * math.exp(-r))

#Hydrogen atom's 2p radial probability density
def P_2p(r):
    return ((1/24) * r**4 * math.exp(-r))

num_of_rs = 0
total_Z_2s = 0
total_Z_2p = 0
iterations = 10000

#Calculates total Z for 2s distribution
while (num_of_rs < iterations):
    rad = random.uniform(0, 15) # generates a random radius between 0 to 15
    y = random.uniform(0, 1) # generates random y from 0 to 1 used for rejection sampling
    p = P_2s(rad)

    if (y < p):
        num_of_rs += 1
        if (rad < 1):
            total_Z_2s += 3
        else:
            total_Z_2s += 1

#resets variables
num_of_rs = 0

#Calculates total Z for 2p distribution
while (num_of_rs < iterations):
    rad = random.uniform(0, 15) # generates a random radius between 0 to 15
    y = random.uniform(0, 1) # generates random y from 0 to 1 used for rejection sampling
    p = P_2p(rad)

    if (y < p):
        num_of_rs += 1
        if (rad < 1):
            total_Z_2p += 3
        else:
            total_Z_2p += 1

Z_eff_2s = total_Z_2s / iterations
Z_eff_2p = total_Z_2p / iterations

print(f"After {iterations} random radii, the average Z_eff are:")
print(f"2s: {Z_eff_2s:.4f}")
print(f"2p: {Z_eff_2p:.4f}")