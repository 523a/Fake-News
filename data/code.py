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
from pprint import pprint
import json
apikey = os.getenv('R7F8JAZUaZUEgbei45EDdUY9X74ECHWC', 'tfInspSSsKz5HIiPy4BTVc7lNSCGfGs8')

# Top Stories:
# https://developer.nytimes.com/docs/top-stories-product/1/overview
section = "world"
URL = f"https://api.nytimes.com/svc/topstories/v2/{section}.json?api-key={apikey}"
res = await fetch(URL)
json1 = await res.json()


pprint(json1.results[2].abstract)
pprint(json1.num_results)



print("All Ok!")
