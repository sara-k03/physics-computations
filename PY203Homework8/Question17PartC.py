import random
from math import e

def probability_distribution(r):
    r_squared = r * r
    parentheses = 0.5 - (0.5 * r) + ((1/8) * r_squared)
    e_r = e ** (-1 * r)
    return parentheses * r_squared * e_r

z_eff_sum = 0
for i in range(10000):
    r = random.uniform(0, 15)
    r_probability = probability_distribution(r)
    y = random.random()

    while (y > r_probability):
        r = random.uniform(0, 15)
        r_probability = probability_distribution(r)
        y = random.random()
    
    if r > 1:
        z_eff = 1
    else: # greater than or equal to 1
        z_eff = 3
    
    z_eff_sum += z_eff

z_eff_average = z_eff_sum / 10000 
print("Z-Effective =", z_eff_average)