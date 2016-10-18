import json

teaminfo = []

#Change the name of the file to open to match the query below:
with open('json/20160921-division-team-standings.json') as file:
    alltext = file.readlines()  #Put each line into a list

for lines in alltext:
    if lines.startswith('{'):
        rawdata = lines
        data = json.loads(rawdata)

        division = data["divisionteamstandings"]["division"]
        print (len(division))
        print (type(division[0]))
        for key, value in division[0].items():
            if key == 'teamentry':
                teaminfo.append([key, value])
                print (type(teaminfo[0]))

