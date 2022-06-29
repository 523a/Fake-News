import numpy as np
from js import fetch
URL = "https://raw.githubusercontent.com/523a/Fake-News/main/data/lt1.csv"
res = await fetch(URL)
text = await res.text()
filename = 'lt1.csv'
with open(filename, 'w') as f:
    f.write(text)
lt1 = pd.read_csv(filename)