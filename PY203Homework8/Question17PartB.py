import random
from math import e

def probability_distribution(r):
    r_squared = r * r
    parentheses = 0.5 - (0.5 * r) + ((1/8) * r_squared)
    e_r = e ** (-1 * r)
    return parentheses * r_squared * e_r

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