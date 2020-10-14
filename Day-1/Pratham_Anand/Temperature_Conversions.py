#!/usr/bin/env python
# coding: utf-8

# In[3]:


def main():
    temp = input("enter the temperature")
    length = int(len(temp))
    postfix = temp[length - 1]

    if postfix == 'C' or postfix == 'c':

        celsius = int(temp[0:length - 1])
        farenheit = 9 / 5 * celsius + 32

        print("Temp in farenheit is :: ", farenheit)
    elif postfix == 'F' or postfix == 'f':

        farenheit = int(temp[0:length - 1])
        celsius = 5 / 9 * (farenheit - 32)

        print("Temp in Celsius is :: ", celsius)
    else:
        print("input format error!")


if __name__ == "__main__":
    main()


# In[ ]:




