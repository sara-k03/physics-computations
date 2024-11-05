from math import pi as pi
import scipy.constants as const

# Energies of single particle states are calculator as E = Ex + Ey
def getEnergy(nx, ny, Ly, Lx):
    
    # Planck's constant divided by 2pi
    hbar = const.hbar

    # Mass of an electron 
    me = const.electron_mass
    
    numerator = hbar * hbar * pi * pi
    denominator = 2 * me
    e0constant = numerator/denominator

    x_component = (nx * nx)/(Lx * Lx)
    y_component = (ny * ny)/(Ly * Ly)
    non_constant_component = x_component + y_component

    energy = e0constant * non_constant_component 

    return f"{energy:.2e}"

f = open("PY203EIC/output.txt", "a")

print("Naphthalene: ", file=f)
print ("HOMO: n = 2", file=f)
print ("LUMO: n = 3", file=f)
print("Lx = 0.485 nm", file=f)
print("Ly = 0.2612 nm", file=f)
print("", file=f)
Lx = 0.485 * (10 ** -9)
Ly = 0.2612 * (10 ** -9)
for nx in range(1, 4): # Stops at n = LUMO
    for ny in range(1, 4):
        print("nx = " + str(nx) + ", ny = " + str(ny), file=f)
        print(str(getEnergy(nx, ny, Lx, Ly)) + " eV", file=f)

print("", file=f)
print("", file=f)

print("Anthracene: ", file=f)
print ("HOMO: n = 3", file=f)
print ("LUMO: n = 3", file=f)
print("Lx = 0.7275 nm", file=f)
print("Ly = 0.2612 nm", file=f)
print("", file=f)
Lx = 0.7275 * (10 ** -9)
Ly = 0.2612 * (10 ** -9)
for nx in range(1, 4): # Stops at n = LUMO
    for ny in range(1, 4):
        print("nx = " + str(nx) + ", ny = " + str(ny), file=f)
        print(str(getEnergy(nx, ny, Lx, Ly)) + " eV", file=f)

print("", file=f)
print("", file=f)

print("Tetracene: ", file=f)
print ("HOMO: n = 3", file=f)
print ("LUMO: n = 3", file=f)
print("Lx = 0.97 nm", file=f)
print("Ly = 0.2612 nm", file=f)
print("", file=f)
Lx = 0.97 * (10 ** -9)
Ly = 0.2612 * (10 ** -9)
for nx in range(1, 4): # Stops at n = LUMO
    for ny in range(1, 4):
        print("nx = " + str(nx) + ", ny = " + str(ny), file=f)
        print(str(getEnergy(nx, ny, Lx, Ly)) + " eV", file=f)

f.close()