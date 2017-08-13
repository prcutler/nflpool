from nflpool.data.teaminfo import TeamInfo
import requests
import nflpool.data.secret as secret
from requests.auth import HTTPBasicAuth
from nflpool.data.dbsession import DbSessionFactory
from nflpool.data.divisioninfo import DivisionInfo
from nflpool.data.conferenceinfo import ConferenceInfo
from nflpool.data.picktypes import PickTypes


class NewInstallService:

    @staticmethod
    def get_install():
        return []

    @classmethod
    def get_team_info(cls):

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
                #division = 'East'
                division_id = 1
            elif afc_team_id <= 63:
                #division = 'North'
                division_id = 2
            elif afc_team_id <= 71:
                #division = 'South'
                division_id = 3
            else:
                #division = 'West'
                division_id = 4

            x = x + 1

            team_info = TeamInfo(city=afc_team_city, team_id=afc_team_id, team_abbr=afc_team_abbr,
                                 name=afc_team_name, conference_id=0, division_id=division_id)

            session.add(team_info)

            session.commit()

        for nfc_team_list in teamlist:
            nfc_team_name = data["conferenceteamstandings"]["conference"][1]["teamentry"][y]["team"]["Name"]
            nfc_team_city = data["conferenceteamstandings"]["conference"][1]["teamentry"][y]["team"]["City"]
            nfc_team_id = int(data["conferenceteamstandings"]["conference"][1]["teamentry"][y]["team"]["ID"])
            nfc_team_abbr = data["conferenceteamstandings"]["conference"][1]["teamentry"][y]["team"]["Abbreviation"]

            if nfc_team_id <= 55:
                #division = 'East'
                division_id = 1
            elif nfc_team_id <= 63:
                #division = 'North'
                division_id = 2
            elif nfc_team_id <= 71:
                #division = 'South'
                division_id = 3
            else:
                #division = 'West'
                division_id = 4

            y = y + 1

            team_info = TeamInfo(city=nfc_team_city, team_id=nfc_team_id, team_abbr=nfc_team_abbr,
                                 name=nfc_team_name, conference_id=1, division_id=division_id)

            session.add(team_info)

            session.commit()

    # Fill out the needed info in the DivisionInfo table
    @classmethod
    def create_division_info(cls):
        for x in range(1, 5):
            division_id = x
            if x == 1:
                division = 'East'
            elif x == 2:
                division = 'North'
            elif x == 3:
                division = 'South'
            else:
                division = 'West'

            session = DbSessionFactory.create_session()

            division_info = DivisionInfo(division=division, division_id=division_id)

            session.add(division_info)
            session.commit()

    # Fill out the needed data in the ConferenceInfo table
    @classmethod
    def create_conference_info(cls):
        for x in range(1, 3):
            if x == 1:
                conference_id = 0
                conference = 'AFC'
            else:
                conference_id = 1
                conference = 'NFC'

            session = DbSessionFactory.create_session()

            conference_info = ConferenceInfo(conference=conference, conf_id=conference_id)

            session.add(conference_info)
            session.commit()

    # Fill out the needed data in the PickTypes table
    @classmethod
    def create_pick_types(cls):
        for x in range(1, 11):
            if x == 1:
                name = 'team'
            elif x == 2:
                name = 'player'
            elif x == 3:
                name = 'points_for'
            elif x == 4:
                name = "passing"
            elif x == 5:
                name = "rushing"
            elif x == 6:
                name = "receiving"
            elif x == 7:
                name = "sacks"
            elif x == 8:
                name = "interceptions"
            elif x == 9:
                name = "wildcard"
            else:
                name = 'tiebreaker'

            session = DbSessionFactory.create_session()

            pick_type_info = PickTypes(name=name)
            session.add(pick_type_info)
            session.commit()


