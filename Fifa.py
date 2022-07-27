#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd 
from matplotlib import pyplot as plt
import seaborn as sns


# In[4]:


fifa = pd.read_csv(r'C:\Users\Sahil\Desktop\players_20.csv')


# In[5]:


fifa.head()


# In[6]:


fifa.shape


# In[7]:


fifa['nationality'].value_counts()


# In[8]:


fifa['nationality'].value_counts()[0:10]


# In[9]:


fifa['nationality'].value_counts()[0:5].index


# In[31]:


plt.figure(figsize=(5,5))
plt.bar(list(fifa['nationality'].value_counts()[0:5].keys()),list(fifa['nationality'].value_counts()[0:5]),color="grey")
plt.show() 


# In[11]:


player_salary= fifa[['short_name', 'wage_eur']]


# In[12]:


player_salary.head()


# In[15]:


player_salary = player_salary.sort_values(by=['wage_eur'],ascending=False)


# In[16]:


player_salary.head()


# In[27]:


plt.figure(figsize=(8,5))
plt.bar(list(player_salary['short_name'])[0:5],list(player_salary['wage_eur'])[0:5],color='skyblue')
plt.show()


# In[32]:


fifa['nationality']=='Germany'


# In[34]:


Germany= fifa[fifa['nationality']=='Germany']
Germany.head()


# In[35]:


Germany.sort_values(by=['height_cm'],ascending=False).head()


# In[36]:


Germany.sort_values(by=['weight_kg'],ascending=False).head()


# In[37]:


Germany.sort_values(by=['wage_eur'],ascending=False).head()


# In[39]:


Germany[['short_name','wage_eur']]


# In[38]:


Germany[['short_name','wage_eur']].sort_values(by=['wage_eur'],ascending=False).head()


# In[40]:


player_shooting=fifa[['short_name','shooting']]


# In[43]:


player_shooting.sort_values(by=['shooting'],ascending=False).head()


# In[44]:


player_defending=fifa[['short_name','defending','nationality','club']]


# In[46]:


player_defending.sort_values(by=['defending'],ascending=False).head()


# In[47]:


real_madrid=fifa[fifa['club']=='Real Madrid']


# In[49]:


real_madrid.sort_values(by=['wage_eur'],ascending=False).head()


# In[50]:


real_madrid.sort_values(by=['shooting'],ascending=False).head()


# In[51]:


real_madrid.sort_values(by=['defending'],ascending=False).head()


# In[52]:


real_madrid['nationality'].value_counts()

