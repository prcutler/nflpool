from nflpool.data.picks import PlayerPicks
from nflpool.data.dbsession import DbSessionFactory
from nflpool.data.account import Account
from nflpool.data.teaminfo import TeamInfo


# Need to create a dictionary with team_id : conference / division
class PlayerPicksService:
    @staticmethod
    def get_afc_east_teams():
        session = DbSessionFactory.create_session()

        afc_east_teams = session.query(TeamInfo).filter(TeamInfo.conference == 'AFC')\
            .filter(TeamInfo.division == 'East').order_by(TeamInfo.name).all()

        return afc_east_teams

    @staticmethod
    def get_afc_north_teams():
        session = DbSessionFactory.create_session()

        afc_north_teams = session.query(TeamInfo).filter(TeamInfo.conference == 'AFC') \
            .filter(TeamInfo.division == 'North').order_by(TeamInfo.name).all()

        return afc_north_teams
