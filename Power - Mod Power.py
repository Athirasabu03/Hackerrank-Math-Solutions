#!/usr/bin/env python
# coding: utf-8

# #### Task
# 
# You are given three integers: , , and . Print two lines.
# On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).

# In[1]:


a,b,m = [int(input()) for _ in '123']
print(pow(a,b),pow(a,b,m),sep='\n')


# In[ ]:




