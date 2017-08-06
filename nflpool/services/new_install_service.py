from nflpool.data.teaminfo import TeamInfo
import requests
import nflpool.data.secret as secret
from requests.auth import HTTPBasicAuth
from nflpool.data.dbsession import DbSessionFactory


class NewInstallService:

    @staticmethod
    def get_install():
        return []

    @classmethod
    def get_team_info(cls, city: str, conference: str, division: str, division_abbr: str,
                      division_id: int, name: str, team_abbr: str, team_id: int):

        session = DbSessionFactory.create_session()

        x = 0
        y = 0

        response = requests.get(
            'https://api.mysportsfeeds.com/v1.1/pull/nfl/2016-2017-regular/conference_team_standings.json',
            auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

        data = response.json()

        teamlist = data["conferenceteamstandings"]["conference"][0]["teamentry"]

        # Create a loop to extract each team name (AFC first, then NFC)

        for afc_team_list in teamlist:
            afc_team_name = data["conferenceteamstandings"]["conference"][0]["teamentry"][x]["team"]["Name"]
            afc_team_city = data["conferenceteamstandings"]["conference"][0]["teamentry"][x]["team"]["City"]
            afc_team_id = int(data["conferenceteamstandings"]["conference"][0]["teamentry"][x]["team"]["ID"])
            afc_team_abbr = data["conferenceteamstandings"]["conference"][0]["teamentry"][x]["team"]["Abbreviation"]

            if afc_team_id <= 55:
                division = 'East'
            elif afc_team_id <= 63:
                division = 'North'
            elif afc_team_id <= 71:
                division = 'South'
            else:
                division = 'West'

            x = x + 1

            team_info = TeamInfo(city=afc_team_city, conference='AFC', team_id=afc_team_id, team_abbr=afc_team_abbr,
                                 name=afc_team_name, division=division)

            session.add(team_info)

            session.commit()

        for nfc_team_list in teamlist:
            nfc_team_name = data["conferenceteamstandings"]["conference"][1]["teamentry"][y]["team"]["Name"]
            nfc_team_city = data["conferenceteamstandings"]["conference"][1]["teamentry"][y]["team"]["City"]
            nfc_team_id = int(data["conferenceteamstandings"]["conference"][1]["teamentry"][y]["team"]["ID"])
            nfc_team_abbr = data["conferenceteamstandings"]["conference"][1]["teamentry"][y]["team"]["Abbreviation"]

            if nfc_team_id <= 55:
                division = 'East'
            elif nfc_team_id <= 63:
                division = 'North'
            elif nfc_team_id <= 71:
                division = 'South'
            else:
                division = 'West'

            y = y + 1

            team_info = TeamInfo(city=nfc_team_city, conference='NFC', team_id=nfc_team_id, team_abbr=nfc_team_abbr,
                                 name=nfc_team_name, division=division)

            session.add(team_info)

            session.commit()
