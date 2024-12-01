from scipy.integrate import quad
from math import e as e
from math import pi as pi
from math import inf as infinity

# function to integrate, in this case Maxwell Speed Distribution
def f(v):
    constant_num = 1.67 * (10**-27)
    constant_den = 2 * pi * 1.38 * (10 ** -23) * 15 * (10**6)
    constant_exp = (constant_num/constant_den) ** (1.5)
    constant = 4 * pi * constant_exp

    v_squared = v**2
    expNum = (-1) * (1.67 * (10**-27)) * (v_squared)
    expDen = 2 * (15 * (10**6)) * (1.38 * (10 ** -23))
    exp = expNum/expDen
    e_exp = e ** exp
    return constant * v_squared * e_exp



# integration limits
a = 3.85 * (10 ** 6)  # Lower limit
b = infinity  # Upper limit

# Perform the integration
result, error = quad(f, a, b)

print(f"The integral of f(x) from {a} to {b} is approximately {result}")