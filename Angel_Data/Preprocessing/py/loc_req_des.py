#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')


# # Merge Location and Requirements

# In[ ]:


location = pd.read_csv("Location.csv")
req = pd.read_csv("Requirements.csv")
location.head()


# In[ ]:


req.head()


# In[ ]:


loc_req = location.merge(req)


# In[ ]:


loc_req.head()


# In[ ]:


req.shape, location.shape, loc_req.shape


# # Merge Designation with Location and Requirements

# In[ ]:


des = pd.read_csv("Desingation.csv")
des.columns


# In[ ]:


des.drop(columns=['Unnamed: 0.1', 'Contact Status'
       ,'Detail Tech Requirement', 'Funding', 'Location', 'Requirements'
       ,'Size','Designation','Designation 2','Designation 3','combined'], inplace=True)


# In[ ]:


des.head()


# In[ ]:


des["Desingations"].unique()


# In[ ]:


loc_req_des = des.merge(loc_req)


# In[ ]:


loc_req_des.head()


# In[ ]:


for i in loc_req_des.columns:
    if '@' in i:
        loc_req_des.drop(columns=i, inplace=True)


# In[ ]:


loc_req_des.head()


# In[ ]:


import csv
loc_req_des.to_csv("loc_req_des.csv")


# In[ ]:




