import pyramid_handlers
from nflpool.controllers.base_controller import BaseController
from nflpool.services.playerpicks_service import PlayerPicksService
from nflpool.services.playerpicks_service import DisplayPlayerPicks
from nflpool.viewmodels.playerpicks_viewmodel import PlayerPicksViewModel
from nflpool.data.dbsession import DbSessionFactory
from nflpool.data.player_picks import PlayerPicks
from nflpool.data.seasoninfo import SeasonInfo
from nflpool.data.nflschedule import NFLSchedule
from nflpool.data.account import Account
import datetime


class PicksController(BaseController):
    @pyramid_handlers.action(renderer='templates/picks/index.pt')
    def index(self):
        if not self.logged_in_user_id:
            print("Cannot view account page, you must be logged in")
            self.redirect('/account/signin')

        return {}

    @pyramid_handlers.action(renderer='templates/picks/completed.pt')
    def completed(self):
        if not self.logged_in_user_id:
            print("Cannot view account page, you must be logged in")
            self.redirect('/account/signin')

#        display_player_picks = DisplayPlayerPicks.display_picks(self.logged_in_user_id)

        session = DbSessionFactory.create_session()
        season_row = session.query(SeasonInfo.current_season).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season

        get_first_name = session.query(Account.first_name).filter(Account.id == self.logged_in_user_id) \
            .first()
        first_name = get_first_name[0]

        return {'season': season,
                'first_name': first_name}

    # Get player picks for the current season
    @pyramid_handlers.action(renderer='templates/picks/submit-picks.pt',
                             request_method='GET',
                             name='submit-picks')
    def submit_player_picks(self):

        if not self.logged_in_user_id:
            print("Cannot view picks page, you must be logged in")
            self.redirect('/account/signin')

        dt = datetime.datetime.now()

        session = DbSessionFactory.create_session()
        season_row = session.query(SeasonInfo.current_season).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season

        first_game = session.query(NFLSchedule.game_date).filter(NFLSchedule.season == season)\
            .filter(NFLSchedule.game_date).order_by(NFLSchedule.game_date).first()

        string_date = first_game[0] + ' 21:59'
        first_game_time = datetime.datetime.strptime(string_date, "%Y-%m-%d %H:%M")

#        if dt > first_game_time:
#            print("Season has already started")
#            self.redirect('/picks/too-late')
#        else:

