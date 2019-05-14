#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import warnings
warnings.filterwarnings('ignore')
from sklearn.preprocessing import OneHotEncoder, LabelBinarizer, LabelEncoder
from sklearn.metrics import *


# In[ ]:


data = pd.read_csv("Final_Data.csv")


# In[ ]:


data.drop(columns=["Company_Name", "Unnamed: 0", "Unnamed: 0.1"], inplace=True)


# * __For Company_Type__ 
#     * __0__ - Startup
#     * __1__ - Non-Startup 
# * __For Company_Name__ 
#     * __0__ - No respose from client
#     * __1__ - Client responded 
#    

# In[ ]:


# ax = sb.countplot(x="Contact Status", data=data,  hue="Company_Type")


# In[ ]:


# plt.figure(figsize=(10,10))
# sb.heatmap(data.corr())


# # Seperating Feature and label

# In[ ]:


X = pd.DataFrame(data.drop(columns="Contact Status"))
y = pd.DataFrame(data["Contact Status"])


# # Divide the data into 1:3 ratio

# In[ ]:


from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# # Apply Random Forest Algorithm on the data

# In[ ]:


# Fitting Random Forest Classification to the Training set
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 128, criterion = 'gini', random_state = 55)
classifier.fit(X_train, y_train)


# In[ ]:


# Predicting the Test set results
y_pred = classifier.predict(X_test)


# In[ ]:


# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
cm


# In[ ]:


f1_score(y_test, y_pred), accuracy_score(y_test, y_pred)


# # Apply SVM Algorithm on the data

# In[ ]:


# Fitting SVC Classification to the Training set
from sklearn.svm import SVC
classifier = SVC(kernel = 'linear', random_state = 42)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
cm


# In[ ]:


accuracy_score(y_test, y_pred), f1_score(y_test, y_pred)  


# # Logistic regression

# In[ ]:


from sklearn.linear_model import LogisticRegression
classify = LogisticRegression(random_state=45)
classify.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
cm


# In[ ]:


accuracy_score(y_test, y_pred), f1_score(y_test, y_pred)  


# # Decision Tree Classification

# In[ ]:


# Fitting Decision Tree Classification to the Training set
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
cm


# In[ ]:


accuracy_score(y_test, y_pred), f1_score(y_test, y_pred)  


# # KNN

# In[ ]:


from sklearn.neighbors import KNeighborsClassifier
classify = KNeighborsClassifier(n_neighbors = 3, metric = "minkowski", p = 2)
classify.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
cm


# In[ ]:


accuracy_score(y_test, y_pred), f1_score(y_test, y_pred)  


# # Decision Tree Using Bagging

# In[ ]:


from sklearn.ensemble import BaggingClassifier
from sklearn import tree
model = BaggingClassifier(tree.DecisionTreeClassifier(random_state=1))
model.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
cm, model.score(X_test,y_test)


# In[ ]:


accuracy_score(y_test, y_pred), f1_score(y_test, y_pred)  


# # AdaBoost Classifier

# In[ ]:


from sklearn.ensemble import AdaBoostClassifier
model = AdaBoostClassifier(random_state=1)
model.fit(X_train, y_train)
model.score(X_test,y_test)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
cm


# In[ ]:


accuracy_score(y_test, y_pred), f1_score(y_test, y_pred), model.score(X_test,y_test)


# # Gradient Boosting Classifier

# In[ ]:


from sklearn.ensemble import GradientBoostingClassifier
model= GradientBoostingClassifier(learning_rate=0.01,random_state=1)
model.fit(X_train, y_train)
model.score(X_test,y_test)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
cm


# In[ ]:


accuracy_score(y_test, y_pred), f1_score(y_test, y_pred), model.score(X_test,y_test)

