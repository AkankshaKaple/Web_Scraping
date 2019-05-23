import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import warnings
warnings.filterwarnings('ignore')
from sklearn.preprocessing import OneHotEncoder, LabelBinarizer, LabelEncoder
from sklearn.metrics import *
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import import_ipynb
from Optimized_Code import Data_Filteration

test = pd.read_csv("Test.csv")
data = test[:1]
# print(test.head())

# pickle.dump(regression, open('model_housing_data.pkl','wb'))
filtering = pickle.load(open('Filtering_and_Preprocessing.pickle', 'rb'))

data = filtering.column_selection(data)
data = filtering.Filter_Company_Type(data)
data = filtering.Filter_Requirments(data)
data = filtering.Filter_Location(data)
data = filtering.Filter_Desingation(data)
data = filtering.Filter_Contact_Status(data)

classifier = pickle.load(open('Classifier.pickle', 'rb'))

X = pd.DataFrame(data.drop(columns="Contact_Status"))
y = pd.DataFrame(data["Contact_Status"])

X.drop(columns='id', inplace=True)

# print(classifier.predict(X))
print(X.columns)
# accuracy = accuracy_score(y_test, pred)
# print("%.2f" % (accuracy*100), "%")





