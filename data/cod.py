
import io
import csv
import js

from js import fetch
URL = "https://raw.githubusercontent.com/523a/Fake-News/main/data/lt1.csv"

res = await fetch(URL)
print("1")
text = await res.text()
filename = 'lt1.csv'
print("-2-")
with open(filename, 'w') as f:
    f.write(text)

lt1 = pd.read_csv(filename)



'''csv_content = js.csvContent
reader = csv.DictReader(io.StringIO(csv_content))
headers = []
rows = []
headers = reader.fieldnames
for line in reader:
    rows.append(line)
'''




print("All Ok!")
