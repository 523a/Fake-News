import pandas as pd
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
import csv
import io
import js
import os

################ LOAD
################

from pyodide.http import open_url

url1 = 'https://raw.githubusercontent.com/523a/Fake-News/main/data/lt1.csv'
lt1 = pd.read_csv(open_url(url1)).dropna()
url2 = 'https://raw.githubusercontent.com/523a/Fake-News/main/data/lt1.csv'
lt2 = pd.read_csv(open_url(url2)).dropna()
url3 = 'https://raw.githubusercontent.com/523a/Fake-News/main/data/lt1.csv'
lt3 = pd.read_csv(open_url(url3)).dropna()

lt = lt1.append(lt2, ignore_index=True) 
lt = lt.append(lt3, ignore_index=True) 








 

###############  LR
from sklearn.linear_model import LogisticRegression

LR = LogisticRegression()
filename = 'LR2_model.sav'
joblib.dump(LR, filename)





print("All Ok 9 !")

