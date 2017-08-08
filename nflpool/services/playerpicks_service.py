from nflpool.data.picks import PlayerPicks
from nflpool.data.dbsession import DbSessionFactory
from nflpool.data.account import Account
from nflpool.data.teaminfo import TeamInfo
from nflpool.data.picks import PlayerPicks
from nflpool.data.seasoninfo import SeasonInfo
from nflpool.data.account import Account
import datetime


# Need to create a dictionary with team_id : conference / division
class PlayerPicksService:
    @staticmethod
    # Query AFC East team list
    def get_afc_east_teams():
        session = DbSessionFactory.create_session()

        afc_east_teams = session.query(TeamInfo).filter(TeamInfo.conference_id == 0)\
            .filter(TeamInfo.division_id == 1).order_by(TeamInfo.name).all()

        return afc_east_teams

    @staticmethod
    # Query AFC north list
    def get_afc_north_teams():
        session = DbSessionFactory.create_session()

        afc_north_teams = session.query(TeamInfo).filter(TeamInfo.conference_id == 0) \
            .filter(TeamInfo.division_id == 2).order_by(TeamInfo.name).all()

        return afc_north_teams

    @staticmethod
    # Query AFC South list
    def get_afc_north_teams():
        session = DbSessionFactory.create_session()

        afc_south_teams = session.query(TeamInfo).filter(TeamInfo.conference_id == 0) \
            .filter(TeamInfo.division_id == 3).order_by(TeamInfo.name).all()

        return afc_south_teams

    @staticmethod
    # Query AFC West list
    def get_afc_west_teams():
        session = DbSessionFactory.create_session()

        afc_north_teams = session.query(TeamInfo).filter(TeamInfo.conference_id == 0) \
            .filter(TeamInfo.division_id == 2).order_by(TeamInfo.name).all()

        return afc_west_teams
    
    @staticmethod
    # Query NFC East team list
    def get_nfc_east_teams():
        session = DbSessionFactory.create_session()

        nfc_east_teams = session.query(TeamInfo).filter(TeamInfo.conference_id == 1)\
            .filter(TeamInfo.division_id == 5).order_by(TeamInfo.name).all()

        return nfc_east_teams

    @staticmethod
    # Query nfc north list
    def get_nfc_north_teams():
        session = DbSessionFactory.create_session()

        nfc_north_teams = session.query(TeamInfo).filter(TeamInfo.conference_id == 1) \
            .filter(TeamInfo.division_id == 6).order_by(TeamInfo.name).all()

        return nfc_north_teams

    @staticmethod
    # Query nfc South list
    def get_nfc_south_teams():
        session = DbSessionFactory.create_session()

        nfc_south_teams = session.query(TeamInfo).filter(TeamInfo.conference_id == 1) \
            .filter(TeamInfo.division_id == 7).order_by(TeamInfo.name).all()

        return nfc_south_teams

    @staticmethod
    # Query nfc West list
    def get_nfc_west_teams():
        session = DbSessionFactory.create_session()

        nfc_west_teams = session.query(TeamInfo).filter(TeamInfo.conference_id == 1) \
            .filter(TeamInfo.division_id == 8).order_by(TeamInfo.name).all()

        return nfc_west_teams

    @classmethod
    def get_player_picks(cls, afc_east_winner_pick: int, afc_east_second: int, afc_north_winner_pick: int,
                         afc_north_second: int, user_id: str):

        session = DbSessionFactory.create_session()

        season = session.query(SeasonInfo.id).filter(SeasonInfo.id == '1').first()
        print(season)

        # user_id = session.query(Account.id).filter(Account.email == user_name).first()

        dt = datetime.datetime.now()

        player_picks = PlayerPicks(date_submitted=dt, user_id=user_id, afc_east_first=afc_east_winner_pick,
                                   afc_east_second=afc_east_second, afc_north_first=afc_north_winner_pick,
                                   afc_north_second=afc_north_second, season=2016)

        session.add(player_picks)

        # TODO Need to write a check to make sure the player has not submitted picks yet.  Maybe similar
        # to the login check with a redirect?

        session.commit()
