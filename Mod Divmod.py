#!/usr/bin/env python
# coding: utf-8

# #### Task
# Read in two integers,  and , and print three lines.
# The first line is the integer division  (While using Python2 remember to import division from __future__).
# The second line is the result of the modulo operator: .
# The third line prints the divmod of  and .

# In[1]:


print('{0}\n{1}\n({0}, {1})'.format(*divmod(int(input()), int(input()))))


# In[ ]:




