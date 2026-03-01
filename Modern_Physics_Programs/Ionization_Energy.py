import matplotlib.pyplot as plt

#Each elements symbol where array's index corresponds to the elements atomic number.
SYMBOL = [
    None,
    "H","He","Li","Be","B","C","N","O","F","Ne",
    "Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca",
    "Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn",
    "Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr",
    "Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn",
    "Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd",
    "Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb",
    "Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg",
    "Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th",
    "Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm"
]

#Generates an array filled with the correct subshell ordering in accordance with the n+l rule
def generate_subshell_order():
    subshells = []

    #iterate through each possible principle quantum number n 1 - 7 on the periodic table then iterate through every possible orbital angular momentum l for each n
    for n in range(1, 8):           
        for l in range(0, n):
            # Use 2l + 1 rule to find how many oritals are possible given l and Pauli exlusion principle to determine maximun number of electrons in the possible shell, then add that orbital to the subshells as a mutable 'tuplet'
            num_orbitals = 2 * l + 1       
            electron_capactiy = 2 * num_orbitals
            subshells.append([n, l, electron_capactiy])

    #Sort the subshells in accordance with the n+l rule using a custom function with first compares
    #the subshells n+l value. In case of a tie it sorts with the lowest n value
    subshells.sort(key=lambda t: (t[0] + t[1], t[0]))
    return subshells

#Find which period the element is in which in turn determines the value of n to use when calculating IE
def find_n(Z):
    remaining_subshells = generate_subshell_order()
    remaining_z = Z
    
    #Track the largest principle number by looking at the first value in each orbital's tuplet
    highest_n = remaining_subshells[0][0] 
    while remaining_z > 0:
        # If the last value in the tuplet is 0 then the orbital is full and the electron must be placed in the next orbital by removing
        # the full oribital from the list of remaining orbitals
        if (remaining_subshells[0][-1] == 0):
            remaining_subshells.pop(0)
            if (remaining_subshells[0][0] > highest_n):
                highest_n = remaining_subshells[0][0]
        # Decrement the tuplet corresponding to hoe many electrons can still
        # be placed in the tuplet and how many electrons are left to be placed
        remaining_subshells[0][-1] -= 1
        remaining_z -= 1
    return highest_n
