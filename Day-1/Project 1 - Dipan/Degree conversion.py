#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Q4.Convert given temp from celsius to faren. and vice-versa
n = float(input("Enter a temp :"))
ch = str(input("Do you want to convert it to 1.Celsius or, 2.Farenheit ??\n"))
if ch == "1":
    print("Temperature in celsius is:", (n-32)/1.8)
else:
    print("temperature in farenheit is:", (n*1.8)+32)


# In[ ]:




