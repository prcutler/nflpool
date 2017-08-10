import pyramid_handlers
from nflpool.controllers.base_controller import BaseController
from nflpool.viewmodels.newinstallviewmodel import NewInstallViewModel
from nflpool.viewmodels.newseasonviewmodel import NewSeasonViewModel
from nflpool.viewmodels.update_nflplayers_viewmodel import UpdateNFLPlayersViewModel
from nflpool.services.new_install_service import NewInstallService
from nflpool.services.new_season_service import NewSeasonService
from nflpool.services.activeplayers_service import ActivePlayersService
from nflpool.viewmodels.update_nflschedule_viewmodel import UpdateNFLScheduleViewModel
from nflpool.services.update_nflschedule_service import NFLSchedule


class AdminController(BaseController):
    @pyramid_handlers.action(renderer='templates/admin/index.pt')
    def index(self):
        if not self.logged_in_user_id:
            print("Cannot view account page, you must be an administrator")
            self.redirect('/account/signin')

        return {}

    # GET /admin/new_install
    @pyramid_handlers.action(renderer='templates/admin/new_install.pt',
                             request_method='GET',
                             name='new_install')
    def new_install_get(self):
        if not self.logged_in_user_id:
            print("Cannot view account page, you must be an administrator")
            self.redirect('/account/signin')
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
        if not self.logged_in_user_id:
            print("Cannot view account page, you must be an administrator")
            self.redirect('/account/signin')
        vm = NewSeasonViewModel()
        return vm.to_dict()

    @pyramid_handlers.action(renderer='templates/admin/new_season.pt',
                             request_method='POST',
                             name='new_season')
    def new_season_post(self):
        vm = NewSeasonViewModel()
        vm.from_dict(self.request.POST)

        # Insert NFLPlayer info
        new_season_input = NewSeasonService.create_season(vm.new_season_input)

        # redirect
        self.redirect('/admin/update_nflschedule')

    @pyramid_handlers.action(renderer='templates/admin/update_nflschedule.pt',
                             request_method='GET',
                             name='update_nflschedule')
    def update_nfl_schedule(self):
        if not self.logged_in_user_id:
            print("Cannot view account page, you must be an administrator")
            self.redirect('/account/signin')
        vm = UpdateNFLScheduleViewModel()
        return vm.to_dict()

    @pyramid_handlers.action(renderer='templates/admin/update_nflplayers',
                             request_method='POST',
                             name='update_nflschedule')
    def update_nfl_schedule_post(self):
        vm = UpdateNFLScheduleViewModel()
        vm.from_dict(self.request.POST)

        # Insert NFL Schedule
        update_nflschedule = ActivePlayersService.add_active_nflplayers(vm.game_id, vm.game_date, vm.away_team,
                                                                        vm.home_team, vm.week, vm.season)

        # redirect
        self.redirect('/admin')
