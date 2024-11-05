import matplotlib.pyplot as plt
import numpy as np

file = open("PY203EIC/NaphthaleneData.txt", "r")

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
plt.title('Particle in a Box: Naphthalene')
plt.xticks(np.arange(0, max(xWavelengths) + 5, 5))
plt.xlim(250, 300)
plt.ylim(-1, 1.3)

plt.show()