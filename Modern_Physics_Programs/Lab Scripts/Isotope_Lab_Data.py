import numpy as np
import matplotlib.pyplot as plt

# Neon calibration data (wavelength in nm, grating steps are unitless motor steps)
neon_wavelength_steps = np.array([
    743.89, 703.24, 671.7, 667.83, 659.9, 653.29, 650.65, 640.22, 638.3,
    633.44, 630.48, 626.65, 621.73, 616.36, 614.31, 609.62, 607.43, 603.0,
    597.55, 594.48, 588.19, 585.25
], dtype=float)

neon_grating_steps = np.array([
    53038, 49566, 47277, 46850, 45966, 45256, 44972, 43851, 43638,
    43090, 42736, 42343, 41822, 41257, 41032, 40528, 40300, 39798,
    39195, 38866, 38202, 37886
], dtype=float)

# ---- Linear regression: lambda = a*G + b ----
a, b = np.polyfit(neon_grating_steps, neon_wavelength_steps, deg=1)

# Predictions + goodness of fit (R^2)
pred = a * neon_grating_steps + b
residuals = neon_wavelength_steps - pred
ss_res = np.sum(residuals**2)
ss_tot = np.sum((neon_wavelength_steps - np.mean(neon_wavelength_steps))**2)
r2 = 1 - ss_res / ss_tot

print(f"Calibration fit: lambda = a*G + b")
print(f"a = {a:.10f} nm/step")
print(f"b = {b:.6f} nm")
print(f"R^2 = {r2:.6f}")

# ---- Plot ----
G_fit = np.linspace(neon_grating_steps.min(), neon_grating_steps.max(), 300)
lam_fit = a * G_fit + b

plt.figure(figsize=(8, 5))
plt.scatter(neon_grating_steps, neon_wavelength_steps, label="Neon data")
plt.plot(G_fit, lam_fit, label="Linear fit")
plt.xlabel("Grating step number")
plt.ylabel("Wavelength (nm)")
plt.title("Neon Calibration Curve: Wavelength vs Grating Step")
plt.grid(True)
plt.legend()
plt.tight_layout()

# Save figure
plt.savefig("neon_calibration_curve.png", dpi=300)
plt.show()

g_or_w = input("Would you like to calculate (1) grating based on wavelength? or (2) wavelength based on grating? [enter '1','2', or exit] ")
while True:
    if g_or_w == "1":
        wavelength = input("enter your wavelength: ")
        grating = (float(wavelength) - b) / a
        print(f"{wavelength} nm corresponds to a grating of {grating:.1f}")
        g_or_w = input("Would you like to calculate (1) grating based on wavelength? or (2) wavelength based on grating? [enter '1','2', or exit] ")
    elif g_or_w == "2":
        grating = input("enter your grating: ")
        wavelength = a * float(grating) + b
        print(f"{grating} corresponds to a wavelength of {wavelength:.1f} nm")
        g_or_w = input("Would you like to calculate (1) grating based on wavelength? or (2) wavelength based on grating? [enter '1','2', or exit] ")
    elif g_or_w == "exit":
        break
    else:
        g_or_w = input(f"{g_or_w} is an invalid input. Enter either 1, 2, or exit ")