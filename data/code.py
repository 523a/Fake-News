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

def clean_dataset(df):
    assert isinstance(df, pd.DataFrame), "df needs to be a pd.DataFrame"
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
    return df[indices_to_keep]#.astype(np.float64)

def wordopt(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W"," ",text) 
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)    
    return text
   
   
lt=clean_dataset(lt)
lt.replace([np.inf, -np.inf], np.nan, inplace=True)

lt.dropna()
lt.to_csv('lt.csv', index=False) 

x = lt["text"]
y = lt["class"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

from sklearn.feature_extraction.text import TfidfVectorizer

vectorization = TfidfVectorizer()
xv_train = vectorization.fit_transform(x_train)
xv_test = vectorization.transform(x_test)


###############  LR
from sklearn.linear_model import LogisticRegression

LR = LogisticRegression()
LR.fit(xv_train,y_train)

filename = 'LR_model.sav'
joblib.dump(LR, filename)

# load the model from disk
loaded_model = joblib.load(filename)
result = loaded_model.score(xv_test, y_test)
#print(result)

pred_lr=LR.predict(xv_test)
LR.score(xv_test, y_test)

#print(classification_report(y_test, pred_lr))


def output_lable(n):
    if n == 0:
        return "Fake News"
    elif n == 1:
        return "Not A Fake News"
    
def manual_testing(news1):
    testing_news = {"text":[news1]}
    new_def_test = pd.DataFrame(testing_news)
    new_def_test["text"] = new_def_test["text"].apply(wordopt) 
    new_x_test = new_def_test["text"]
    new_xv_test = vectorization.transform(new_x_test)
    pred_LR = LR.predict(new_xv_test)


    #return print("\n\n LR Prediction: {}".format(output_lable(pred_LR[0])))
    return (output_lable(pred_LR[0]))



import os
from pprint import pprint
import json
apikey = os.getenv('R7F8JAZUaZUEgbei45EDdUY9X74ECHWC', 'tfInspSSsKz5HIiPy4BTVc7lNSCGfGs8')

# Top Stories:
# https://developer.nytimes.com/docs/top-stories-product/1/overview
section = "world"
url4 = f"https://api.nytimes.com/svc/topstories/v2/{section}.json?api-key={apikey}"
json1 = json.load(open_url(url4))
nn="NEWS"

i=1
while i < json1["num_results"]:
    nnn = json1["results"][i]["abstract"]
    nn = nn + "\n" + str(i) + "\n" + nnn + "\n"+ manual_testing(nnn)+ "\n"
    #nn = nn+"<p>" + str(i) + "<br>" + nnn + "<br> "+ manual_testing(nnn)+ "</p>"+"<br>"
    #print(str(manual_testing(nnn)))
    #print(manual_testing(nnn),i,nnn)
    i=i+1
print(nn) 

#str(manual_testing(nnn))   
#div2 = js.document.createElement("div")
#div2.innerHTML = nn
#js.document.body.prepend(div2)
