
import io
import csv
import js
import js

div = js.document.createElement("div")
div.innerHTML = "<h1>Этот документ сгенерировани Python</h1>"
js.document.body.prepend(div)

from pyodide.http import open_url
import os
from pprint import pprint
import json

r=int(50)

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

print(r)
i=0
while i < json1["num_results"]:
    nnn = json1["results"][i]["abstract"]
    div.innerHTML = "<p>"+nnnn+"</p>"
    js.document.body.prepend(div)
    
    print((nnn),i)
    i=i+1

print("All Ok 9 !")


