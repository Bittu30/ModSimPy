#!/usr/bin/env python
# coding: utf-8

# In[2]:


from modsim import *


# In[3]:


bikeshare=State(olin =10, wellesley=2)


# In[4]:


bikeshare.olin


# In[5]:


bikeshare.wellesley


# In[6]:


bikeshare


# In[7]:


bikeshare.olin-=1
bikeshare.wellesley+=1


# In[12]:


def bike_to_wellesley():
    print('Moving bike to wellesley')
    bikeshare.olin-=1
    bikeshare.wellesley+=1


# In[13]:


bike_to_wellesley()


# In[14]:


def bike_to_olin():
    print('Move bike to olin')
    bikeshare.olin+=1
    bikeshare.wellesley-=1


# In[15]:


bike_to_olin()


# In[16]:


flip(0.7)


# In[18]:


if flip(0.5):
    print('heads')
else:
    print('tails')


# In[19]:


if flip(0.5):
    bike_to_wellesley()


# In[20]:


if flip(0.33):
    bike_to_olin()


# In[21]:


def step():
    if flip(0.5):
        bike_to_wellesley()
    if flip(0.33):
        bike_to_olin()


# In[24]:


step()


# In[25]:


def step(p1,p2):
    if flip(p1):
        bike_to_wellesley()
    if flip(p2):
        bike_to_olin()


# In[26]:


step(0.5,0.33)


# In[27]:


for i in range(4):
    bike_to_wellesley()


# In[28]:


results=TimeSeries()


# In[30]:


results[0]=bikeshare.olin


# In[33]:


for i in range(100):
    step(0.3,0.2)
    results[i]=bikeshare.olin


# In[34]:


results.mean()


# In[40]:


results.plot()


# In[43]:


decorate(title='Olin-Wellesley Bikeshare',
xlabel='Time step (min)',
ylabel='Number of bikes')
results.plot();


# In[ ]:




