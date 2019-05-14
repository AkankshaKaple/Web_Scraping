#!/usr/bin/env python
# coding: utf-8

# <b>Features:</b> Following are the features in dataset:
# 
# * __'Added Date'__  --> Date when entry entered
# * __'BANT Status'__ --> 
#     * __B(Budget)__ - Depends on Funding or Minimum salary that the company gives to freshers
#     * __A(Authority)__ - Right Contact person
#     * __N(Need)__ - Company Tech Requirement
#     * __T(Time Frame)__ - Company has to wait for 4 Months for deployment. 
# * __'Co Linkedin URL'__ --> LinkedIn URL
# * __'Company Name'__  --> Name of Comapny
# * __'Contact #2', 'Contact #3'__ --> Contact Number
# * __'Contact Status'__ --> Company's reaction
# * __'Designation','Designation 2', 'Designation 3'__ --> Designation of person we are contacting
# * __'Detail Tech Requirement'__ --> Company's requirments
# * __'Email', 'Email 2', 'Email 3'__ --> Email id of person we are contacting
# * __'FollowUp Date'__ --> Date given by comapny to contact back
# * __'Funding'__ --> Total amount invested into the company
# * __'Linkedin URL'__ --> LinkedIn URL
# * __'Location'__ --> Location of headquarter of the comapny
# * __'Merge status'__ --> Ignore
# * __'Phone 2', 'Phone 3', 'Phone No'__ --> Phone Number
# * __'Primary Contact Person', 'Proimary Contact Person'__
# * __'Remarks'__  --> Ignore
# * __'Requirements'__
# * __'Sales Status'__ --> Ignore
# * __'Segment'__ --> Type of company
# * __'Size'__ --> Number of enployees
# * __'Source'__ --> Ignore

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import warnings
warnings.filterwarnings('ignore')


# In[ ]:


data = pd.ExcelFile("Data.xlsx")


# In[ ]:


df1 = pd.read_excel(data, 'Ashish')
df2 = pd.read_excel(data, 'Deepu')
df3 = pd.read_excel(data, "Rozer")
df4 = pd.read_excel(data, "Shubham")


# In[ ]:


data = pd.concat([df1, df2, df3, df4])


# In[ ]:


df1.shape, df2.shape, df3.shape, df4.shape


# In[ ]:


data.shape


# In[ ]:


data["Designation"].isna().sum(), data["Designation 2"].isna().sum()


# # Drop unwanted columns
# 
# Out of above features useful features are :
# * __'Contact Status'__ --> Company's reaction
# * __'Designation','Designation 2', 'Designation 3'__ --> Designation of person we are contacting
# * __'Detail Tech Requirement'__ --> Company's requirments
# * __'Funding'__ --> Total amount invested into the company
# * __'Location'__ --> Location of headquarter of the comapny
# * __'Segment'__ --> Type of company
# * __'Size'__ --> Number of enployees
# 
# <b>Reasons</b>
# * __'Contact Status'__ --> This is what we are goning to predict
# * __'Designation','Designation 2', 'Designation 3'__ --> If the contact person is technical head  or a descision making person of comapny then he'll easily understant the technical stuff and can make descisions without much dealy.
# * __'Detail Tech Requirement'__ --> If company's requirment matches what we are providing then there is high chance of that company to consider us
# * __'Funding'__ --> If company has low funding then it won't be able to hadle our chargers
# * __'Location'__ --> Location of headquarter of the comapny
# * __'Segment'__ --> Type of company
# * __'Size'__ --> Number of enployees
# 

# In[ ]:


data.drop(columns=['Added Date', 'BANT Status', 'Co Linkedin URL'
                   ,'Contact #2', 'Contact #3','Email','Email 2', 'Email 3', 'FollowUp Date', 'Linkedin URL', 'Phone 2', 'Phone 3'
                   , 'Phone No','Primary Contact Person', 'Proimary Contact Person','Unnamed: 28', 'Unnamed: 29', 'Unnamed: 30', 'Unnamed: 31'
                   ,'Unnamed: 32', 'Unnamed: 33', 'Unnamed: 34', 'Unnamed: 35'
                   ,'Unnamed: 36', "Sales Status", "Segment", "Source", 'Merge status', "Remarks"], inplace = True)


