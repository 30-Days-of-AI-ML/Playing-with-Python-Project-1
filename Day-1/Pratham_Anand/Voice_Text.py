#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install gTTs


# In[7]:



from gtts import gTTS 


import os 

mytext = 'Welcome to my world!'

language = 'en'


myobj = gTTS(text=mytext, lang=language, slow=False) 


myobj.save("welcome.mp3") 

os.system("mpg321 welcome.mp3") 


# In[ ]:




