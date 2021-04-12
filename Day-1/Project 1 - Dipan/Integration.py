"""
Playing-with-Python-Project-1
            - Dipan Mandal
"""
# Q1.Integration

import sympy as sp
from sympy import *

x = Symbol('x')
integrate((x * log(x)), x)  # integration of xlog(x)
integrate(x**2, x)
# integration of tan(sin(x)), but still doesnt work out!
sp.integrate(sp.tan(sp.sin(x)), x)
