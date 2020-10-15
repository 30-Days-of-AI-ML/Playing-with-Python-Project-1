#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def main() :
    temp = input("enter temperature : ")
    length = int(len(temp))
    postfix = temp[length - 1]
    if postfix == 'c' or postfix == 'C' :
        c = int(temp[0 : length - 1])
        print(c * (9 / 5) + 32 , "F")
    elif postfix == 'f' or postfix == 'F' :
        f = int(temp[0 : length - 1])
        print((f - 32) * (5 / 9), "C")
    else :
        print("invalid input, enter temperature in either celcius or fahrenhiet")


if __name__ == "__main__" :
    main()
