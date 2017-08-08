import pyramid_handlers
from nflpool.controllers.base_controller import BaseController
from nflpool.services.account_service import AccountService
from nflpool.services.playerpicks_service import PlayerPicksService
from nflpool.viewmodels.playerpicks_viewmodel import PlayerPicksViewModel


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

        # Return the models
        return {
            'afc_east': afc_east_list,
            'afc_north': afc_north_list
        }

    # POST /picks/submit_picks
    @pyramid_handlers.action(renderer='templates/picks/submit_picks.pt',
                             request_method='POST',
                             name='submit_picks')
    def submit_player_picks_post(self):
        vm = PlayerPicksViewModel()
        vm.from_dict(self.request.POST)

        # Insert a player's picks
        player_picks = PlayerPicksService.get_player_picks(vm.afc_east_winner, vm.afc_east_second,
                                                           vm.afc_north_winner, vm.afc_north_second,
                                                           )

        # redirect
        # TODO: Create review page before database?
