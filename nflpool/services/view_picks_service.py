from nflpool.data.dbsession import DbSessionFactory
from nflpool.data.account import Account
from nflpool.data.player_picks import PlayerPicks
from nflpool.data.teaminfo import TeamInfo
from nflpool.data.picktypes import PickTypes
from nflpool.data.conferenceinfo import ConferenceInfo
from nflpool.data.divisioninfo import DivisionInfo
from nflpool.data.activeplayers import ActiveNFLPlayers
import sqlalchemy
from nflpool.data.seasoninfo import SeasonInfo


class ViewPicksService():
    @classmethod
    def get_account_info(cls, user_id):
        session = DbSessionFactory.create_session()

        account_info = session.query(Account).filter(Account.id == user_id).all()

        return account_info

    @classmethod
    def seasons_played(cls, user_id):
        session = DbSessionFactory.create_session()

        seasons_played = session.query(PlayerPicks.season).distinct(PlayerPicks.season).filter(Account.id == user_id)

        return seasons_played

    @classmethod
    def view_picks(cls, season):
        pass
        #session = DbSessionFactory.create_session()

        #pick_query = session.query

    @staticmethod
    def display_picks(user_id):
        session = DbSessionFactory.create_session()
#        season_row = session.query(SeasonInfo.current_season).filter(SeasonInfo.id == 1).first()
#        season = season_row.current_season

#        user_query = session.query(PlayerPicks, TeamInfo.name).join(TeamInfo, PlayerPicks.afc_east_first == TeamInfo.team_id) \
#            .filter(PlayerPicks.user_id == user_id) \
#            .filter(PlayerPicks.season == season).all()

#        print(user_query)
#        print(type(user_query[0]))

#        picks_query = session.query(PlayerPicks.pick_type, ConferenceInfo.conference, DivisionInfo.division,
#                                    ActiveNFLPlayers.firstname, ActiveNFLPlayers.lastname).\
#            outerjoin(DivisionInfo.division_id, PlayerPicks.division_id == DivisionInfo.division_id).\
#            outerjoin(ConferenceInfo, ConferenceInfo.conf_id == PlayerPicks.conf_id).\
#            outerjoin(TeamInfo, TeamInfo.team_id == PlayerPicks.team_id).\
#            outerjoin(ActiveNFLPlayers.player_id == PlayerPicks.player_id).\
#            and_(PlayerPicks.season == ActiveNFLPlayers.season).filter(PlayerPicks.user_id == user_id).\
#            and_(PlayerPicks.season == season)

        picks_query = session.query(PlayerPicks.pick_type, ConferenceInfo.conference, DivisionInfo.division,
                                    ActiveNFLPlayers.firstname, ActiveNFLPlayers.lastname).\
            outerjoin(DivisionInfo).\
            outerjoin(ConferenceInfo).\
            outerjoin(TeamInfo).\
            outerjoin(ActiveNFLPlayers).filter(and_(PlayerPicks.season == ActiveNFLPlayers.season)).\
            filter(PlayerPicks.user_id == user_id).and_(PlayerPicks.season == 2016)

        return picks_query

    conn = engine.connect()





