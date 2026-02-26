import random
import math

#Hydrogen atom's 2s radial probability density
def P_2s(r):
    return ((1/8) * r**2 * (2 - r)**2 * math.exp(-r))

num_of_rs = 0
total_Z = 0
total_iterations = 10

while True:
    rad = random.uniform(0, 15) # generates a random radius between 0 to 15
    y = random.uniform(0, 1) # generates random y from 0 to 1 used for rejection sampling
    P_r = P_2s(rad)

    if (y < P_r):
        ++num_of_rs
        if (rad < 1):
            total_Z += 3
        else:
            ++total_Z
        ++num_of_rs
        if (num_of_rs >= total_iterations):
            break

Z_eff = total_Z / 3

print(f"After {total_iterations} random radii, the average Z_eff = {Z_eff}")