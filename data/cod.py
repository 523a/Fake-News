# -*- coding: utf-8 -*-

import io
import csv
import js

div1 = js.document.createElement("div")
div1.innerHTML = "<h1> Json получен </h1>"
js.document.body.prepend(div1)

from pyodide.http import open_url
import os
from pprint import pprint
import json


apikey = os.getenv('R7F8JAZUaZUEgbei45EDdUY9X74ECHWC', 'tfInspSSsKz5HIiPy4BTVc7lNSCGfGs8')

# Top Stories:
# https://developer.nytimes.com/docs/top-stories-product/1/overview
section = "world"

url4 = f"https://api.nytimes.com/svc/topstories/v2/{section}.json?api-key={apikey}"
#print(url4)
json1 = json.load(open_url(url4))
#print(json1)




nn="Hello"
#nn=json1["results"][0]["abstract"]
#print(nn)
#print(json1['num_results'])
print("#########################  1 #################################")

i=1
while i < json1["num_results"]:
    nnn = json1["results"][i]["abstract"]
    nn = nn+nnn 
    i=i+1

#with open('FN.json', 'w') as f:
#    json.dump(nn, f)
#print((nn))   
    
#print("All Ok 9 !")
#div2 = js.document.createElement("div")
#div2.innerHTML = nn
#js.document.body.prepend(div2)
#div3 = js.document.createElement("div")
#div3.style.backgroundColor="green"
#js.document.body.append(div3)
#div3.innerText="Какая-то строка"


