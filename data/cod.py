
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

pprint(json1.results[2].abstract)
pprint(json1.num_results)

#lt3 = pd.read_csv(open_url(url3))
#json1 = fetch(URL).json()

print("All Ok 9 !")



