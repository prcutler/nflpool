from sqlalchemy.orm import joinedload
import sqlalchemy.orm
from nflpool.data.conferenceinfo import ConferenceInfo
from nflpool.data.divisioninfo import DivisionInfo
from nflpool.data.teaminfo import TeamInfo
from nflpool.data.activeplayers import ActivePlayers
import requests
import nflpool.data.secret as secret
import sqlite3
from requests.auth import HTTPBasicAuth
from nflpool.data.dbsession import DbSessionFactory


class NewInstallService:

    @staticmethod
    def get_install():
        return []


    @classmethod
    def get_team_info(cls, city: str, conference: str, division: str, division_abbr: str,
                      division_id: int, name: str, team_abbr: str, team_id: int):
        x = 0
        y = 0

        response = requests.get(
            'https://www.mysportsfeeds.com/api/feed/pull/nfl/2016-2017-regular/conference_team_standings.json',
            auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

        data = response.json()

        teamlist = data["conferenceteamstandings"]["conference"][0]["teamentry"]

        # Create a loop to extract each team name (AFC first, then NFC)

        for afc_team_list in teamlist:
            afc_team_name = data["conferenceteamstandings"]["conference"][0]["teamentry"][x]["team"]["Name"]
            afc_team_city = data["conferenceteamstandings"]["conference"][0]["teamentry"][x]["team"]["City"]
            afc_team_id = data["conferenceteamstandings"]["conference"][0]["teamentry"][x]["team"]["ID"]
            afc_team_abbr = data["conferenceteamstandings"]["conference"][0]["teamentry"][x]["team"]["Abbreviation"]
            #            print((afc_team_name), (afc_team_city), (afc_team_id), (afc_team_abbr))
            x = x + 1

            conn = sqlite3.connect(secret.db_location())
            cur = conn.cursor()

            cur.execute('''INSERT INTO TeamInfo(name, team_id, city, team_abbr, conference)
                        VALUES(?,?,?,?, "AFC")''', (afc_team_name, afc_team_id, afc_team_city, afc_team_abbr))

            conn.commit()
            conn.close()