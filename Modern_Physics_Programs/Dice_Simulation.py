import random
import matplotlib.pyplot as plt

"""
Author: David Senstad

This program simulates N number of dice starting at 1 and every second ecah dice has a x% chance to change to a different value.
The average value of the dice for each second are plotted. This is meant to simulate a macrostate moving
to its highest entropy microstate.

"""

# Number of dice
N = 1000

# Number of times dice are randomized
rolls = 3000

# Starting value
start_val = 6

# Initializes array of dice values all starting at 1
Dice_Values = [start_val] * N
Average_Dice_Values = [start_val]

# Percantage change that a die changes value
percent = 1

for x in range(rolls):
    for n in range(N):
        if random.random() * 100 <= percent:
            Dice_Values[n] = random.randint(1, 6)
    Average_Dice_Values.append(sum(Dice_Values) / N)

x_vals = list(range(0, rolls + 1))
plt.figure()
plt.plot(x_vals, Average_Dice_Values)
plt.axhline(y=3.5, color='black', linestyle='-', label='Expected average value')

plt.xlabel("Time Intervals")
plt.ylabel("Average Value of the Dice")
plt.title("Average Dice Value over time")

plt.legend()
plt.tight_layout()
plt.show()