import pandas as pd
'''
import numpy as np
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
'''
import csv
import io
import js
import os

from js import fetch


#lt = pd.read_csv("lt.csv", names=columns)
print(os.getcwd())


 
myData = [["first_name", "second_name", "Grade"],
          ['Alex', 'Brian', 'A'],
          ['Tom', 'Smith', 'B']]
 
myFile = open('ex1.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)

lt = pd.read_csv("ex1.csv")
print(lt)

print("Writing complete 4")


from sklearn.linear_model import LogisticRegression

LR = LogisticRegression()
filename = 'LR2_model.sav'
joblib.dump(LR, filename)



########################################
#import altair as alt
#import panel as pn
from pyodide.http import open_url

url = 'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-07-28/penguins.csv'
penguins = pd.read_csv(open_url(url)).dropna()
cols = list(penguins.columns)[2:6]



print("All Ok 9 !")

