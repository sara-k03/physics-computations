"""
Exercise 17.3.1, Shankar Quantum
"""
import sympy as sp

# Symbols
r, theta, phi = sp.symbols('r theta phi', real=True, nonnegative=True)
a0, e, E = sp.symbols('a_0 e E', positive=True)

# Radial wavefunctions
R20 = (1 / (2*a0))**sp.Rational(3, 2) * 2 * (1 - r/(2*a0)) * sp.exp(-r/(2*a0))
R21 = (1 / (2*a0))**sp.Rational(3, 2) * (1/sp.sqrt(3)) * (r/a0) * sp.exp(-r/(2*a0))

# Spherical harmonics
Y00 = 1 / sp.sqrt(4*sp.pi)
Y10 = sp.sqrt(3 / (4*sp.pi)) * sp.cos(theta)

# Full wavefunctions
psi200 = R20 * Y00
psi210 = R21 * Y10

# Z = r cos(theta)
Z = r * sp.cos(theta)

# Integrating over volume --> r^2 sin(theta) dr dtheta dphi
integrand = sp.conjugate(psi200) * Z * psi210 * r**2 * sp.sin(theta)

Z_element = sp.integrate(
    integrand,
    (r, 0, sp.oo),
    (theta, 0, sp.pi),
    (phi, 0, 2*sp.pi),
)
Z_element = sp.simplify(Z_element)

Delta = sp.simplify(e * E * Z_element)
print("Δ=", Delta)