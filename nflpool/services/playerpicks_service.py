from sqlalchemy.orm import joinedload
from nflpool.data.picks import PlayerPicks
from nflpool.data.dbsession import DbSessionFactory
from nflpool.data.account import Account
from nflpool.data.teaminfo import TeamInfo


# Need to create a dictionary with team_id : conference / division
class PlayerPicksService:
    @staticmethod
    def get_pick_categories():
        session = DbSessionFactory.create_session()

        afc_east = session.query(TeamInfo).filter(TeamInfo.conference)\
            .filter(TeamInfo.division).order_by(TeamInfo.name).all()

        return afc_east
