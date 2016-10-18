import json

x = 0
y = 0
z = 0

#Change the name of the file to open to match the query below:
with open('json/20160921-division-team-standings.json') as file:
    alltext = file.readlines()  #Put each line into a list

for lines in alltext:
    if lines.startswith('{'):
        rawdata = lines
        data = json.loads(rawdata)

        teamlist = data["divisionteamstandings"]["division"]
        print (len(teamlist))
#        teamid = divisionlist[x]["teamentry"][0]["team"]["ID"]


# This iterates through all 8 divisions -- but only for the #1 rank team (list sub-0)
        #divisionlist = data["divisionteamstandings"]["division"]
#        print (type(divisionlist))

#        team = divisionlist[x]["teamentry"][0]["team"]["ID"]
#        for rank in team:
#            rank = divisionlist[x]["teamentry"][0]["rank"]
#            y = y + 1
#            x = x + 1
#            print(team, rank)


# This iterates through all 8 divisions -- but only for the #1 rank team (list sub-0)
#        divisionlist = data["divisionteamstandings"]["division"]
#        print (type(divisionlist))

#        for rank in divisionlist:
#            team = divisionlist[x]["teamentry"][0]["team"]["ID"]
#            rank = divisionlist[x]["teamentry"][0]["rank"]
#            x = x + 1
#            print(team, rank)


#        for afc_division in divisionlist:
#            afc_division_name = data["divisionteamstandings"]["division"][0]["@name"]


        for afc_team_list in teamlist:
            afc_team_id = data["divisionteamstandings"]["division"][y]["teamentry"][x]["team"]["ID"]
            for rank in afc_team_id:
                rank = data["divisionteamstandings"]["division"][y]["teamentry"][x]["rank"]
            print(afc_team_id, rank)
            x = x + 1
            if x == 4:
                x = 0
                y = y + 1
                if y == 4:
                    y = 0



#TODO
# Change division to Y above.  Then run a rank in "Division" in a for loop underneat


#        for nfc_team_list in teamlist:
#            nfc_team_name = data["divisionteamstandings"]["division"][1]["teamentry"][y]["team"]["Name"]
#            nfc_team_city = data["divisionteamstandings"]["division"][1]["teamentry"][y]["team"]["City"]
#            nfc_team_id = data["divisionteamstandings"]["division"][1]["teamentry"][y]["team"]["ID"]
#            nfc_team_abbr = data["divisionteamstandings"]["division"][1]["teamentry"][y]["team"]["Abbreviation"]
#            print((nfc_team_name), ",", (nfc_team_city), ",", (nfc_team_id), ",", (nfc_team_abbr))
#            y = y + 1