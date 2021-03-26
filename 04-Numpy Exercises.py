#!/usr/bin/env python
# coding: utf-8

# ___
# 
# Mr. Yogesh P Murumkar (Mob. 9657080905)
# 
# www.youtube.com/yogeshmurumkar
# ___

# # NumPy Exercises 
# 
# Now that we've learned about NumPy let's test your knowledge. We'll start off with a few simple tasks, and then you'll be asked some more complicated questions.

# #### Import NumPy as np

# In[1]:


import numpy as np


# #### Create an array of 10 zeros 

# In[3]:


np.zeros(10)


# #### Create an array of 10 ones

# In[4]:


np.ones(10)


# #### Create an array of 10 fives

# In[5]:


np.ones(10)*5


# #### Create an array of the integers from 10 to 50

# In[6]:


np.arange(10,51)


# #### Create an array of all the even integers from 10 to 50

# In[7]:


np.arange(10,51,2)


# #### Create a 3x3 matrix with values ranging from 0 to 8

# In[8]:


np.arange(0,9).reshape(3,3)


# #### Create a 3x3 identity matrix

# In[10]:


np.eye(3,3)


# #### Use NumPy to generate a random number between 0 and 1

# In[12]:


np.random.rand()


# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

# In[13]:


np.random.randn(25)


# #### Create the following matrix:

# In[20]:


np.arange(0.01,1.01,0.01).reshape(10,10)


# In[21]:


np.linspace(0.01,1,100).reshape(10,10)


# In[35]:


np.linspace(0.01,1,)


# #### Create an array of 20 linearly spaced points between 0 and 1:

# In[52]:


np.linspace(0,1.1,20)


# ## Numpy Indexing and Selection
# 
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

# In[22]:


arr=np.arange(1,26).reshape(5,5)


# In[23]:


arr


# In[24]:


arr=np.arange(1,26).reshape(5,5)


# In[39]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[25]:


arr[2:,1:]


# In[40]:





# In[27]:


arr[3,4]


# In[29]:


arr[0,2]


# In[29]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[30]:


arr[3,4]


# In[30]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[32]:


array=np.arange(1,26).reshape(5,5)


# In[33]:


array


# In[37]:


array[0:3,1:2]


# In[42]:





# In[31]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[39]:


array[4:]


# In[46]:





# In[42]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
array[3:]


# In[49]:





# ### Now do the following

# #### Get the sum of all the values in mat

# In[44]:


array


# In[45]:


array.sum()


# In[50]:





# #### Get the standard deviation of the values in mat

# In[46]:


array.std()


# #### Get the sum of all the columns in mat

# In[47]:


array[0].sum()


# In[48]:


arr[:,4:]


# In[51]:


array.sum(axis=0)


# # Great Job!
