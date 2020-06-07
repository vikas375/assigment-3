#!/usr/bin/env python
# coding: utf-8

# # Write a function to compute 5/0 and use try/except to catch the exceptions. 

# In[1]:


def divide():
    return 5/0

try:
    divide()
except ZeroDivisionError as ze:
    print("Why on earth you are dividing a number by ZERO!!")
except:
    print("Any other exception")


# # Implement a Python program to generate all sentences

# In[3]:


subject=["Americans", "Indians"]
verb=["Play", "watch"]
obj=["Baseball","cricket"]

# Use list comprehension instead of looping over each of the predicates
sentence_list = [(sub+" "+ vb + " " + ob) for sub in subject for vb in verb for ob in obj]
for sentence in sentence_list:
 print (sentence)


# #  function so that the columns of the output matrix are powers of the input vector.

# In[5]:


import numpy as np
x = np.array([1, 2, 3, 5])
N = 3
np.vander(x, N)


# In[6]:


np.column_stack([x**(N-1-i) for i in range(N)])


# In[7]:


x = np.array([1, 2, 3, 5])
np.vander(x)


# In[8]:


np.vander(x, increasing=True)


# In[ ]:




