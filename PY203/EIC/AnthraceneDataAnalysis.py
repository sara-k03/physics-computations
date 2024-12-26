import matplotlib.pyplot as plt
import numpy as np

file = open("PY203EIC/AnthraceneData.txt", "r")

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
plt.title('Particle in a Box: Anthracene')
plt.xticks(np.arange(0, max(xWavelengths) + 10, 10))
plt.xlim(290, 410)

plt.show()