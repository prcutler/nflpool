import json
import pprint
import os

# from json_digger.json_digger import JsonDigger
# from traverse import traverse_modify

#Open the JSON file that includes headers

#Change the name of the file to open to match the query below:
with open('json/20161018-cumulative-player-stats.json') as file:
    alltext = file.readlines()  #Put each line into a list

# division-team-standings.json
#for lines in alltext:
#    if lines.startswith('{'):
#        rawdata = lines
#        data = json.loads(rawdata)
#        for stat_categories in data["divisionteamstandings"]["division"][0]["teamentry"][0]["stats"]:
#            pprint.pprint(stat_categories)   #Print all the categories in "stats"
#        pprint.pprint(data)  #Print the JSON


# overall-team-standings
#for lines in alltext:
#    if lines.startswith('{'):
#        rawdata = lines
#        data = json.loads(rawdata)
#        for stat_categories in data["overallteamstandings"]["teamstandingsentry"][0]["stats"]:
#            pprint.pprint(stat_categories)
#        pprint.pprint(data)

# conference-team-standings.json
# for lines in alltext:
#    if lines.startswith('{'):
#        rawdata = lines
#        data = json.loads(rawdata)


#        for stat_categories in data["conferenceteamstandings"]["conference"]:
#        for stat_categories in data["conferenceteamstandings"]["conference"][0]["teamentry"][0]["team"]:
#            x = dict.keys(data["conferenceteamstandings"]["conference"][0]["teamentry"][0])  #This equals rank, team, stats
#            x = dict.keys(data["conferenceteamstandings"]["conference"][0]["teamentry"][0]["team"])  # This equals rank, team, stats

#           x = data["conferenceteamstandings"]["conference"][0]["teamentry"][1]["team"]["Name"]
 #           pprint.pprint(x)
#            print (x)
 #       pprint.pprint(data)

# cumulative-player-stats.json
for lines in alltext:
    if lines.startswith('{'):
        rawdata = lines
        data = json.loads(rawdata)
        for stat_categories in data["cumulativeplayerstats"]["playerstatsentry"][0]["stats"]:
            pprint.pprint(stat_categories)
        pprint.pprint(data)
