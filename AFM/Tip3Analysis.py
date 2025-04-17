import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#read in the file 
file_base_name= "Tip3Data" 

data = pd.read_csv(file_base_name +".txt", sep="	", skiprows=1, header=None)
#rename the columns
data.columns = ["freq","amp", "phase"]
data["freq"] = pd.to_numeric(data["freq"], errors='coerce')
data["amp"] = pd.to_numeric(data["amp"], errors='coerce')
data["phase"] = pd.to_numeric(data["phase"], errors='coerce')
data.dropna(inplace=True)

peak_index = data['amp'].idxmax()
w_r = data["freq"][peak_index]
print("Peak at:", w_r)

#defining the model that we are fitting to
def amp_model(w, A0, C1, wr, C2):
    return ( A0 + C1/( (w - wr)**2 + C2))

#guessing some initial parameters to input into the function 
A0 = 0.125
C1 = 250000
C2 = 250000
data["amp model"] = amp_model(data["freq"],A0,C1, w_r, C2)

#optimizing the coefficients 
fit_coefficients, fit_error = curve_fit( f = amp_model, 
                       xdata= data['freq'], 
                       ydata = data['amp'], 
                       p0 = [A0,C1, w_r, C2])

data["opt amp model"] = amp_model(data["freq"],
                             fit_coefficients[0],fit_coefficients[1], 
                             fit_coefficients[2],fit_coefficients[3])

#find the R^2 value of the fit 
corr_matrix = np.corrcoef(data["amp"], data["amp model"])
R_sq_intial = corr_matrix[0,1]**2
print("R^2 of Initial Guess:", R_sq_intial)
corr_matrix2 = np.corrcoef(data["amp"], data["opt amp model"])
R_sq_optimized = corr_matrix2[0,1]**2
print("R^2 of Optimized Fit:", R_sq_optimized)

#plot all the data
plt.figure()
plt.plot(data["freq"], data["amp"], label="raw data")
plt.plot(data["freq"], data["amp model"], label="fit")
plt.plot(data["freq"], data["opt amp model"], label="optimized fit")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amp (V)")
plt.legend()
plt.title("Cantilever 3")
plt.show()
plt.savefig("PY411-amplitude-fitting-cantilever3.png", dpi=300)

# Peak at: 79969.4
# R^2 of Initial Guess: 0.8554953630155305
# # R^2 of Optimized Fit: 0.9742495844399078