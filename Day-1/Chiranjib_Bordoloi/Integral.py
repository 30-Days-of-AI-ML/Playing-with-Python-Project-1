# Run the command below if package not installed
# pip install sympy

# Importing sympy
import sympy as sp

x = sp.symbols('x')

# Expressions
exp1 = x * sp.log(x)
exp2 = x ** 2
exp3 = sp.tan(sp.sin(x))

print("Integration of", exp1, "is", sp.integrate(exp1, x))
print("Integration of", exp2, "is", sp.integrate(exp2, x))
print("Integration of", exp3, "is", sp.integrate(exp3, x))
