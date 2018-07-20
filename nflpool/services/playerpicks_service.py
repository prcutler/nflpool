from nflpool.data.dbsession import DbSessionFactory
from nflpool.data.account import Account
from nflpool.data.teaminfo import TeamInfo
from nflpool.data.activeplayers import ActiveNFLPlayers
from nflpool.data.seasoninfo import SeasonInfo
from nflpool.data.player_picks import PlayerPicks
import datetime
from nflpool.services.time_service import TimeService


# Need to create a dictionary with team_id : conference / division
class PlayerPicksService:
    @staticmethod
    def get_team_list(conf_id, division_id):
        session = DbSessionFactory.create_session()

        team_list = session.query(TeamInfo).filter(TeamInfo.conference_id == conf_id)\
            .filter(TeamInfo.division_id == division_id).order_by(TeamInfo.name).all()

        return team_list

    @staticmethod
    def get_player_list(conf_id, position):
        session = DbSessionFactory.create_session()

        player_list = session.query(ActiveNFLPlayers.player_id, ActiveNFLPlayers.firstname, ActiveNFLPlayers.lastname,
                                    ActiveNFLPlayers.position, TeamInfo.team_abbr) \
            .join(TeamInfo, ActiveNFLPlayers.team_id == TeamInfo.team_id) \
            .filter(TeamInfo.conference_id == conf_id) \
            .filter(ActiveNFLPlayers.position == position) \
            .filter(ActiveNFLPlayers.season == SeasonInfo.current_season) \
            .order_by(ActiveNFLPlayers.lastname).all()

        return player_list

    @staticmethod
    def get_rec_list(conf_id, wr, te):
        session = DbSessionFactory.create_session()

        player_list = session.query(ActiveNFLPlayers.player_id, ActiveNFLPlayers.firstname, ActiveNFLPlayers.lastname,
                                    ActiveNFLPlayers.position, TeamInfo.team_abbr).\
            join(TeamInfo, ActiveNFLPlayers.team_id == TeamInfo.team_id) \
            .filter(TeamInfo.conference_id == conf_id) \
            .filter(ActiveNFLPlayers.position.in_([wr, te])) \
            .filter(ActiveNFLPlayers.season == SeasonInfo.current_season) \
            .order_by(ActiveNFLPlayers.lastname).all()

        return player_list

    @staticmethod
    # Get list of sack leaders
    def get_sacks(conf_id, de, dt, ilb, lb, mlb, nt, olb):
        session = DbSessionFactory.create_session()

        sacks_list = session.query(ActiveNFLPlayers.player_id, ActiveNFLPlayers.firstname,
                                   ActiveNFLPlayers.lastname, ActiveNFLPlayers.position, TeamInfo.team_abbr). \
            join(TeamInfo, ActiveNFLPlayers.team_id == TeamInfo.team_id) \
            .filter(TeamInfo.conference_id == conf_id) \
            .filter(ActiveNFLPlayers.position.in_([de, dt, ilb, lb, mlb, nt, olb])) \
            .filter(ActiveNFLPlayers.season == SeasonInfo.current_season) \
            .order_by(ActiveNFLPlayers.lastname).all()

        return sacks_list

    @staticmethod
    # Get list of interception leaders
    def get_int(conf_id, cb, db, fs, ss, mlb, lb, olb, ilb):
        session = DbSessionFactory.create_session()

        int_list = session.query(ActiveNFLPlayers.player_id, ActiveNFLPlayers.firstname, ActiveNFLPlayers.lastname,
                                 ActiveNFLPlayers.position, TeamInfo.team_abbr). \
            join(TeamInfo, ActiveNFLPlayers.team_id == TeamInfo.team_id) \
            .filter(TeamInfo.conference_id == conf_id) \
            .filter(ActiveNFLPlayers.position.in_([cb, db, fs, ss, mlb, lb, olb, ilb])) \
            .filter(ActiveNFLPlayers.season == SeasonInfo.current_season) \
            .order_by(ActiveNFLPlayers.lastname).all()

        return int_list

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
        season_row = session.query(SeasonInfo.current_season).filter(SeasonInfo.id == 1).first()
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
        season_row = session.query(SeasonInfo.current_season).filter(SeasonInfo.id == 1).first()
        season = season_row.current_season

        dt = TimeService.get_time()

        # Add AFC team picks
        afc_east_winner_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, conf_id=0, division_id=1, 
                                         rank=1, team_id=afc_east_winner_pick, pick_type=1)
        session.add(afc_east_winner_db)
        afc_east_second_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, conf_id=0, division_id=1, 
                                         rank=2, team_id=afc_east_second, pick_type=1)
        session.add(afc_east_second_db)
        
        afc_east_last_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, conf_id=0, division_id=1, 
                                       rank=4, team_id=afc_east_last, pick_type=1)

        session.add(afc_east_last_db)

        afc_north_winner_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, conf_id=0, division_id=2,
                                          rank=1, team_id=afc_north_winner_pick, pick_type=1)
        session.add(afc_north_winner_db)
        afc_north_second_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, conf_id=0, division_id=2,
                                          rank=2, team_id=afc_north_second, pick_type=1)
        session.add(afc_north_second_db)

        afc_north_last_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, conf_id=0, division_id=2,
                                        rank=4, team_id=afc_north_last, pick_type=1)

        session.add(afc_north_last_db)

        afc_south_winner_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, conf_id=0, division_id=3,
                                          rank=1, team_id=afc_south_winner_pick, pick_type=1)
        session.add(afc_south_winner_db)
        afc_south_second_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, conf_id=0, division_id=3,
                                          rank=2, team_id=afc_south_second, pick_type=1)
        session.add(afc_south_second_db)

        afc_south_last_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, conf_id=0, division_id=3,
                                        rank=4, team_id=afc_south_last, pick_type=1)

        session.add(afc_south_last_db)

        afc_west_winner_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, conf_id=0, division_id=4,
                                         rank=1, team_id=afc_west_winner_pick, pick_type=1)
        session.add(afc_west_winner_db)
        afc_west_second_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, conf_id=0, division_id=4,
                                         rank=2, team_id=afc_west_second, pick_type=1)
        session.add(afc_west_second_db)

        afc_west_last_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, conf_id=0, division_id=4,
                                       rank=4, team_id=afc_west_last, pick_type=1)

        session.add(afc_west_last_db)

        # Add AFC team picks
        nfc_east_winner_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, conf_id=1, division_id=1,
                                         rank=1, team_id=nfc_east_winner_pick, pick_type=1)
        session.add(nfc_east_winner_db)
        nfc_east_second_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, conf_id=1, division_id=1,
                                         rank=2, team_id=nfc_east_second, pick_type=1)
        session.add(nfc_east_second_db)

        nfc_east_last_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, conf_id=1, division_id=1,
                                       rank=4, team_id=nfc_east_last, pick_type=1)

        session.add(nfc_east_last_db)

        nfc_north_winner_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, conf_id=1, division_id=2,
                                          rank=1, team_id=nfc_north_winner_pick, pick_type=1)
        session.add(nfc_north_winner_db)
        nfc_north_second_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, conf_id=1, division_id=2,
                                          rank=2, team_id=nfc_north_second, pick_type=1)
        session.add(nfc_north_second_db)

        nfc_north_last_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, conf_id=1, division_id=2,
                                        rank=4, team_id=nfc_north_last, pick_type=1)

        session.add(nfc_north_last_db)

        nfc_south_winner_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, conf_id=1, division_id=3,
                                          rank=1, team_id=nfc_south_winner_pick, pick_type=1)
        session.add(nfc_south_winner_db)
        nfc_south_second_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, conf_id=1, division_id=3,
                                          rank=2, team_id=nfc_south_second, pick_type=1)
        session.add(nfc_south_second_db)

        nfc_south_last_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, conf_id=1, division_id=3,
                                        rank=4, team_id=nfc_south_last, pick_type=1)

        session.add(nfc_south_last_db)

        nfc_west_winner_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, conf_id=1, division_id=4,
                                         rank=1, team_id=nfc_west_winner_pick, pick_type=1)
        session.add(nfc_west_winner_db)
        nfc_west_second_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, conf_id=1, division_id=4,
                                         rank=2, team_id=nfc_west_second, pick_type=1)
        session.add(nfc_west_second_db)

        nfc_west_last_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, conf_id=1, division_id=4,
                                       rank=4, team_id=nfc_west_last, pick_type=1)

        session.add(nfc_west_last_db)

        # Add AFC Player Picks

        afc_passing_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, player_id=afc_qb_pick,
                                     pick_type=4, conf_id=0)
        session.add(afc_passing_db)

        afc_rushing_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, player_id=afc_rb_pick,
                                     pick_type=5, conf_id=0)
        session.add(afc_rushing_db)

        afc_receiving_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, player_id=afc_rec_pick,
                                       pick_type=6, conf_id=0)
        session.add(afc_receiving_db)

        afc_sacks_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, player_id=afc_sacks_pick,
                                   pick_type=7, conf_id=0)
        session.add(afc_sacks_db)

        afc_int_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, player_id=afc_int_pick,
                                 pick_type=8, conf_id=0)
        session.add(afc_int_db)
        
        # Add NFC Player Picks
        
        nfc_passing_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, player_id=nfc_qb_pick,
                                     pick_type=4, conf_id=1)
        session.add(nfc_passing_db)

        nfc_rushing_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, player_id=nfc_rb_pick,
                                     pick_type=5, conf_id=1)
        session.add(nfc_rushing_db)

        nfc_receiving_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, player_id=nfc_rec_pick,
                                       pick_type=6, conf_id=1)
        session.add(nfc_receiving_db)

        nfc_sacks_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, player_id=nfc_sacks_pick,
                                   pick_type=7, conf_id=1)
        session.add(nfc_sacks_db)

        nfc_int_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, player_id=nfc_int_pick,
                                 pick_type=8, conf_id=1)
        session.add(nfc_int_db)

        # Add the wildcard picks
        afc_wildcard1_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, team_id=afc_wildcard1_pick,
                                       pick_type=9, conf_id=0)
        session.add(afc_wildcard1_db)

        afc_wildcard2_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, team_id=afc_wildcard2_pick,
                                       pick_type=9, conf_id=0)
        session.add(afc_wildcard2_db)
        
        nfc_wildcard1_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, team_id=nfc_wildcard1_pick,
                                       pick_type=9, conf_id=1)
        session.add(nfc_wildcard1_db)

        nfc_wildcard2_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, team_id=nfc_wildcard2_pick,
                                       pick_type=9, conf_id=1)
        session.add(nfc_wildcard2_db)

        # Add the Points For picks
        afc_pf_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, team_id=afc_pf_pick,
                                pick_type=3, conf_id=0)
        session.add(afc_pf_db)

        nfc_pf_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, team_id=nfc_pf_pick,
                                pick_type=3, conf_id=1)
        session.add(nfc_pf_db)

        # Add the tiebreaker
        specialteams_tiebreaker_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt,
                                                 team_id=specialteams_td_pick, pick_type=10)
        session.add(specialteams_tiebreaker_db)
        session.commit()

    @classmethod
    def change_player_picks(cls, afc_east_winner_pick: int, afc_east_second: int, afc_east_last: int,
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

        """Update the player_picks table with the changes the pool player wants to make."""
        session = DbSessionFactory.create_session()
        season_row = session.query(SeasonInfo.current_season).filter(SeasonInfo.id == 1).first()
        season = season_row.current_season

        now_time = TimeService.get_time()

        # Update Pick Type 1 - AFC East Winner
        if afc_east_winner_pick != session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.rank == 1) \
                .filter(PlayerPicks.conf_id == 0) \
                .filter(PlayerPicks.division_id == 1):
            session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id).filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.rank == 1) \
                .filter(PlayerPicks.conf_id == 0) \
                .filter(PlayerPicks.division_id == 1) \
                .update({"team_id": afc_east_winner_pick, "date_submitted": now_time})

        # Update AFC East 2nd place
        if afc_east_second != session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.rank == 2) \
                .filter(PlayerPicks.conf_id == 0) \
                .filter(PlayerPicks.division_id == 1):
            session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id).filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.rank == 2) \
                .filter(PlayerPicks.conf_id == 0) \
                .filter(PlayerPicks.division_id == 1) \
                .update({"team_id": afc_east_second, "date_submitted": now_time})
                
        # Update AFC East Last place team
        if afc_east_last != session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.rank == 4) \
                .filter(PlayerPicks.conf_id == 0) \
                .filter(PlayerPicks.division_id == 1):
            session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id).filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.rank == 4) \
                .filter(PlayerPicks.conf_id == 0) \
                .filter(PlayerPicks.division_id == 1) \
                .update({"team_id": afc_east_last, "date_submitted": now_time})

        # Update Pick Type 1 - AFC North Winner
        if afc_north_winner_pick != session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.rank == 1) \
                .filter(PlayerPicks.conf_id == 0) \
                .filter(PlayerPicks.division_id == 2):
            session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id).filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.rank == 1) \
                .filter(PlayerPicks.conf_id == 0) \
                .filter(PlayerPicks.division_id == 2) \
                .update({"team_id": afc_north_winner_pick, "date_submitted": now_time})

        # Update AFC North 2nd place
        if afc_north_second != session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.rank == 2) \
                .filter(PlayerPicks.conf_id == 0) \
                .filter(PlayerPicks.division_id == 2):
            session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id).filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.rank == 2) \
                .filter(PlayerPicks.conf_id == 0) \
                .filter(PlayerPicks.division_id == 2) \
                .update({"team_id": afc_north_second, "date_submitted": now_time})

        # Update AFC North Last place team
        if afc_north_last != session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.rank == 4) \
                .filter(PlayerPicks.conf_id == 0) \
                .filter(PlayerPicks.division_id == 2):
            session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id).filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.rank == 4) \
                .filter(PlayerPicks.conf_id == 0) \
                .filter(PlayerPicks.division_id == 2) \
                .update({"team_id": afc_north_last, "date_submitted": now_time})

        # Update Pick Type 1 - AFC South Winner
        if afc_south_winner_pick != session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.rank == 1) \
                .filter(PlayerPicks.conf_id == 0) \
                .filter(PlayerPicks.division_id == 3):
            session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id).filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.rank == 1) \
                .filter(PlayerPicks.conf_id == 0) \
                .filter(PlayerPicks.division_id == 3) \
                .update({"team_id": afc_south_winner_pick, "date_submitted": now_time})

        # Update AFC South 2nd place
        if afc_south_second != session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.rank == 2) \
                .filter(PlayerPicks.conf_id == 0) \
                .filter(PlayerPicks.division_id == 1):
            session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id).filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.rank == 2) \
                .filter(PlayerPicks.conf_id == 0) \
                .filter(PlayerPicks.division_id == 3) \
                .update({"team_id": afc_south_second, "date_submitted": now_time})

        # Update AFC South Last place team
        if afc_south_last != session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.rank == 4) \
                .filter(PlayerPicks.conf_id == 0) \
                .filter(PlayerPicks.division_id == 3):
            session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id).filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.rank == 4) \
                .filter(PlayerPicks.conf_id == 0) \
                .filter(PlayerPicks.division_id == 3) \
                .update({"team_id": afc_south_last, "date_submitted": now_time})

        # Update Pick Type 1 - AFC West Winner
        if afc_west_winner_pick != session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.rank == 1) \
                .filter(PlayerPicks.conf_id == 0) \
                .filter(PlayerPicks.division_id == 4):
            session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id).filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.rank == 1) \
                .filter(PlayerPicks.conf_id == 0) \
                .filter(PlayerPicks.division_id == 4) \
                .update({"team_id": afc_west_winner_pick, "date_submitted": now_time})

        # Update AFC West 2nd place
        if afc_west_second != session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.rank == 2) \
                .filter(PlayerPicks.conf_id == 0) \
                .filter(PlayerPicks.division_id == 1):
            session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id).filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.rank == 2) \
                .filter(PlayerPicks.conf_id == 0) \
                .filter(PlayerPicks.division_id == 4) \
                .update({"team_id": afc_west_second, "date_submitted": now_time})

        # Update AFC West Last place team
        if afc_west_last != session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.rank == 4) \
                .filter(PlayerPicks.conf_id == 0) \
                .filter(PlayerPicks.division_id == 4):
            session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id).filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.rank == 4) \
                .filter(PlayerPicks.conf_id == 0) \
                .filter(PlayerPicks.division_id == 4) \
                .update({"team_id": afc_west_last, "date_submitted": now_time})

        # Update Pick Type 1 - NFC East Winner
        if nfc_east_winner_pick != session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.rank == 1) \
                .filter(PlayerPicks.conf_id == 1) \
                .filter(PlayerPicks.division_id == 1):
            session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id).filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.rank == 1) \
                .filter(PlayerPicks.conf_id == 1) \
                .filter(PlayerPicks.division_id == 1) \
                .update({"team_id": nfc_east_winner_pick, "date_submitted": now_time})

        # Update NFC East 2nd place
        if nfc_east_second != session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.rank == 2) \
                .filter(PlayerPicks.conf_id == 1) \
                .filter(PlayerPicks.division_id == 1):
            session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id).filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.rank == 2) \
                .filter(PlayerPicks.conf_id == 1) \
                .filter(PlayerPicks.division_id == 1) \
                .update({"team_id": nfc_east_second, "date_submitted": now_time})

        # Update NFC East Last place team
        if nfc_east_last != session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.rank == 4) \
                .filter(PlayerPicks.conf_id == 1) \
                .filter(PlayerPicks.division_id == 1):
            session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id).filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.rank == 4) \
                .filter(PlayerPicks.conf_id == 1) \
                .filter(PlayerPicks.division_id == 1) \
                .update({"team_id": nfc_east_last, "date_submitted": now_time})

        # Update Pick Type 1 - NFC North Winner
        if nfc_north_winner_pick != session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.rank == 1) \
                .filter(PlayerPicks.conf_id == 1) \
                .filter(PlayerPicks.division_id == 2):
            session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id).filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.rank == 1) \
                .filter(PlayerPicks.conf_id == 1) \
                .filter(PlayerPicks.division_id == 2) \
                .update({"team_id": nfc_north_winner_pick, "date_submitted": now_time})

        # Update NFC North 2nd place
        if nfc_north_second != session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.rank == 2) \
                .filter(PlayerPicks.conf_id == 1) \
                .filter(PlayerPicks.division_id == 2):
            session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id).filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.rank == 2) \
                .filter(PlayerPicks.conf_id == 1) \
                .filter(PlayerPicks.division_id == 2) \
                .update({"team_id": nfc_north_second, "date_submitted": now_time})

        # Update NFC North Last place team
        if nfc_north_last != session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.rank == 4) \
                .filter(PlayerPicks.conf_id == 1) \
                .filter(PlayerPicks.division_id == 2):
            session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id).filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.rank == 4) \
                .filter(PlayerPicks.conf_id == 1) \
                .filter(PlayerPicks.division_id == 2) \
                .update({"team_id": nfc_north_last, "date_submitted": now_time})

        # Update Pick Type 1 - NFC South Winner
        if nfc_south_winner_pick != session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.rank == 1) \
                .filter(PlayerPicks.conf_id == 1) \
                .filter(PlayerPicks.division_id == 3):
            session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id).filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.rank == 1) \
                .filter(PlayerPicks.conf_id == 1) \
                .filter(PlayerPicks.division_id == 3) \
                .update({"team_id": nfc_south_winner_pick, "date_submitted": now_time})

        # Update NFC South 2nd place
        if nfc_south_second != session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.rank == 2) \
                .filter(PlayerPicks.conf_id == 1) \
                .filter(PlayerPicks.division_id == 1):
            session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id).filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.rank == 2) \
                .filter(PlayerPicks.conf_id == 1) \
                .filter(PlayerPicks.division_id == 3) \
                .update({"team_id": nfc_south_second, "date_submitted": now_time})

        # Update NFC South Last place team
        if nfc_south_last != session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.rank == 4) \
                .filter(PlayerPicks.conf_id == 1) \
                .filter(PlayerPicks.division_id == 3):
            session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id).filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.rank == 4) \
                .filter(PlayerPicks.conf_id == 1) \
                .filter(PlayerPicks.division_id == 3) \
                .update({"team_id": nfc_south_last, "date_submitted": now_time})

        # Update Pick Type 1 - NFC West Winner
        if nfc_west_winner_pick != session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.rank == 1) \
                .filter(PlayerPicks.conf_id == 1) \
                .filter(PlayerPicks.division_id == 4):
            session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id).filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.rank == 1) \
                .filter(PlayerPicks.conf_id == 1) \
                .filter(PlayerPicks.division_id == 4) \
                .update({"team_id": nfc_west_winner_pick, "date_submitted": now_time})

        # Update NFC West 2nd place
        if nfc_west_second != session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.rank == 2) \
                .filter(PlayerPicks.conf_id == 1) \
                .filter(PlayerPicks.division_id == 1):
            session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id).filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.rank == 2) \
                .filter(PlayerPicks.conf_id == 1) \
                .filter(PlayerPicks.division_id == 4) \
                .update({"team_id": nfc_west_second, "date_submitted": now_time})

        # Update NFC West Last place team
        if nfc_west_last != session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.rank == 4) \
                .filter(PlayerPicks.conf_id == 1) \
                .filter(PlayerPicks.division_id == 4):
            session.query(PlayerPicks).filter(PlayerPicks.user_id == user_id).filter(PlayerPicks.pick_type == 1) \
                .filter(PlayerPicks.season == season) \
                .filter(PlayerPicks.rank == 4) \
                .filter(PlayerPicks.conf_id == 1) \
                .filter(PlayerPicks.division_id == 4) \
                .update({"team_id": nfc_west_last, "date_submitted": now_time})

        # TODO Add pick types 2-10


class DisplayPlayerPicks:

    @staticmethod
    def display_picks(user_id):

        session = DbSessionFactory.create_session()
        season_row = session.query(SeasonInfo.current_season).filter(SeasonInfo.id == 1).first()
        season = season_row.current_season

        user_query = session.query(PlayerPicks, TeamInfo.name).join(TeamInfo, PlayerPicks.afc_east_first == TeamInfo.team_id)\
            .filter(PlayerPicks.user_id == user_id) \
            .filter(PlayerPicks.season == season).all()

        return user_query

