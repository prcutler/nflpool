import pyramid_handlers
from nflpool.controllers.base_controller import BaseController
from nflpool.services.account_service import AccountService
from nflpool.services.playerpicks_service import PlayerPicksService
from nflpool.viewmodels.playerpicks_viewmodel import PlayerPicksViewModel
from nflpool.data.dbsession import DbSessionFactory
from nflpool.data.account import Account


class PicksController(BaseController):
    @pyramid_handlers.action(renderer='templates/picks/index.pt')
    def index(self):
        if not self.logged_in_user_id:
            print("Cannot view account page, you must be logged in")
            self.redirect('/account/signin')

        return {}

    # Get player picks for the current season
    @pyramid_handlers.action(renderer='templates/picks/submit_picks.pt',
                             request_method='GET',
                             name='submit_picks')
    def submit_player_picks(self):

        # Data / Service access
        afc_east_list = PlayerPicksService.get_afc_east_teams()
        afc_north_list = PlayerPicksService.get_afc_north_teams()
        afc_south_list = PlayerPicksService.get_afc_south_teams()
        afc_west_list = PlayerPicksService.get_afc_west_teams()
        nfc_east_list = PlayerPicksService.get_nfc_east_teams()
        nfc_north_list = PlayerPicksService.get_nfc_north_teams()
        nfc_south_list = PlayerPicksService.get_nfc_south_teams()
        nfc_west_list = PlayerPicksService.get_nfc_west_teams()

        session = DbSessionFactory.create_session()
        user_name = session.query(Account.email).filter(Account.id == self.logged_in_user_id).first()

        # Return the models
        return {
            'user_name': user_name,
            'afc_east': afc_east_list,
            'afc_north': afc_north_list,
            'afc_south': afc_south_list,
            'afc_west': afc_west_list,
            'nfc_east': nfc_east_list,
            'nfc_north': nfc_north_list,
            'nfc_south': nfc_south_list,
            'nfc_west': nfc_west_list
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

        player_picks = PlayerPicksService.get_player_picks(vm.afc_east_winner, vm.afc_east_second,
                                                           vm.afc_north_winner, vm.afc_north_second,
                                                           vm.user_id)

        # redirect
        # TODO: Create review page before database?
        self.redirect('/picks')


