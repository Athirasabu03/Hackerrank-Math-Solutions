#!/usr/bin/env python
# coding: utf-8

# #### Task
# ABC  is a right triangle,  at .
# Therefore, .
# 
# Point  is the midpoint of hypotenuse .
# 
# You are given the lengths  and .
# Your task is to find  (angle , as shown in the figure) in degrees.

# In[1]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
# taking the input from user
ab = float(input())
bc = float(input())

# finding the distance 
ac = math.sqrt((ab*ab)+(bc*bc))
bm = ac / 2.0
mc = bm

# equalizing the sides 
b = mc
c = bm
a = bc

# where b=c
# finding the angle in radian
angel_b_radian = math.acos(a / (2*b))

# converting the radian to degree
angel_b_degree = int(round((180 * angel_b_radian) / math.pi))

# printing with degree
print(angel_b_degree,'\u00B0',sep='')


# In[ ]:




