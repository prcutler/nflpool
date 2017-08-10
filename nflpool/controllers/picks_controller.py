import pyramid_handlers
from nflpool.controllers.base_controller import BaseController
from nflpool.services.account_service import AccountService
from nflpool.services.playerpicks_service import PlayerPicksService
from nflpool.viewmodels.playerpicks_viewmodel import PlayerPicksViewModel
from nflpool.data.dbsession import DbSessionFactory
from nflpool.data.account import Account
from nflpool.data.picks import PlayerPicks
from nflpool.data.seasoninfo import SeasonInfo


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

        session = DbSessionFactory.create_session()
        season_row = session.query(SeasonInfo.current_season).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season

        return {'season': season}

    # Get player picks for the current season
    @pyramid_handlers.action(renderer='templates/picks/submit_picks.pt',
                             request_method='GET',
                             name='submit_picks')
    def submit_player_picks(self):

        if not self.logged_in_user_id:
            print("Cannot view account page, you must be logged in")
            self.redirect('/account/signin')
        else:
            session = DbSessionFactory.create_session()
            season_row = session.query(SeasonInfo.current_season).filter(SeasonInfo.id == '1').first()
            season = season_row.current_season

            print(self.logged_in_user_id)

            user_query = session.query(PlayerPicks.user_id).filter(PlayerPicks.user_id == self.logged_in_user_id)\
                .filter(PlayerPicks.season == season).first()
            print(user_query)
            print(type(user_query))
#            for user in user_pick_list:

            try:
                if self.logged_in_user_id == user_query[0]:
                    print("You have already submitted picks for this season")
                    self.redirect('/picks/completed')
                else:
                    # Data / Service access
                    afc_east_list = PlayerPicksService.get_afc_east_teams()
                    afc_north_list = PlayerPicksService.get_afc_north_teams()
                    afc_south_list = PlayerPicksService.get_afc_south_teams()
                    afc_west_list = PlayerPicksService.get_afc_west_teams()
                    nfc_east_list = PlayerPicksService.get_nfc_east_teams()
                    nfc_north_list = PlayerPicksService.get_nfc_north_teams()
                    nfc_south_list = PlayerPicksService.get_nfc_south_teams()
                    nfc_west_list = PlayerPicksService.get_nfc_west_teams()
                    afc_qb_list = PlayerPicksService.afc_get_qb()
                    nfc_qb_list = PlayerPicksService.nfc_get_qb()
                    afc_rb_list = PlayerPicksService.afc_get_rb()
                    nfc_rb_list = PlayerPicksService.nfc_rb_get()
                    afc_rec_list = PlayerPicksService.afc_get_rec()
                    nfc_rec_list = PlayerPicksService.nfc_get_rec()
                    afc_sacks_list = PlayerPicksService.afc_get_sacks()
                    nfc_sacks_list = PlayerPicksService.nfc_get_sacks()
                    afc_int_list = PlayerPicksService.afc_get_int()
                    nfc_int_list = PlayerPicksService.nfc_get_int()
                    afc_wildcard_list = PlayerPicksService.get_afc_wildcard()
                    nfc_wildcard_list = PlayerPicksService.get_nfc_wildcard()
                    all_team_list = PlayerPicksService.get_all_teams()

                    session = DbSessionFactory.create_session()
                    user_name = session.query(Account.email).filter(Account.id == self.logged_in_user_id).first()

                    # Return the models
                    return {
                        'user_name': user_name[0],
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

            except TypeError:
                # Data / Service access
                afc_east_list = PlayerPicksService.get_afc_east_teams()
                afc_north_list = PlayerPicksService.get_afc_north_teams()
                afc_south_list = PlayerPicksService.get_afc_south_teams()
                afc_west_list = PlayerPicksService.get_afc_west_teams()
                nfc_east_list = PlayerPicksService.get_nfc_east_teams()
                nfc_north_list = PlayerPicksService.get_nfc_north_teams()
                nfc_south_list = PlayerPicksService.get_nfc_south_teams()
                nfc_west_list = PlayerPicksService.get_nfc_west_teams()
                afc_qb_list = PlayerPicksService.afc_get_qb()
                nfc_qb_list = PlayerPicksService.nfc_get_qb()
                afc_rb_list = PlayerPicksService.afc_get_rb()
                nfc_rb_list = PlayerPicksService.nfc_rb_get()
                afc_rec_list = PlayerPicksService.afc_get_rec()
                nfc_rec_list = PlayerPicksService.nfc_get_rec()
                afc_sacks_list = PlayerPicksService.afc_get_sacks()
                nfc_sacks_list = PlayerPicksService.nfc_get_sacks()
                afc_int_list = PlayerPicksService.afc_get_int()
                nfc_int_list = PlayerPicksService.nfc_get_int()
                afc_wildcard_list = PlayerPicksService.get_afc_wildcard()
                nfc_wildcard_list = PlayerPicksService.get_nfc_wildcard()
                all_team_list = PlayerPicksService.get_all_teams()

                session = DbSessionFactory.create_session()
                user_name = session.query(Account.email).filter(Account.id == self.logged_in_user_id).first()

                # Return the models
                return {
                    'user_name': user_name[0],
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





    # POST /picks/submit_picks
    @pyramid_handlers.action(renderer='templates/picks/submit_picks.pt',
                             request_method='POST',
                             name='submit_picks')
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

        # redirect
        # TODO: Create review page before database?
        self.redirect('/picks/completed')


