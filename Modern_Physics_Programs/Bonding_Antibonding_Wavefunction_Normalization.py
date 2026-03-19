import numpy as np

"""
Please note AI was used to help create this program. All results were double checked and verified by David Senstad

Normalize psi_S = A(psi1 + psi2) and psi_D = B(psi1 - psi2)
for H2+ using 3D numerical integration on a Cartesian grid.

Protons are placed at:
   (0, 0, 0) and (L, 0, 0)

The code computes:
   S = ∭ psi1 * psi2 dV
and then uses
   A = 1 / sqrt(2(1 + S))
   B = 1 / sqrt(2(1 - S))

It also directly checks the normalization integrals:
   ∭ |psi_S|^2 dV
   ∭ |psi_D|^2 dV
"""

# Physical constants (SI units)
a0 = 5.29177210903e-11      # Bohr radius in meters
L = 0.106e-9                # proton separation in meters = 0.106 nm

# ------------------------------------------------------------
# Numerical grid settings
# Increase N for better accuracy, but it will use more memory.
# Start with N = 81 or 101. Larger is slower but more accurate.
# ------------------------------------------------------------
N = 81

# Integration box:
# Make it large enough that the wavefunctions are negligible
# near the boundaries.
x_min = -8.0 * a0
x_max = L + 8.0 * a0
y_min = -8.0 * a0
y_max =  8.0 * a0
z_min = -8.0 * a0
z_max =  8.0 * a0

# Create grid
x = np.linspace(x_min, x_max, N)
y = np.linspace(y_min, y_max, N)
z = np.linspace(z_min, z_max, N)

dx = x[1] - x[0]
dy = y[1] - y[0]
dz = z[1] - z[0]

X, Y, Z = np.meshgrid(x, y, z, indexing="ij")

# Distances from the electron to the two protons
r1 = np.sqrt(X**2 + Y**2 + Z**2)
r2 = np.sqrt((X - L)**2 + Y**2 + Z**2)

# Hydrogen 1s orbital normalization constant
norm_1s = 1.0 / np.sqrt(np.pi * a0**3)

# Wavefunctions centered on each proton
psi1 = norm_1s * np.exp(-r1 / a0)
psi2 = norm_1s * np.exp(-r2 / a0)

# ------------------------------------------------------------
# Helper function for 3D integration using repeated trapezoidal rule
# ------------------------------------------------------------
def integrate_3d(f, x, y, z):
    return np.trapz(np.trapz(np.trapz(f, z, axis=2), y, axis=1), x, axis=0)

# Check that psi1 and psi2 are approximately normalized
I1 = integrate_3d(psi1**2, x, y, z)
I2 = integrate_3d(psi2**2, x, y, z)

# Overlap integral
S = integrate_3d(psi1 * psi2, x, y, z)

# Normalization constants for symmetric and antisymmetric combinations
A = 1.0 / np.sqrt(2.0 * (1.0 + S))
B = 1.0 / np.sqrt(2.0 * (1.0 - S))

# Construct normalized psi_S and psi_D
psi_S = A * (psi1 + psi2)
psi_D = B * (psi1 - psi2)

# Direct checks of normalization
IS = integrate_3d(psi_S**2, x, y, z)
ID = integrate_3d(psi_D**2, x, y, z)

# ------------------------------------------------------------
# Print results
# ------------------------------------------------------------
print("Grid points per axis N =", N)
print("dx = {:.3e} m".format(dx))
print("dy = {:.3e} m".format(dy))
print("dz = {:.3e} m".format(dz))
print()

print("Check normalization of psi1: ∭|psi1|^2 dV =", I1)
print("Check normalization of psi2: ∭|psi2|^2 dV =", I2)
print()

print("Overlap integral S = ∭ psi1*psi2 dV =", S)
print("Normalization constant A =", A)
print("Normalization constant B =", B)
print()

print("Check normalization of psi_S: ∭|psi_S|^2 dV =", IS)
print("Check normalization of psi_D: ∭|psi_D|^2 dV =", ID)