#            if not self.logged_in_user_id:
#                print("Cannot view account page, you must be logged in")
#                self.redirect('/account/signin')
#            else:
                # Check if user has already submitted picks
        session = DbSessionFactory.create_session()
        season_row = session.query(SeasonInfo.current_season).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season
        print(season)

        user_query = session.query(PlayerPicks.user_id).filter(PlayerPicks.user_id == self.logged_in_user_id)\
            .filter(PlayerPicks.season == season).first()

        if user_query is None:

            # Data / Service access
            afc_east_list = PlayerPicksService.get_team_list(0, 1)
            afc_north_list = PlayerPicksService.get_team_list(0, 2)
            afc_south_list = PlayerPicksService.get_team_list(0, 3)
            afc_west_list = PlayerPicksService.get_team_list(0, 4)
            nfc_east_list = PlayerPicksService.get_team_list(1, 1)
            nfc_north_list = PlayerPicksService.get_team_list(1, 2)
            nfc_south_list = PlayerPicksService.get_team_list(1, 3)
            nfc_west_list = PlayerPicksService.get_team_list(1, 4)
            afc_qb_list = PlayerPicksService.get_player_list(0, 'QB')
            nfc_qb_list = PlayerPicksService.get_player_list(1, 'QB')
            afc_rb_list = PlayerPicksService.get_player_list(0, 'RB')
            nfc_rb_list = PlayerPicksService.get_player_list(1, 'RB')
            afc_rec_list = PlayerPicksService.get_rec_list(0, 'WR', 'TE')
            nfc_rec_list = PlayerPicksService.get_rec_list(1, 'WR', 'TE')
            afc_sacks_list = PlayerPicksService.get_sacks\
                (0, 'DE', 'DT', 'ILB', 'LB', 'MLB', 'NT', 'OLB')
            nfc_sacks_list = PlayerPicksService.get_sacks\
                (1, 'DE', 'DT', 'ILB', 'LB', 'MLB', 'NT', 'OLB')
            afc_int_list = PlayerPicksService.get_int\
                (0, 'CB', 'DB', 'FS', 'SS', 'MLB', 'LB', 'OLB', 'ILB')
            nfc_int_list = PlayerPicksService.get_int\
                (1, 'CB', 'DB', 'FS', 'SS', 'MLB', 'LB', 'OLB', 'ILB')
            afc_wildcard_list = PlayerPicksService.get_afc_wildcard()
            nfc_wildcard_list = PlayerPicksService.get_nfc_wildcard()
            all_team_list = PlayerPicksService.get_all_teams()

            # Get the user ID
            user_id = self.logged_in_user_id
            get_first_name = session.query(Account.first_name).filter(Account.id == self.logged_in_user_id)\
                .first()
            first_name = get_first_name[0]

            # Return the models
            return {
                'season': season,
                'user_id': user_id,
                'first_name': first_name,
                'afc_east': afc_east_list,
                'afc_north': afc_north_list,
                'afc_south': afc_south_list,
                'afc_west': afc_west_list,
                'nfc_east': nfc_east_list,
                'nfc_north': nfc_north_list,
                'nfc_south': nfc_south_list,
                'nfc_west': nfc_west_list,
                'afc_qb_list': afc_qb_list,
                'nfc_qb_list': nfc_qb_list,
                'afc_rb_list': afc_rb_list,
                'nfc_rb_list': nfc_rb_list,
                'afc_rec_list': afc_rec_list,
                'nfc_rec_list': nfc_rec_list,
                'afc_sacks_list': afc_sacks_list,
                'nfc_sacks_list': nfc_sacks_list,
                'afc_int_list': afc_int_list,
                'nfc_int_list': nfc_int_list,
                'afc_wildcard_list': afc_wildcard_list,
                'nfc_wildcard_list': nfc_wildcard_list,
                'all_team_list': all_team_list
            }

        else:
            print("You have already submitted picks for this season")
            self.redirect('/picks/completed')

    # POST /picks/submit_picks
    @pyramid_handlers.action(renderer='templates/picks/submit-picks.pt',
                             request_method='POST',
                             name='submit-picks')
    def submit_player_picks_post(self):
        vm = PlayerPicksViewModel()
        vm.from_dict(self.request.POST)

        # Pass a player's picks to the service to be inserted in the db

        vm.user_id = self.logged_in_user_id

        player_picks = PlayerPicksService.get_player_picks(vm.afc_east_winner_pick, vm.afc_east_second, 
                                                           vm.afc_east_last,
                                                           vm.afc_north_winner_pick, vm.afc_north_second,
                                                           vm.afc_north_last,
                                                           vm.afc_south_winner_pick, vm.afc_south_second,
                                                           vm.afc_south_last,
                                                           vm.afc_west_winner_pick, vm.afc_west_second,
                                                           vm.afc_west_last,
                                                           vm.nfc_east_winner_pick, vm.nfc_east_second,
                                                           vm.nfc_east_last,
                                                           vm.nfc_north_winner_pick, vm.nfc_north_second,
                                                           vm.nfc_north_last,
                                                           vm.nfc_south_winner_pick, vm.nfc_south_second,
                                                           vm.nfc_south_last,
                                                           vm.nfc_west_winner_pick, vm.nfc_west_second,
                                                           vm.nfc_west_last,
                                                           vm.afc_qb_pick, vm.nfc_qb_pick,
                                                           vm.afc_rb_pick, vm.nfc_rb_pick,
                                                           vm.afc_rec_pick, vm.nfc_rec_pick,
                                                           vm.afc_sacks_pick, vm.nfc_sacks_pick,
                                                           vm.afc_int_pick, vm.nfc_int_pick,
                                                           vm.afc_wildcard1_pick, vm.afc_wildcard2_pick,
                                                           vm.nfc_wildcard1_pick, vm.nfc_wildcard2_pick,
                                                           vm.afc_pf_pick, vm.nfc_pf_pick,
                                                           vm.specialteams_td_pick,
                                                           vm.user_id)


        # Log that a user submitted picks
        self.log.notice("Picks submitted by {}.".format(self.logged_in_user.email))

        # redirect
        # TODO: Create review page before database?
        self.redirect('/picks/completed')

    @pyramid_handlers.action(renderer='templates/picks/too-late.pt',
                             request_method='GET',
                             name='too-late')
    def too_late(self):
        if not self.logged_in_user_id:
            print("Cannot view account page, you must be logged in")
            self.redirect('/account/signin')

        session = DbSessionFactory.create_session()
        season_row = session.query(SeasonInfo.current_season).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season

        return {'season': season}
