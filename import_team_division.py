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

        teamlist = data["divisionteamstandings"]["division"][0]["teamentry"]
#        print(teamlist)


        divisionlist = data["divisionteamstandings"]["division"]
        print (type(divisionlist))

        for afc_division in divisionlist:
            afc_division_name = data["divisionteamstandings"]["division"][z]["@name"]
            z = z + 1

        for afc_team_list in teamlist:
            afc_team_name = data["divisionteamstandings"]["division"][0]["teamentry"][x]["team"]["Name"]
            afc_team_city = data["divisionteamstandings"]["division"][0]["teamentry"][x]["team"]["City"]
            afc_team_id = data["divisionteamstandings"]["division"][0]["teamentry"][x]["team"]["ID"]
            afc_team_abbr = data["divisionteamstandings"]["division"][0]["teamentry"][x]["team"]["Abbreviation"]
            print((afc_team_name), ",", (afc_team_city), ",", (afc_team_id), ",", (afc_team_abbr))
            x = x + 1


        for nfc_team_list in teamlist:
            nfc_team_name = data["divisionteamstandings"]["division"][1]["teamentry"][y]["team"]["Name"]
            nfc_team_city = data["divisionteamstandings"]["division"][1]["teamentry"][y]["team"]["City"]
            nfc_team_id = data["divisionteamstandings"]["division"][1]["teamentry"][y]["team"]["ID"]
            nfc_team_abbr = data["divisionteamstandings"]["division"][1]["teamentry"][y]["team"]["Abbreviation"]
            print((nfc_team_name), ",", (nfc_team_city), ",", (nfc_team_id), ",", (nfc_team_abbr))
            y = y + 1