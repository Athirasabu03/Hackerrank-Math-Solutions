#!/usr/bin/env python
# coding: utf-8

# You are given a positive integer .
# Your task is to print a palindromic triangle of size .

# In[1]:


for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print (((10**i - 1)//9)**2)


# In[ ]:




