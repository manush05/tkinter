import json

f = open ('data.json', "r")
data = json.loads(f.read())
print(data)