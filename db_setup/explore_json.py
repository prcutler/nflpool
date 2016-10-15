import json

#Change the name of the file to open to match the query below:
with open('json/20160921-conference-team-standings.json') as file:
    alltext = file.readlines()  #Put each line into a list

for lines in alltext:
    if lines.startswith('{'):
        rawdata = lines
        data = json.loads(rawdata)



#       This code shows it's a list with 16 items - each team!
        teamlist = data["conferenceteamstandings"]["conference"][0]["teamentry"]
#        print(len(teamlist))

#       This shows team_dict is a dictionary with 4 items (abbr, name, short name and ID)
#        team_dict = data["conferenceteamstandings"]["conference"][0]["teamentry"][x]["team"]
#        print(len(team_dict))
#        print(type(team_dict))