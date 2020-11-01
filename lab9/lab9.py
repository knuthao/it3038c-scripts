import json
import requests



r = requests.get('http://localhost:3000')

data = r.json()

i = 0
while i < len(data):
    wname = data[i]['name']
    wcolor = data[i]['color']
    print(""+wname.capitalize()+" is "+wcolor+".")
    i += 1
