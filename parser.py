import json

jsondata = open('example_data.json').read()

json_object = json.loads(jsondata)
print("Parsing Data:")
imdata = json_object["imdata"]
for i in imdata:
    id = i["id"]
    description = i["description"]
    name = i["name"]
    print(id, name, description)