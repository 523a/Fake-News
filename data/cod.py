
import io
import csv
import js

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
print(lt)

print("Writing complete 4")


'''csv_content = js.csvContent
reader = csv.DictReader(io.StringIO(csv_content))
headers = []
rows = []
headers = reader.fieldnames
for line in reader:
    rows.append(line)
'''




print("All Ok!")
