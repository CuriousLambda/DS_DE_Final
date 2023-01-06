import json

with open("/Users/admin/Desktop/final/data/cvc_code.json", "r") as f:
    data = json.load(f)

for i in data:
    print(i)