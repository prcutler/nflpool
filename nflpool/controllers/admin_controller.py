import pyramid_handlers
from nflpool.controllers.base_controller import BaseController
from nflpool.viewmodels.newinstallviewmodel import NewInstallViewModel
from nflpool.viewmodels.newseasonviewmodel import NewSeasonViewModel
from nflpool.viewmodels.update_nflplayers_viewmodel import UpdateNFLPlayersViewModel
from nflpool.services.new_install_service import NewInstallService
from nflpool.services.new_season_service import NewSeasonService
from nflpool.services.activeplayers_service import ActivePlayersService


class AdminController(BaseController):
    @pyramid_handlers.action(renderer='templates/admin/index.pt')
    def index(self):
        if not self.logged_in_user_id:
            print("Cannot view account page, must login")
            self.redirect('/account/signin')

        return {}

    # GET /admin/new_install
    @pyramid_handlers.action(renderer='templates/admin/new_install.pt',
                             request_method='GET',
                             name='new_install')
    def new_install_get(self):
        vm = NewInstallViewModel()
        return vm.to_dict()

    # POST /admin/new_install
    @pyramid_handlers.action(renderer='templates/admin/new_install.pt',
                             request_method='POST',
                             name='new_install')
    def new_install_post(self):
        vm = NewInstallViewModel()
        vm.from_dict(self.request.POST)

        # Insert team info
        division_data = NewInstallService.get_team_info(vm.city, vm.conference, vm.division, vm.division_abbr,
                                        vm.division_id, vm.name, vm.team_abbr, vm.team_id)

        # redirect
        self.redirect('/admin/new_season')

    @pyramid_handlers.action(renderer='templates/admin/new_season.pt',
                             request_method='GET',
                             name='new_season')
    def new_season_get(self):
        vm = NewSeasonViewModel()
        return vm.to_dict()

    @pyramid_handlers.action(renderer='templates/admin/new_season.pt',
                             request_method='POST',
                             name='new_season')
    def new_season_post(self):
        vm = NewSeasonViewModel()
        vm.from_dict(self.request.POST)

        # Insert NFLPlayer info
        new_season = NewSeasonService.create_season(vm.current_season)

        # redirect
        self.redirect('/update_players')

    @pyramid_handlers.action(renderer='templates/admin/update_nflplayers.pt',
                             request_method='GET',
                             name='update_nflplayers')
    def update_nfl_players(self):
        vm = NewSeasonViewModel()
        return vm.to_dict()

    @pyramid_handlers.action(renderer='templates/admin/update_nflplayers',
                             request_method='POST',
                             name='update_nflplayers')
    def new_season_post(self):
        vm = UpdateNFLPlayersViewModel()
        vm.from_dict(self.request.POST)

        # Insert NFLPlayer info
        active_players = ActivePlayersService.add_active_nflplayers(vm.firstname, vm.lastname, vm.player_id,
                                                                    vm.team_id, vm.position, vm.season)

        # redirect
        self.redirect('/admin')
