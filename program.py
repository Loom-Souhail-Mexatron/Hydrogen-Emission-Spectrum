import numpy as np

rydConst = 109.737e-4 #nm
hartree = 27.211 #eV
planckConst = 6.626e-34 # m^2.Kg/s
c = 299792458 #m/s

waves = [] #Array to store wavelengths

def spect(n1, n2, r):
	m = r * (np.square((1/n1)) - np.square((1/n2)))
	return round(1/m, 5)

def eneL(z, n):
	result = (-1 * np.square(z)) / 2 * np.square(n)
	return hartree / result

def phoE(pl, c, w):
	return (pl * c) / w

print("Hydrogen emission spectrum wavelengths of the Balmer series (in the visible part of the light spectrum)")
print("") #I forgot how to space between lines smh

for i in range(4):
	print("Transition from n =", i+3, end="")
	print(" of energy level equivalent to", round(eneL(1, i + 3), 3), end="")
	print(" eV to n =", 2)
	waves.append(spect(2, i+3, rydConst))
	print(spect(2, i+3, rydConst), "nm", end="")
	print(" Photon's energy: ", end="")
	print(format(phoE(planckConst, c, waves[i]*10**-9), "0.3e"), "J")

print("")
print("Wavelengths:")
print(waves)
