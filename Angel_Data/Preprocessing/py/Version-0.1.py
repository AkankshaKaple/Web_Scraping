#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import warnings
warnings.filterwarnings('ignore')


# In[ ]:


data = pd.read_csv('Column_Selection.csv')
data.head()


# In[ ]:


data.columns


# In[ ]:


data.drop(columns=[ 'Designation', 'Designation 2','Designation 3', 'Detail Tech Requirement','Location',
       'Requirements'], inplace=True)


# In[ ]:


data.head()


# In[ ]:


data.Funding.isna().sum()


# In[ ]:


len(data.Funding)


# In[ ]:


(data.Size.unique())


# In[ ]:


loc_req_des = pd.read_csv("loc_req_des.csv")
data = data.merge(loc_req_des)


# In[ ]:


data.head()


# In[ ]:


data.shape


# In[ ]:


data.to_csv('Version-0.1.csv')


# In[ ]:




