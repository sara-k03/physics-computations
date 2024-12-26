import random
from math import e

def probability_distribution(r):
    r_tothe_fourth = r ** 4
    e_negative_r = e ** (r * -1)
    probability = (r_tothe_fourth * e_negative_r) / 24
    return probability

r = random.uniform(0, 15)
r_probability = probability_distribution(r)
y = random.random()

while (y > r_probability):
    r = random.uniform(0, 15)
    r_probability = probability_distribution(r)
    y = random.random()

print("r =", r)
print("P(r) =", r_probability)
print("y =", y)

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