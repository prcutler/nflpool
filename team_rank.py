import json

x = 0
y = 0

#NOTE: This code works, but MySportsFeeds only uses W/L, not http://www.nfl.com/standings/tiebreakingprocedures - hopefully they will fix

#Change the name of the file to open to match the query below:
with open('json/20161011-playoff-team-standings.json') as file:
    alltext = file.readlines()  #Put each line into a list

for lines in alltext:
    if lines.startswith('{'):
        rawdata = lines
        data = json.loads(rawdata)


#       This code shows it's a list with 16 items - each team!
        teamlist = data["playoffteamstandings"]["conference"][0]["teamentry"]
#        print(len(teamlist))
#        print(type(teamlist))

        #Create a loop to extract each team name (AFC first, then NFC) and rank in conference

        for afc_team_list in teamlist:
            afc_team_name = data["playoffteamstandings"]["conference"][0]["teamentry"][x]["team"]["Name"]
            afc_team_city = data["playoffteamstandings"]["conference"][0]["teamentry"][x]["team"]["City"]
            afc_team_id = data["playoffteamstandings"]["conference"][0]["teamentry"][x]["team"]["ID"]
            afc_team_abbr = data["playoffteamstandings"]["conference"][0]["teamentry"][x]["team"]["Abbreviation"]
            afc_rank = data["playoffteamstandings"]["conference"][0]["teamentry"][x]["rank"]
            print((afc_team_name), (afc_team_city), (afc_team_id), (afc_team_abbr), afc_rank)
            x = x + 1

        for nfc_team_list in teamlist:
            nfc_team_name = data["playoffteamstandings"]["conference"][1]["teamentry"][y]["team"]["Name"]
            nfc_team_city = data["playoffteamstandings"]["conference"][1]["teamentry"][y]["team"]["City"]
            nfc_team_id = data["playoffteamstandings"]["conference"][1]["teamentry"][y]["team"]["ID"]
            nfc_team_abbr = data["playoffteamstandings"]["conference"][1]["teamentry"][y]["team"]["Abbreviation"]
            nfc_rank = data["playoffteamstandings"]["conference"][1]["teamentry"][y]["rank"]
            y = y + 1
            print((nfc_team_name), (nfc_team_city), (nfc_team_id), (nfc_team_abbr), nfc_rank)

