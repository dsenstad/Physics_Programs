# Author: David Senstad
import math
"""

The purpose of this program is given a paramagnet with N atoms, find
the probability that between 40% and 60% of those atoms are pointing up

Note these bounds can be changed by changing the lower_bound and upper_bound variables

Also Note the level of presision in which the final probability is printed out with must also be increased
for larger values of N to avoid the program printing out '100.00000...%'

"""

# size of paramagnet
N = 100

lower_bound = 0.4
upper_bound = 0.6

states = []
total_states = 2**N
# checks for each number from 0 to N if that number is between the given lower bound and upper bound
for i in range(N + 1):
    if (i / N) >= lower_bound and (i / N) <= upper_bound:
        states.append(i)

probability = 0

for i in states:
    probability += (math.comb(N, i)) / total_states

print(f"The probability of finding between {lower_bound * 100}% and {upper_bound * 100}% of the atoms in a paramagnet {N} atoms large is {probability * 100:.5f}%")