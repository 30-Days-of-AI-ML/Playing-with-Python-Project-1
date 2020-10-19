# importing our sympy module 
import sympy as sp

# defining our variable
x = sp.Symbol('x')
sp.init_printing(use_unicode=True)

# our questions of integral
ques1 = x * sp.log(x)
ques2 = x ** 2
ques3 = sp.tan(sp.sin(x))

# solving the integrals using sp.integrate
print(f"The integration of {ques1} is: {sp.integrate(ques1)}.")
print(f"The integration of {ques1} is: {sp.integrate(ques2)}.")
print(f"The integration of {ques1} is: {sp.integrate(ques3)}.")
