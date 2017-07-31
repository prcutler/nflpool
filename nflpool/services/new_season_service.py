from sqlalchemy.orm import joinedload
import sqlalchemy.orm
from nflpool.data.conferenceinfo import ConferenceInfo
from nflpool.data.divisioninfo import DivisionInfo
from nflpool.data.teaminfo import TeamInfo
from nflpool.data.activeplayers import ActivePlayers

class NewSeasonService:
    @staticmethod
    def get_active_players():

