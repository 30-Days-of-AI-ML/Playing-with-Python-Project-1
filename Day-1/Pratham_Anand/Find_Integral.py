#!/usr/bin/env python
# coding: utf-8

# In[12]:


import sympy as sp


def main() :
    x = sp.symbols('x')
    i1 = sp.integrate(sp.log(x) * x, x)
    i2 = sp.integrate(x ** 2, x)
    i3 = sp.integrate(sp.tan(sp.sin(x)), x)
    print(i1)
    print(i2)
    print(i3)


if __name__ == "__main__" :
    main()
