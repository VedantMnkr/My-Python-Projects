import json

d = {"www.Nagpur.com":
     {
         "name": "vedant",
         "age": 21
     }
     }

json_obj = json.dumps(d, indent=5)
print(json_obj)
with open("saved_password.json", "w+") as f:
    f.write(json_obj)

with open("saved_password.json", "r") as f:
    json_obj = json.load(f)

new_d = {"name": "Daddi", "age": 13}
json_obj["www.SOS.com"] = new_d

with open("saved_password.json", "w+") as f:
    f.write(json.dumps(json_obj, indent= 3))

print(json_obj)
