#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


# In[ ]:


data = pd.read_csv('cont_size_loc_req_des.csv')


# In[ ]:


data.columns


# In[ ]:


data.drop(columns=['Unnamed: 0', 'Unnamed: 0.1','Unnamed: 0.1.1'], inplace=True)


# In[ ]:


data.columns


# In[ ]:


data.shape


# In[ ]:


linkedin = pd.read_csv("Data_with_result-Copy1.csv")
linkedin.columns


# In[ ]:


linkedin.Industry.unique()


# In[ ]:


Service_based = ['Information Technology and Services', 'Computer Software'
                , 'Research''Information Services']


# In[ ]:


Product_based= [ 'Financial Services','Computer Games','E-Learning','Hospital & Health Care']


# Human Resources, Staffing and Recruiting, 'Education Management' # useless

# In[ ]:


others = ['Marketing and Advertising','Internet','Automotive','Events Services','Mechanical or Industrial Engineering'
          ,'Photography','Leisure, Travel & Tourism','Consumer Services', 'Security and Investigations'
         ,'Computer & Network Security']


# __Divide companies into categories__

# In[ ]:


c_type = []
for i in linkedin.Industry:
    if i in Service_based:
        c_type.append("Service_based")
    elif i in Product_based:
        c_type.append("Product_based")
    else:
        c_type.append("Other")
    


# In[ ]:


linkedin.shape, data.shape, len(c_type)


# In[ ]:


linkedin.drop(columns=["Industry", "Type"], inplace=True)


# In[ ]:


linkedin["Company_Type"] = c_type


# In[ ]:


import csv
linkedin.to_csv("link_C_type.csv")


# In[ ]:


d = pd.read_csv("Column_Selection.csv")
d.shape


# In[ ]:


d.columns


# In[ ]:


data["Company_Name"] = d["Company Name"]


# In[ ]:


import csv
data.to_csv("C_name.csv")

