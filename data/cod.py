
import io
import csv
import js


from pyodide.http import open_url
import os
from pprint import pprint
import json


apikey = os.getenv('R7F8JAZUaZUEgbei45EDdUY9X74ECHWC', 'tfInspSSsKz5HIiPy4BTVc7lNSCGfGs8')

# Top Stories:
# https://developer.nytimes.com/docs/top-stories-product/1/overview
section = "world"

url4 = f"https://api.nytimes.com/svc/topstories/v2/{section}.json?api-key={apikey}"
print(url4)

json1 = json.load(open_url(url4))

nn=json1["results"][1]["abstract"]
print(nn)
print(json1['num_results'])
r=5
print(r)
i=0
while i < json1["num_results"]:
    nnn = json1["results"][i]["abstract"]
    
    
    #print((nnn),i)
    i=i+1

print("All Ok 9 !")



