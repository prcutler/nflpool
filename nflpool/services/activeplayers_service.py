import requests
from nflpool.data.dbsession import DbSessionFactory
from nflpool.data.activeplayers import ActiveNFLPlayers
import nflpool.data.secret as secret


class ActivePlayersService:
    @staticmethod
    def get_active_players():
        pass
#        session = DbSessionFactory.create_session()

#        url = secret.base_url +

#        response = requests.get(secret.base_url /2016-2017-regular/active_players.json',
#                                auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

#        player_info = response.json()
#        player_list = player_info["activeplayers"]["playerentry"]

 #       for players in player_list:
 #           try:
 #               firstname = (players["player"]["FirstName"])
 #               lastname = (players["player"]["LastName"])
 #               player_id = (players["player"]["ID"])
 #               team_id = (players["team"]["ID"])
 #               position = (players["player"]["Position"])
 #           except KeyError:
 #               continue

