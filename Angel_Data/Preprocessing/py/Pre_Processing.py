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


data = pd.read_csv("Column_Selection.csv")
data.head()


# In[ ]:


data.head()


# # Location

# In[ ]:


loc = data.Location


# In[ ]:


data.Location.unique()


# # Change Gurugoan by Gurgaon 

# In[ ]:


import re
location = []
for i in range(len(data)):
    value = re.split('; |, |/',str(loc[i]))
    if "Gurugoan" in value:
        words = [w.replace('Gurugoan', 'Gurgaon') for w in re.split('; |, |/',str(data["Location"][i]))]
        location.append(words)
    else:
        location.append(value)


# In[ ]:


lo = ['Bengaluru', 'Mumbai', 'Pune', 'Hyderabad', 'Gurugram', 'Chennai', 'Noida', 'Delhi', 'Kolkata', 'Gurgaon']


# In[ ]:


import itertools
loc_dict = {}

for i in range(len(data)):
    for j in location[i]:
        if j in lo and j in loc_dict.keys():
            c = []
            c.append(loc_dict[j])
            c.append([i])
            merged = list(itertools.chain(*c))
            loc_dict[j] = merged
        elif j not in lo and "Others" in loc_dict.keys():
            c = []
            c.append(loc_dict["Others"])
            c.append([i])
            merged = list(itertools.chain(*c))
            loc_dict["Others"] = merged
        elif j not in loc_dict.keys():
            if j in lo:
                loc_dict[j] = [i]  
            else:
                loc_dict["Others"] = [i]
        print(loc_dict)


# In[ ]:


len(loc_dict["Others"])


# In[ ]:


feature_list = loc_dict.keys()
zero_data = np.zeros(shape=(len(data),len(feature_list)))
new_d = pd.DataFrame(zero_data, columns=feature_list)


# In[ ]:


# for k in range(len(new_d)):
#     for i in  loc_dict.keys():
#         for j in loc_dict[i]:
#             new_d[i][j] = 1 


# In[ ]:


# import csv
# new_d.to_csv("Location.csv")


# # Designation

# __Here replace designation of the contact person by one which it at higher rank in hierarchy__

# In[ ]:


data["Designation"].fillna("Missing", inplace=True)
data["Designation 2"].fillna("Missing", inplace=True)
data["Designation 3"].fillna("Missing", inplace=True)


# In[ ]:


data["combined"] = data["Designation"].str.cat(data[["Designation", "Designation 2", "Designation 3"]].astype(str), sep="/")


# In[ ]:


comb = (data.combined).str.split("/")


# In[ ]:


founder = ["F","Founder","CF", "Co-founder", "President", "Director", "MD", "Founder & CEO"
           , "Owner", "cbo", "CEO & Cofounder",'Co-Founder & CTO', 'Co-Founder', 'Co-Founder & CPO'
           ,'Co-Founder & MD',  'Co-founder & CBO','CEO & Founder','CEO & Cofounder', 'Co-Founder', 'Co-founder', 'Sugandhi'
           ,'Co-Founder & CPO', 'Co-Founder & CEO', 'Co-Founder & CTO','CoFounder & CEO', 'Co-Founder & MD'
           , 'Co-founder & CTO','MD & CEO','Cofounder & COO', 'Cofounder', 'Founder & COO', 'Cofounder & CEO'
           , 'Cofouncder & CEO','Founder & MD','Cofounder & CTO','founder']

vp = ["Associate VP","VP", 'SVP', 'Vice President', 'VP HOO','AVP ','VP HR', 'AVP-Technology','Excecutive Director'
     , 'City Head', 'Sr VP']

ceo = ["CEO", "CTO", 'MD & CTO', 'Sr Pricipal Consultant',  'CMO','India Head & Chief Engg Officer','COO', 'CEO & Director']

hr = ["HR"," VP HR", "Director-HR", 'Senior Director HR', 'Global Head-HR','Manager HR','Director HR'
      ,'HR Director','Tech HR', 'VP HR','Head HR','Director-TA', 'Director-TA']

Head_engg = ['Head Engg',"HR & TA Head", 'Co-Founder & Data Center Automation Specialist', 'Head od Software Dev'
            ,"Head od Software Dev", "TA", "Head TA", 'VP TA', 'Head IT', 'VP IT','Head of India Engg','GM IT'
             , 'Director of Technology','VP of rtechnology', 'VP Tech','Director of Engg','GM IT','GM','TA Lead'
             ,'VP Tech','Director of Technology','Global Head','Director Technology', 'Head of Tech','Director & Head Engg' 
            , 'Head of Technology','Head Product Engg', 'Engg Manager', 'Principal Engg','Director Engg', 'Sr TA Manager']


# In[ ]:


l = []
founder = ["CF"]
for i in comb[:5]:
    if any(item in i for item in founder):
        print(i)
        print("y")
#         l.append("Founder")'Director & Head Engg'


# In[ ]:


l = []
for i in comb:
    if any(item in i for item in founder):
        l.append("Founder")
    elif any(item in i for item in vp):
        l.append("VP")
    elif any(item in i for item in ceo):
        l.append("CEO")
    elif any(item in i for item in hr):
        l.append("HR")
    elif all(item in i for item in ["Missing"]):
        l.append("Missing")
    elif any(item in i for item in Head_engg):
        l.append("Head_engg")
    else:
        l.append(i[0])


# In[ ]:


data["Desingations"] = l


# In[ ]:


data.columns


# In[ ]:


data.head()


# In[ ]:


import csv
data.to_csv("Desingation.csv")


# In[ ]:


len(data["Desingations"].unique())


# In[ ]:


data["Desingations"].unique()


# In[ ]:




