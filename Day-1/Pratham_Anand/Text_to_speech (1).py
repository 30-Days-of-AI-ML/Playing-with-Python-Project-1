#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()
