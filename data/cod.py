
import io
import csv
import js


import os
from pprint import pprint
import json
apikey = os.getenv('R7F8JAZUaZUEgbei45EDdUY9X74ECHWC', 'tfInspSSsKz5HIiPy4BTVc7lNSCGfGs8')

# Top Stories:
# https://developer.nytimes.com/docs/top-stories-product/1/overview
section = "world"

url4 = f"https://api.nytimes.com/svc/topstories/v2/{section}.json?api-key={apikey}"

json1 = json.loads(open_url(url4).decode("utf-8"))

pprint(json1.results[2].abstract)
pprint(json1.num_results)

#lt3 = pd.read_csv(open_url(url3))
#json1 = fetch(URL).json()

print("All Ok 9 !")




'''
from js import fetch
URL ="https://raw.githubusercontent.com/523a/Fake-News/main/data/lt1.csv"

myData = [["first_name", "second_name", "Grade"],
          ['Alex', 'Brian', 'A'],
          ['Tom', 'Smith', 'B']]
 myFile = open('ex1.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)
lt = pd.read_csv("ex1.csv")

print("Writing complete 4")

csv_content = js.csvContent
reader = csv.DictReader(io.StringIO(csv_content))
headers = []
rows = []
headers = reader.fieldnames
for line in reader:
    rows.append(line)

print("All Ok!")
'''
