import json
import pprint
import os


with open('json/test.json') as json_data:
    d = json.load(json_data)
#    print(d)
#    pprint.pprint(d)
    for stat_categories in d["divisionteamstandings"]["division"][0]["teamentry"][0]["stats"]:
        pprint.pprint(stat_categories)