# In[ ]:


data.columns


# In[ ]:


import csv
data.to_csv("Column_Selection.csv")


# # 'Contact Status'
# <h3><b>Replace the values by 1 if company responded else replace by 0.</b></h3>

# In[ ]:


data["Contact Status"].unique()
np.array(data["Contact Status"].fillna("Missing", inplace=True))


# In[ ]:


data["Contact Status"] = (data["Contact Status"].replace(to_replace={'Reminded2','Reminded1','Emailed #1', "Missing"}, value="0", regex=True) )
data["Contact Status"] = (data["Contact Status"].replace(to_replace={'Responded', 'Not Interested', 'Called', 'Call-Disqualified'
       ,'Call-Scheduled', 'Call-Yes', 'Call-Qualified', 'postponed'}, value="1", regex=True) )


# # Requirements

# </h3><b> Make techs as key in dict and save column number as values. Then replace those col by 1 </b> </h3>
# 

# In[ ]:


data["Requirements"].fillna("Missing", inplace = True)


# Remove the brackets and everything within it.

# In[ ]:


l = []
import re
for i in range(len(data)):
    x = re.sub("[\(\[].*?[\)\]]", "", str(np.array(data["Requirements"])[i]))
    l.append(x)


# In[ ]:


l[:4]


# In[ ]:


req = []
for i in l:
    req.append(i.split(","))


# In[ ]:


req[:4]


# In[ ]:


b = []
for i in l:
    b.append(i.split(","))


# In[ ]:


# import itertools
# dict = {}
# c = []
# list_keys = dict.keys()
# for i in range(len(b)):
#     for j in b[i]:
#         j = j.strip().replace(" ", "").lower()
#         j = j.strip().replace("-", "").lower()
#         if j in list_keys:
#             c = []
#             c.append(dict[j])
#             c.append([i])
#             merged = list(itertools.chain(*c))
#             dict[j] = merged
#         else:
#             dict[j] = [i]


# In[ ]:


# (dict.keys())


# In[ ]:


dict["vineeta@fabbag.com"]


# __In the data, few columns contain wrong information. Here Requirement column contain few email ids instead of technologies. To avoid wrong predictions, we need to remove the ones which contain no values or mark it as missing.__

# In[ ]:


d = pd.read_csv("Column_Selection.csv")
d[4839:4840]


# In[ ]:


for i in dict.keys():
    if "@" in i:
        print(dict[i])


# In[ ]:


d[4469:4470]


# In[ ]:


d[4837:4843]


# In[ ]:


d[5751:5752]


# In[ ]:


d[5897:5898]


# In[ ]:


feature_list = dict.keys()
zero_data = np.zeros(shape=(len(data),len(feature_list)))
new_d = pd.DataFrame(zero_data, columns=feature_list)


# In[ ]:


d.head()


# __Convert this dictionary into dataset__

# In[ ]:


for k in range(len(new_d)):
    for i in  dict.keys():
        for j in dict[i]:
            new_d[i][j] = 1 


# In[ ]:


type(new_d)


# In[ ]:


new_d.shape


# In[ ]:


data.shape


# In[ ]:


import csv
new_d.to_csv("Requirements.csv")


# In[ ]:


req_data = pd.read_csv("Requirements.csv")
# whole_data = pd.concat([data, req_data])
# req_data.drop(columns="Unnamed: 0", inplace = True)
req_data.head()


# In[ ]:


data.head()


# In[ ]:


for i in req_data.columns:
    if "@" in i:
        req_data.drop(columns=i, inplace=True)


# In[ ]:


req_data.shape


# In[ ]:


# whole_data.drop(columns="Unnamed: 33", inplace =True)
# whole_data.backend[:2], req_data.backend[:2]


# In[ ]:


whole_data.columns


# In[ ]:


list_req = req_data.columns


# In[ ]:


for i in whole_data.columns:
    if i in list_req:
        whole_data[i].fillna(0, inplace=True)


# In[ ]:


whole_data.head()


# In[ ]:


data.head()


# In[ ]:


data.drop(columns=["Detail Tech Requirement", "Requirements"], inplace = True)


# In[ ]:


data.head()

