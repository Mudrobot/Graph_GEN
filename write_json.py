import json
import os
import sys

with open('query.json', 'r',encoding="utf-8") as file:
    data = json.load(file)
n = len(data)
for i in range(1,n):
    data[i]['lon_delta'] = 0
    data[i]['lat_delta'] = 0
with open('output.json', 'w',encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)