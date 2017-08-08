from nflpool.data.picks import PlayerPicks
from nflpool.data.dbsession import DbSessionFactory
from nflpool.data.account import Account
from nflpool.data.teaminfo import TeamInfo
from nflpool.data.picks import PlayerPicks
from nflpool.data.seasoninfo import SeasonInfo
import datetime


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

    @classmethod
    def get_player_picks(cls, afc_east_winner_pick: int, afc_east_second: int, afc_north_winner_pick: int,
                         afc_north_second: int):

        session = DbSessionFactory.create_session()

        user_id = Account.id

        season = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()

        dt = datetime.datetime.now()

        player_picks = PlayerPicks(date_submitted=dt, user_id=user_id, afc_east_first=afc_east_winner_pick,
                                   afc_east_second=afc_east_second, afc_north_first=afc_north_winner_pick,
                                   afc_north_second=afc_north_second, season=season)

        session.add(player_picks)

        session.commit()
