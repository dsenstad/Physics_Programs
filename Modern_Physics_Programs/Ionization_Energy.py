import matplotlib.pyplot as plt

#Each elements symbol where array's index corresponds to the elements atomic number.
SYMBOL = [
    None,
    "H","He",
    "Li","Be","B","C","N","O","F","Ne",
    "Na","Mg","Al","Si","P","S","Cl","Ar",
    "K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn",
    "Ga","Ge","As","Se","Br","Kr",
    "Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd",
    "In","Sn","Sb","Te","I","Xe",
    "Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu",
    "Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg",
    "Tl","Pb","Bi","Po","At","Rn",
    "Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr",
    "Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn",
    "Nh","Fl","Mc","Lv","Ts","Og"
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

#Find which period the element is in which in and the Z_eff of that element
def find_n_and_Zeff(Z):
    remaining_subshells = generate_subshell_order()
    remaining_z = Z
    Z_eff = 0.5
    
    #Track the largest principle number by looking at the first value in each orbital's tuplet
    highest_n = remaining_subshells[0][0] 
    while remaining_z > 0:
        # If the last value in the tuplet is 0 then the orbital is full and the electron must be placed in the next orbital by removing
        # the full oribital from the list of remaining orbitals
        if (remaining_subshells[0][-1] == 0):
            remaining_subshells.pop(0)
            Z_eff = 1
            if (remaining_subshells[0][0] > highest_n):
                highest_n = remaining_subshells[0][0]
        else:
            Z_eff += 0.5

        if (remaining_subshells[0][1] == 2): # hard codes the Z_eff of every element in the d-block to be Z_eff = 1.5
            Z_eff = 1.5
        elif (remaining_subshells[0][1] == 3): # hard codes the Z_eff of every element in the f-block to be Z_eff = 2.5
            Z_eff = 2.5
        # Decrement the tuplet corresponding to hoe many electrons can still
        # be placed in the tuplet and how many electrons are left to be placed
        remaining_subshells[0][-1] -= 1
        remaining_z -= 1
    return (highest_n, Z_eff)

def IE(Z):
    n_zeff_tuple = find_n_and_Zeff(Z)
    n = n_zeff_tuple[0]
    Z_eff = n_zeff_tuple[1]
    return 13.6 * (Z_eff/n)**2

#Ask user how many elements they want to see
Z_max = input("Enter how many elements you want to appear on this graph (max 118): ")
while True:
    try:
        Z_max = int(Z_max)
        if (Z_max <= 118):
            break
        Z_max = input(f"{Z_max} is not a valid input. Enter a valid integer less than or equal to 118: ")
    except:
        Z_max = input(f"{Z_max} is not a valid input. Enter a valid integer less than or equal to 118: ")


Elements_Z = list(range(1, Z_max + 1))
IEs = []

for i in Elements_Z:
    IEs.append(IE(i))

#Generate plot with names
plt.figure()
plt.plot(Elements_Z, IEs)
plt.xlabel("Z (atomic number)")
plt.ylabel("Ionization energy (eV) — simple screening model")
plt.title("Model ionization energy vs Z (screening: lower=1, same shell=1/2)")

#Label the noble gases
noble_Z = [2, 10, 18, 36, 54, 86, 118]  # He, Ne, Ar, Kr, Xe, Rn, Og
for z in noble_Z:
    if z <= Z_max:
        #Annote the elemental symbol at an offest 8 pixels above the point on the graph and center the text
        plt.annotate(SYMBOL[z], (z, IEs[z-1]), textcoords="offset points", xytext=(0, 8), ha="center")

plt.tight_layout()
plt.show()