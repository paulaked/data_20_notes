import json

new_dict = {"name": "apple", "flavour":"tasty"}

with open("new_json_file.json", "w") as jsonfile:
    json.dump(new_dict, jsonfile)

with open("new_json_file.json") as jsonfile:
    json.load(jsonfile)

