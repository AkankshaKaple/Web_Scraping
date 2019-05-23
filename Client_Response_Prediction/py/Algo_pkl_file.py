#!/usr/bin/env python
# coding: utf-8

# In[57]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import warnings
warnings.filterwarnings('ignore')
from sklearn.preprocessing import OneHotEncoder, LabelBinarizer, LabelEncoder
from sklearn.metrics import *
from sklearn.ensemble import RandomForestClassifier
from sklearn.grid_search import GridSearchCV
from sklearn.datasets import make_classification
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler


# In[67]:


data = pd.read_csv("Final_data.csv")
df.columns


# In[59]:


df = data.drop(columns=['Unnamed: 0', 'id'], axis=1)


# In[60]:


X = pd.DataFrame(data.drop(columns="Contact_Status"))
y = pd.DataFrame(data["Contact_Status"])


# In[69]:


X.columns


# In[70]:


X.drop(columns=['Unnamed: 0', 'id'], inplace = True)


# In[71]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)


# In[72]:


# Feature Scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# In[73]:


rfc=RandomForestClassifier(random_state=42)

param_grid = { 
    'n_estimators': [200, 500, 1000],
    'max_features': ['auto', 'sqrt', 'log2'],
    'max_depth' : [4,5,6,7,8],
    'criterion' :['gini', 'entropy']
}

CV_rfc = GridSearchCV(estimator=rfc, param_grid=param_grid, cv= 5)
# CV_rfc.fit(X_train, y_train)

rfc1 = RandomForestClassifier(random_state=42, max_features='auto', n_estimators= 200, max_depth=8, criterion='gini')


# In[74]:


X_train.shape, y_train.shape
X_test.shape


# In[75]:


rfc1.fit(X_train, y_train)

pred=rfc1.predict(X_test)

accuracy = accuracy_score(y_test,pred)

print("%.2f" % (accuracy*100), "%")


# In[76]:


import pickle

pickle_out = open("Classifier.pickle", "wb")
pickle.dump(rfc1, pickle_out)
pickle_out.close()


# In[ ]:





# In[ ]:




