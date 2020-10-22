from sympy import *

x = symbols('x')

form1 = x*log(x)
intr1 = integrate(form1)
Print("xlog(x) is ", intr1)

form2 = x*2
intr2 = integrate(form2)
print("x*2 is ", intr2)

form3 = tan(sin(x))
intr3 = integrate(form3)
print("tan(sin(x)) is ", intr3)
