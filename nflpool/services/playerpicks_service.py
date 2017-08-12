from nflpool.data.picks import PlayerPicks
from nflpool.data.dbsession import DbSessionFactory
from nflpool.data.account import Account
from nflpool.data.teaminfo import TeamInfo
from nflpool.data.activeplayers import ActiveNFLPlayers
from nflpool.data.picks import PlayerPicks
from nflpool.data.seasoninfo import SeasonInfo
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
    def get_afc_south_teams():
        session = DbSessionFactory.create_session()

        afc_south_teams = session.query(TeamInfo).filter(TeamInfo.conference_id == 0) \
            .filter(TeamInfo.division_id == 3).order_by(TeamInfo.name).all()

        return afc_south_teams

    @staticmethod
    # Query AFC West list
    def get_afc_west_teams():
        session = DbSessionFactory.create_session()

        afc_west_teams = session.query(TeamInfo).filter(TeamInfo.conference_id == 0) \
            .filter(TeamInfo.division_id == 4).order_by(TeamInfo.name).all()

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

    @staticmethod
    # Get list of AFC QBs
    def afc_get_qb():
        session = DbSessionFactory.create_session()

        afc_qb_list = session.query(ActiveNFLPlayers.player_id, ActiveNFLPlayers.firstname, ActiveNFLPlayers.lastname).\
            join(TeamInfo, ActiveNFLPlayers.team_id == TeamInfo.team_id) \
            .filter(TeamInfo.conference_id == 0) \
            .filter(ActiveNFLPlayers.position == 'QB') \
            .filter(ActiveNFLPlayers.season == SeasonInfo.current_season) \
            .order_by(ActiveNFLPlayers.lastname).all()

        return afc_qb_list

    @staticmethod
    # Get list of NFC QBs
    def nfc_get_qb():
        session = DbSessionFactory.create_session()

        nfc_qb_list = session.query(ActiveNFLPlayers.player_id, ActiveNFLPlayers.firstname, ActiveNFLPlayers.lastname).\
            join(TeamInfo, ActiveNFLPlayers.team_id == TeamInfo.team_id) \
            .filter(TeamInfo.conference_id == 1) \
            .filter(ActiveNFLPlayers.position == 'QB') \
            .filter(ActiveNFLPlayers.season == SeasonInfo.current_season) \
            .order_by(ActiveNFLPlayers.lastname).all()

        return nfc_qb_list

    @staticmethod
    # Get list of AFC RBs
    def afc_get_rb():
        session = DbSessionFactory.create_session()

        afc_rb_list = session.query(ActiveNFLPlayers.player_id, ActiveNFLPlayers.firstname, ActiveNFLPlayers.lastname).\
            join(TeamInfo, ActiveNFLPlayers.team_id == TeamInfo.team_id) \
            .filter(TeamInfo.conference_id == 0) \
            .filter(ActiveNFLPlayers.position == 'RB') \
            .filter(ActiveNFLPlayers.season == SeasonInfo.current_season) \
            .order_by(ActiveNFLPlayers.lastname).all()

        return afc_rb_list

    @staticmethod
    # Get list of NFC RBs
    def nfc_rb_get():
        session = DbSessionFactory.create_session()

        nfc_rb_list = session.query(ActiveNFLPlayers.player_id, ActiveNFLPlayers.firstname, ActiveNFLPlayers.lastname).\
            join(TeamInfo, ActiveNFLPlayers.team_id == TeamInfo.team_id) \
            .filter(TeamInfo.conference_id == 1) \
            .filter(ActiveNFLPlayers.position == 'RB') \
            .filter(ActiveNFLPlayers.season == SeasonInfo.current_season) \
            .order_by(ActiveNFLPlayers.lastname).all()

        return nfc_rb_list

    @staticmethod
    # Get list of AFC pass catchers
    def afc_get_rec():
        session = DbSessionFactory.create_session()

        afc_rec_list = session.query(ActiveNFLPlayers.player_id,
                                     ActiveNFLPlayers.firstname, ActiveNFLPlayers.lastname).\
            join(TeamInfo, ActiveNFLPlayers.team_id == TeamInfo.team_id) \
            .filter(TeamInfo.conference_id == 0) \
            .filter(ActiveNFLPlayers.position.in_(['TE', 'WR'])) \
            .filter(ActiveNFLPlayers.season == SeasonInfo.current_season) \
            .order_by(ActiveNFLPlayers.lastname).all()

        return afc_rec_list

    @staticmethod
    # Get list of NFC pass catchers
    def nfc_get_rec():
        session = DbSessionFactory.create_session()

        nfc_rec_list = session.query(ActiveNFLPlayers.player_id, ActiveNFLPlayers.firstname,
                                     ActiveNFLPlayers.lastname).\
            join(TeamInfo, ActiveNFLPlayers.team_id == TeamInfo.team_id) \
            .filter(TeamInfo.conference_id == 1) \
            .filter(ActiveNFLPlayers.position.in_(['TE', 'WR'])) \
            .filter(ActiveNFLPlayers.season == SeasonInfo.current_season) \
            .order_by(ActiveNFLPlayers.lastname).all()

        return nfc_rec_list

    @staticmethod
    # Get list of AFC sack leaders
    def afc_get_sacks():
        session = DbSessionFactory.create_session()

        afc_sacks_list = session.query(ActiveNFLPlayers.player_id, ActiveNFLPlayers.firstname,
                                       ActiveNFLPlayers.lastname). \
            join(TeamInfo, ActiveNFLPlayers.team_id == TeamInfo.team_id) \
            .filter(TeamInfo.conference_id == 0) \
            .filter(ActiveNFLPlayers.position.in_(['DE', 'DT', 'ILB', 'LB', 'MLB', 'NT', 'OLB'])) \
            .filter(ActiveNFLPlayers.season == SeasonInfo.current_season) \
            .order_by(ActiveNFLPlayers.lastname).all()

        return afc_sacks_list

    @staticmethod
    # Get list of NFC sack leaders
    def nfc_get_sacks():
        session = DbSessionFactory.create_session()

        nfc_sacks_list = session.query(ActiveNFLPlayers.player_id, ActiveNFLPlayers.firstname,
                                       ActiveNFLPlayers.lastname). \
            join(TeamInfo, ActiveNFLPlayers.team_id == TeamInfo.team_id) \
            .filter(TeamInfo.conference_id == 1) \
            .filter(ActiveNFLPlayers.position.in_(['DE', 'DT', 'ILB', 'LB', 'MLB', 'NT', 'OLB'])) \
            .filter(ActiveNFLPlayers.season == SeasonInfo.current_season) \
            .order_by(ActiveNFLPlayers.lastname).all()

        return nfc_sacks_list

    @staticmethod
    # Get list of AFC interception leaders
    def afc_get_int():
        session = DbSessionFactory.create_session()

        afc_int_list = session.query(ActiveNFLPlayers.player_id, ActiveNFLPlayers.firstname,
                                       ActiveNFLPlayers.lastname). \
            join(TeamInfo, ActiveNFLPlayers.team_id == TeamInfo.team_id) \
            .filter(TeamInfo.conference_id == 0) \
            .filter(ActiveNFLPlayers.position.in_(['CB', 'DB', 'FS', 'SS', 'MLB', 'LB', 'OLB', 'ILB'])) \
            .filter(ActiveNFLPlayers.season == SeasonInfo.current_season) \
            .order_by(ActiveNFLPlayers.lastname).all()

        return afc_int_list

    @staticmethod
    # Get list of NFC interception leaders
    def nfc_get_int():
        session = DbSessionFactory.create_session()

        nfc_int_list = session.query(ActiveNFLPlayers.player_id, ActiveNFLPlayers.firstname,
                                     ActiveNFLPlayers.lastname). \
            join(TeamInfo, ActiveNFLPlayers.team_id == TeamInfo.team_id) \
            .filter(TeamInfo.conference_id == 1) \
            .filter(ActiveNFLPlayers.position.in_(['CB', 'DB', 'FS', 'SS', 'MLB', 'LB', 'OLB', 'ILB'])) \
            .filter(ActiveNFLPlayers.season == SeasonInfo.current_season) \
            .order_by(ActiveNFLPlayers.lastname).all()

        return nfc_int_list

    @staticmethod
    def get_afc_wildcard():
        session = DbSessionFactory.create_session()

        afc_wildcard_list = session.query(TeamInfo).filter(TeamInfo.conference_id == 0).order_by(TeamInfo.name).all()

        return afc_wildcard_list

    @staticmethod
    def get_nfc_wildcard():
        session = DbSessionFactory.create_session()

        nfc_wildcard_list = session.query(TeamInfo).filter(TeamInfo.conference_id == 1).order_by(TeamInfo.name).all()

        return nfc_wildcard_list

    @staticmethod
    def get_all_teams():
        session = DbSessionFactory.create_session()

        all_team_list = session.query(TeamInfo).filter(TeamInfo.team_id).order_by(TeamInfo.name).all()

        return all_team_list

    @staticmethod
    def get_current_season():
        session = DbSessionFactory.create_session()
        season_row = session.query(SeasonInfo.current_season).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season

        return season

    @classmethod
    def get_player_picks(cls, afc_east_winner_pick: int, afc_east_second: int, afc_east_last: int,
                         afc_north_winner_pick: int, afc_north_second: int, afc_north_last: int,
                         afc_south_winner_pick: int, afc_south_second: int, afc_south_last: int,
                         afc_west_winner_pick: int, afc_west_second: int, afc_west_last: int,
                         nfc_east_winner_pick: int, nfc_east_second: int, nfc_east_last: int,
                         nfc_north_winner_pick: int, nfc_north_second: int, nfc_north_last: int,
                         nfc_south_winner_pick: int, nfc_south_second: int, nfc_south_last: int,
                         nfc_west_winner_pick: int, nfc_west_second: int, nfc_west_last: int,
                         afc_qb_pick: int, nfc_qb_pick: int, afc_rb_pick: int, nfc_rb_pick: int,
                         afc_rec_pick: int, nfc_rec_pick: int,
                         afc_sacks_pick: int, nfc_sacks_pick: int,
                         afc_int_pick: int, nfc_int_pick: int,
                         afc_wildcard1_pick: int, afc_wildcard2_pick: int,
                         nfc_wildcard1_pick: int, nfc_wildcard2_pick: int,
                         afc_pf_pick: int, nfc_pf_pick: int,
                         specialteams_td_pick: int,
                         user_id: str):

        session = DbSessionFactory.create_session()
        season_row = session.query(SeasonInfo.current_season).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season

        dt = datetime.datetime.now()

        player_picks = PlayerPicks(date_submitted=dt, user_id=user_id, afc_east_first=afc_east_winner_pick,
                                   afc_east_second=afc_east_second, afc_east_last=afc_east_last,
                                   afc_north_first=afc_north_winner_pick, afc_north_second=afc_north_second,
                                   afc_north_last=afc_north_last,
                                   afc_south_first=afc_south_winner_pick, afc_south_second=afc_south_second,
                                   afc_south_last=afc_south_last,
                                   afc_west_first=afc_west_winner_pick, afc_west_second=afc_west_second,
                                   afc_west_last=afc_west_last,
                                   nfc_east_first=nfc_east_winner_pick,
                                   nfc_east_second=nfc_east_second, nfc_east_last=nfc_east_last,
                                   nfc_north_first=nfc_north_winner_pick, nfc_north_second=nfc_north_second,
                                   nfc_north_last=nfc_north_last,
                                   nfc_south_first=nfc_south_winner_pick, nfc_south_second=nfc_south_second,
                                   nfc_south_last=nfc_south_last,
                                   nfc_west_first=nfc_west_winner_pick,
                                   nfc_west_second=nfc_west_second,
                                   nfc_west_last=nfc_west_last,
                                   afc_passing_pick=afc_qb_pick,
                                   nfc_passing_pick=nfc_qb_pick,
                                   afc_rushing_pick=afc_rb_pick,
                                   nfc_rushing_pick=nfc_rb_pick,
                                   afc_receiving_pick=afc_rec_pick,
                                   nfc_receiving_pick=nfc_rec_pick,
                                   afc_sacks_pick=afc_sacks_pick,
                                   nfc_sacks_pick=nfc_sacks_pick,
                                   afc_int_pick=afc_int_pick,
                                   nfc_int_pick=nfc_int_pick,
                                   afc_wildcard1=afc_wildcard1_pick, afc_wildcard2=afc_wildcard2_pick,
                                   nfc_wildcard2=nfc_wildcard2_pick, nfc_wildcard1=nfc_wildcard1_pick,
                                   afc_pf=afc_pf_pick, nfc_pf=nfc_pf_pick,
                                   specialteams_td=specialteams_td_pick,

                                   season=season)

        session.add(player_picks)

        session.commit()


class DisplayPlayerPicks:

    @staticmethod
    def display_picks(user_id):

        session = DbSessionFactory.create_session()
        season_row = session.query(SeasonInfo.current_season).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season
        # user_id = self.logged_in_user_id
        user_query = session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id) \
            .filter(PlayerPicks.season == season).all()

        print(user_query)
        print(type(user_query[0]))

        return user_query
