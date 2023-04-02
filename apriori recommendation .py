#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install apriori 


# In[2]:


t = [['A','B','C'],['A','C'],['A','D'],['B','E','F']]
t


# In[3]:


from apyori import apriori 
rules = apriori(t,min_support=0.5,min_confidence=0.5,min_lift= 1.1, min_length=2)
list(rules)


# In[11]:


import pandas as pd 
import numpy as np
data = pd.read_csv("/home/pranjal/Documents/sem 2/data set/GroceryStoreDataSet.csv", header= None)
data.head()


# In[13]:


l1 = data.values.tolist()
l1


# In[17]:


from apyori import apriori 
rules = apriori(l1,min_support=0.03,min_confidence=0.3,min_lift= 3)
list(rules)


# In[2]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

df = pd.read_csv("/home/pranjal/Documents/sem 2/data set/store_data.csv",header = None)
df


# In[3]:


# list conversion 
df.values.tolist()


# In[4]:


#create a list T and append only if the earlier list has not null values 
T = []
for i in range(len(df)):
    T.append([str(df.values[i,j]) for j in range(0,20) if str(df.values[i,j])!= 'nan'])
T


# In[17]:


from apyori import apriori 
rules = apriori(T,min_support= 0.003, min_confidence= 0.30,min_lifts=2,min_length=2)
list(rules)


# In[ ]:


#check max sold items 


# In[18]:


#convert values into array 
D = df.values.ravel()
import collections 
value = collections.Counter(D)
value


# In[19]:


value.items()


# In[24]:


DF = pd.DataFrame(value.items())
DF


# In[60]:


DF1 = DF.rename(columns={0:"Items",1:"T"})
DF1


# In[61]:


DF1.sort_values(by ="T",ascending = False)[1:]

