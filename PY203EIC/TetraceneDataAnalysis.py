import matplotlib.pyplot as plt
import numpy as np

file = open("PY203EIC/TetraceneData.txt", "r")

arr = file.readlines()

xWavelengths = []
yAbsorption = []

tracker = 0
for each in arr:
    eachArr = each.split("\t")
    xWavelengths.append(float(eachArr[0]))
    yAbsorption.append(float(eachArr[1].strip()))
    tracker = tracker + 1


plt.plot(xWavelengths, yAbsorption, ".")

plt.xlabel('Wavelength (nm)')
plt.ylabel('Absorption (AU)')
plt.title('Particle in a Box: Tetracene')
plt.xticks(np.arange(0, max(xWavelengths) + 15, 15))
plt.xlim(320, 500)
plt.ylim(0, 2)

plt.show()