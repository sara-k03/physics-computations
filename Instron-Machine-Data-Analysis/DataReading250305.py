import numpy as np
import matplotlib.pyplot as plt

file = open("Instron-Machine-Data-Analysis/periodic_clipped_1.5mm_80mm_a1.0_1.csv", "r")

# Load the file and skip the header
data = np.genfromtxt(file, delimiter=',', skip_header=1, usecols=(2, 3))

# Extract displacement (mm) and force (kN -> N)
xDisp = data[:, 0]  # Displacement in mm
yLoad = data[:, 1] * 1000  # Force in N (convert from kN)

# Split the data
split_index = 624
xDisp1, yLoad1 = xDisp[:split_index], yLoad[:split_index]  # Trial 1 
xDisp2, yLoad2 = xDisp[split_index:], yLoad[split_index:]  # Trial 2

# Plot the two segments
plt.plot(xDisp1, yLoad1, label='Trial 1 - 1mm Disp.', color='blue', linestyle='-')
plt.plot(xDisp2, yLoad2, label='Trial 2 - 1.5mm Disp', color='red', linestyle='-')

# Add labels, legend, and grid
plt.xlabel('DISPLACEMENT (mm)')
plt.ylabel('LOAD (N)')
plt.title('Displacement vs Load for Periodic-Clipped-1.5mm-80mm-a=1')
plt.legend()
plt.grid(True)
plt.show()
