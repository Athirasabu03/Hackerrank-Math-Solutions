#!/usr/bin/env python
# coding: utf-8

# #### Task
# You are given a complex . Your task is to convert it to polar coordinates.
# 
# #### Input Format
# 
# A single line containing the complex number . Note: complex() function can be used in python to convert the input as a complex number.
# 
# #### Constraints
# 
# Given number is a valid complex number
# 
# #### Output Format
# 
# Output two lines:
# The first line should contain the value of .
# The second line should contain the value of .

# In[1]:


import cmath
m=complex(input())
print(abs(m))
print(cmath.phase(m))


# In[ ]:




