# -*- coding: utf-8 -*-

import io
import csv
import js
import js

div1 = js.document.createElement("div")
div1.innerHTML = "<h1> This element WAS from Python </h1>"
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
print(url4)

json1 = json.load(open_url(url4))

nn=json1["results"][1]["abstract"]

print(nn)
print(json1['num_results'])
print("****************** 1 *****************************")

i=0
пп=[]
while i < json1["num_results"]:
    nnn = json1["results"][i]["abstract"]
    nn=nn+"<p>"+nnn+str(i)+"</p>"+"<br>"
   
    
    print((nn))
    i=i+1

print("All Ok 9 !")

#div2 = js.document.createElement("div")
#div2.innerHTML(nn)
#js.document.body.prepend(div2)



