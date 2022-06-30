print("1")
import io
import csv
import js

csv_content = js.csvContent

reader = csv.DictReader(io.StringIO(csv_content))
headers = []
rows = []
print("-2-")
headers = reader.fieldnames
for line in reader:
    rows.append(line)





print("All Ok!")
