from sqlalchemy.orm import joinedload
import sqlalchemy.orm
from nflpool.data.activeplayers import ActiveNFLPlayers
import requests
import nflpool.data.secret as secret
from requests.auth import HTTPBasicAuth
from nflpool.data.dbsession import DbSessionFactory


class NewSeasonService:

    @staticmethod
    def get_season():
        return []

    @classmethod
    def add_active_nflplayers(cls, season: int, team_id: int, firstname: str, lastname: str,
                              position: str, player_id: int):

        session = DbSessionFactory.create_session()

        response = requests.get('https://api.mysportsfeeds.com/v1.1/pull/nfl/2017-regular/active_players.json',
                                auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

        player_info = response.json()
        player_list = player_info["activeplayers"]["playerentry"]

        for players in player_list:
            try:
                firstname = (players["player"]["FirstName"])
                lastname = (players["player"]["LastName"])
                player_id = (players["player"]["ID"])
                team_id = (players["team"]["ID"])
                position = (players["player"]["Position"])
            except KeyError:
                continue

            active_players = ActiveNFLPlayers(firstname=firstname, lastname=lastname, player_id=player_id,
                                              team_id=team_id, position=position, season='2017')

            session.add(active_players)

            session.commit()


