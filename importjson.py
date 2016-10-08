import json
import pprint
import os

#Open the JSON file that includes headers

with open('json/20160927-division-team-standings.json') as file:
    alltext = file.readlines()  #Put each line into a list

for lines in alltext:
    if lines.startswith('{'):
        rawdata = lines
        data = json.loads(rawdata)
        for stat_categories in data["divisionteamstandings"]["division"][0]["teamentry"][0]["stats"]:
            pprint.pprint(stat_categories)
