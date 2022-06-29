import numpy as np
import pandas as pd
from js import fetch
from sklearn.model_selection import train_test_split
from sklearn.ensemble import HistGradientBoostingClassifier, HistGradientBoostingRegressor
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer
from sklearn.compose import make_column_selector
from sklearn.preprocessing import OrdinalEncoder, LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, mean_absolute_percentage_error
from sklearn.metrics import classification_report
import re
import string
import joblib
import sklearn


from js import fetch
import os
#lt = pd.read_csv("lt.csv", names=columns)
print(os.getcwd())

import csv
 
myData = [["first_name", "second_name", "Grade"],
          ['Alex', 'Brian', 'A'],
          ['Tom', 'Smith', 'B']]
 
myFile = open('ex.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)
     
print("Writing complete")

import sys
import js
import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib




LR = LogisticRegression()
filename = 'LR2_model.sav'
joblib.dump(LR, filename)
print("All Ok 4 !")

