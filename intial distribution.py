#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


Po=[[0.8,0.2],[0.3,0.7]]


# In[3]:


intial_dis=[1,0]


# In[4]:





# In[ ]:





# In[5]:


d=[[]]
for i in range(200):
    d+=[[]]


# In[6]:


d[0]=[0,1,0]


# In[7]:


def final_dis(intial_dis):
    for i in range(200):
        b=list(np.dot(intial_dis,Po))
        d[i+1]=(i+1,b[0],b[1])
        intial_dis=b
        df = pd.DataFrame(d,columns = ['n_step_transition', 'probability_1','probability_2'])
    return df
    


# In[8]:


df=final_dis(intial_dis)
df


# In[9]:


fig, ax1 = plt.subplots()
  
color = 'tab:blue'
ax1.set_xlabel('n_step_transition')
ax1.set_ylabel('probability_1', color = color)
ax1.plot(df['n_step_transition'],df['probability_1'], color = color)
ax1.tick_params(axis ='y', labelcolor = color)
  
ax2 = ax1.twinx()
  
color = 'tab:green'
ax2.set_ylabel('probability_2', color = color)
ax2.plot(df['n_step_transition'],df['probability_2'], color = color)
ax2.tick_params(axis ='y', labelcolor = color)
  
fig.suptitle('matplotlib.axes.Axes.twinx() function Example\n\n', fontweight ="bold")
  
plt.show()


# In[14]:


intial_dis=[0,1]


# In[15]:


d[0]=[0,0,1]
def final_dis(intial_dis):
    for i in range(200):
        b=list(np.dot(intial_dis,Po))
        d[i+1]=(i+1,b[0],b[1])
        intial_dis=b
        df = pd.DataFrame(d,columns = ['n_step_transition', 'probability_1','probability_2'])
    return df
    


# In[16]:


df=final_dis(intial_dis)
df


# In[13]:


fig, ax1 = plt.subplots()
  
color = 'tab:blue'
ax1.set_xlabel('n_step_transition')
ax1.set_ylabel('probability_1', color = color)
ax1.plot(df['n_step_transition'],df['probability_1'], color = color)
ax1.tick_params(axis ='y', labelcolor = color)
  
ax2 = ax1.twinx()
  
color = 'tab:green'
ax2.set_ylabel('probability_2', color = color)
ax2.plot(df['n_step_transition'],df['probability_2'], color = color)
ax2.tick_params(axis ='y', labelcolor = color)
  
fig.suptitle('matplotlib.axes.Axes.twinx() function Example\n\n', fontweight ="bold")
  
plt.show()

