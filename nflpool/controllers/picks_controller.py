import pyramid_handlers
from nflpool.controllers.base_controller import BaseController
from nflpool.services.account_service import AccountService
from nflpool.viewmodels.playerpicks_viewmodel import PlayerPicksViewModel
import nflpool.infrastructure.cookie_auth as cookie_auth


class PicksController(BaseController):
    @pyramid_handlers.action(renderer='templates/picks/index.pt')
    def index(self):

        return {}

    @pyramid_handlers.action(renderer='templates/picks/submit_picks.pt',
                             request_method='GET',
                             name='submit_picks')
    def submit_picks_get(self):
        if not self.logged_in_user_id:
            print("Cannot view account page, must login")
            self.redirect('/account/signin')

        vm = PlayerPicksViewModel()
        return vm.to_dict()
