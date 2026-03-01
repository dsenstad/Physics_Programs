import matplotlib.pyplot as plt

RYD_EEV = 13.6  # 1 Rydberg in eV

# Element symbols 1–100 (for optional labeling)
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

def subshell_fill_order(nmax=10):
    """
    Generate subshells in (n+l, n) order (Aufbau / n+l rule).
    Each subshell has capacity 2(2l+1).
    Returns list of tuples (n, l, cap).
    """
    subs = []
    for n in range(1, nmax + 1):
        for l in range(0, n):
            cap = 2 * (2 * l + 1)
            subs.append((n, l, cap))
    subs.sort(key=lambda t: (t[0] + t[1], t[0]))  # (n+l), then lower n first
    return subs

FILL_ORDER = subshell_fill_order(nmax=10)

def shell_populations_for_Z(Z):
    """
    Fill electrons up to atomic number Z using n+l rule.
    Returns:
      shell_counts: dict n -> total electrons in shell n
      outer_n: principal quantum number of outer shell (highest n occupied)
    """
    remaining = Z
    shell_counts = {}

    for n, l, cap in FILL_ORDER:
        if remaining <= 0:
            break
        put = min(cap, remaining)
        shell_counts[n] = shell_counts.get(n, 0) + put
        remaining -= put

    outer_n = max(shell_counts.keys())
    return shell_counts, outer_n

def ionization_energy_simple(Z):
    """
    Simple screening model:
      - Each electron in a lower shell (n' < n_outer) screens 1 proton.
      - Each other electron in the same outer shell (same n) screens 1/2 proton.
    Binding energy for outermost electron:
      E = -Ry * Z_eff^2 / n^2
    Ionization energy = |E| in eV.
    """
    shell_counts, n_outer = shell_populations_for_Z(Z)

    n_lower_e = sum(cnt for n, cnt in shell_counts.items() if n < n_outer)
    n_same = shell_counts.get(n_outer, 0)

    # Outer electron does not screen itself:
    S = n_lower_e + 0.5 * (n_same - 1)

    Z_eff = Z - S
    if Z_eff < 0:
        Z_eff = 0.0

    IE = RYD_EEV * (Z_eff ** 2) / (n_outer ** 2)
    return IE, n_outer, Z_eff

# ---- Compute and plot IE vs Z ----
Z_max = 100
Zs = list(range(1, Z_max + 1))
IEs = []
outer_ns = []
Zeffs = []

for Z in Zs:
    ie, n_out, zeff = ionization_energy_simple(Z)
    IEs.append(ie)
    outer_ns.append(n_out)
    Zeffs.append(zeff)

plt.figure()
plt.plot(Zs, IEs)
plt.xlabel("Z (atomic number)")
plt.ylabel("Ionization energy (eV) — simple screening model")
plt.title("Model ionization energy vs Z (screening: lower=1, same shell=1/2)")

# Label noble gases like Figure 8.5
noble_Z = [2, 10, 18, 36, 54, 86]  # He, Ne, Ar, Kr, Xe, Rn
for z in noble_Z:
    if z <= Z_max:
        plt.annotate(SYMBOL[z],
                     (z, IEs[z-1]),
                     textcoords="offset points",
                     xytext=(0, 8),
                     ha="center")

plt.tight_layout()
plt.show()