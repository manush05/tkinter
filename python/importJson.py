import json

a = '{"name":"saran","class":"python"}'
y = json.loads(a)
print(y["name"])


# convert python objects into json 
string = "string"
z = json.dumps(string)
print(z)

boolean = True
r = json.dumps(boolean)
print(r)

integer = 12
e = json.dumps(integer)
print(e)

list_json = ["arjun","glass","layer"]
t = json.dumps(list_json)
print(t)

diction = {
    "name": "saran",
    "var":"json"
}
dict_json = json.dumps(diction)
print(dict_json)

