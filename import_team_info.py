import json

x = 0
y = 0

#Change the name of the file to open to match the query below:
with open('json/20160921-conference-team-standings.json') as file:
    alltext = file.readlines()  #Put each line into a list

for lines in alltext:
    if lines.startswith('{'):
        rawdata = lines
        data = json.loads(rawdata)


#       This shows there are two dictionaries in conference - AFC and NFC
#        teamdata = data["conferenceteamstandings"]["conference"]
#        print (len(teamdata)), (type(teamdata))

#       This code shows it's a dictionary with 3 items (team, stats, rank) and prints all their nested dicts for just HOU - teamentry 0
#        teamdata = data["conferenceteamstandings"]["conference"][0]["teamentry"][0]
#        print(len(teamdata)), (type(teamdata))

#        for key, value in teamdata.items():
#            print(key, ":", value)

#       This code shows it's a dictionary with 2 items
#        teamdata = data["conferenceteamstandings"]["conference"][0]
#        print(len(teamdata)), (type(teamdata))

#       This code shows it's a dictionary with 2 items (AFC and NFC dictionaries)
#        conf_dict = data["conferenceteamstandings"]["conference"][0]
#        print(len(conf_dict))
#        print(type(conf_dict))
#       This will print all the keys and values for all nested dictionaries
#        for key, value in conf_dict.items():
#            print(key, ":", value)


#       This code shows it's a list with 16 items - each team!
        teamlist = data["conferenceteamstandings"]["conference"][0]["teamentry"]
#        print(len(teamlist))
#        print(type(teamlist))

        #Create a loop to extract each team name (AFC first, then NFC)

        for afc_team_list in teamlist:
            afc_team_name = data["conferenceteamstandings"]["conference"][0]["teamentry"][x]["team"]["Name"]
            afc_team_city = data["conferenceteamstandings"]["conference"][0]["teamentry"][x]["team"]["City"]
            afc_team_id = data["conferenceteamstandings"]["conference"][0]["teamentry"][x]["team"]["ID"]
            afc_team_abbr = data["conferenceteamstandings"]["conference"][0]["teamentry"][x]["team"]["Abbreviation"]
            print((afc_team_name),",",(afc_team_city),",",(afc_team_id),",",(afc_team_abbr))
            x = x + 1


        for nfc_team_list in teamlist:
            nfc_team_name = data["conferenceteamstandings"]["conference"][1]["teamentry"][y]["team"]["Name"]
            nfc_team_city = data["conferenceteamstandings"]["conference"][1]["teamentry"][y]["team"]["City"]
            nfc_team_id = data["conferenceteamstandings"]["conference"][1]["teamentry"][y]["team"]["ID"]
            nfc_team_abbr = data["conferenceteamstandings"]["conference"][1]["teamentry"][y]["team"]["Abbreviation"]
            print((nfc_team_name),",",(nfc_team_city),",",(nfc_team_id),",",(nfc_team_abbr))
            y = y + 1

#       This shows team_dict is a dictionary with 4 items
#        team_dict = data["conferenceteamstandings"]["conference"][0]["teamentry"][x]["team"]
#        print(len(team_dict))
#        print(type(team_dict))


#        for key, value in team_dict.items():
#            print(key, ":", value)
#            x = x + 1

#        for key, value in teamdata.items():
#            print(key, ":", value)


