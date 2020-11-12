#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sympy as sp
from sympy import *


# In[2]:


x = sp.symbols('x')


# In[3]:


form1 = x* sp.log(x)


# In[4]:


form2 = x**2


# In[5]:


form3 = tan(sin(x))


# In[6]:


intr3 = sp.integrate(form3)


# In[7]:


intr1 = sp.integrate(form1, x)
intr2 = sp.integrate(form2, x)


# In[9]:


print("integration of ", form1, "is :: ", intr1)
print("integration of ", form2, "is :: ", intr2)
print("tan(sin(x)) is ", intr3)


# In[ ]:




