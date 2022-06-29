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

import csv
import io
import js

from js import fetch
import os
#lt = pd.read_csv("lt.csv", names=columns)
print(os.getcwd())


 
myData = [["first_name", "second_name", "Grade"],
          ['Alex', 'Brian', 'A'],
          ['Tom', 'Smith', 'B']]
 
myFile = open('ex1.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)
     
print("Writing complete 2")


from sklearn.linear_model import LogisticRegression

LR = LogisticRegression()
filename = 'LR2_model.sav'
joblib.dump(LR, filename)



########################################
csv_content = js.csvContent

reader = csv.DictReader(io.StringIO(csv_content))
headers = []
rows = []

headers = reader.fieldnames
for line in reader:
    rows.append(line)


print("All Ok 7 !")

