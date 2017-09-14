import pyramid_handlers
from nflpool.controllers.base_controller import BaseController
from nflpool.viewmodels.newinstallviewmodel import NewInstallViewModel
from nflpool.viewmodels.newseasonviewmodel import NewSeasonViewModel
from nflpool.viewmodels.update_nflplayers_viewmodel import UpdateNFLPlayersViewModel
from nflpool.services.new_install_service import NewInstallService
from nflpool.services.new_season_service import NewSeasonService
from nflpool.services.activeplayers_service import ActivePlayersService
from nflpool.viewmodels.update_nflschedule_viewmodel import UpdateNFLScheduleViewModel
from nflpool.services.update_nflschedule_service import UpdateScheduleService
from nflpool.data.account import Account
from nflpool.data.dbsession import DbSessionFactory
from nflpool.services.admin_service import AccountService
from nflpool.viewmodels.update_weekly_stats_viewmodel import UpdateWeeklyStats
from nflpool.services.weekly_msf_data import WeeklyTeamStats
from nflpool.services.weekly_msf_data import WeeklyStatsService
from nflpool.viewmodels.update_unique_picks_viewmodel import UniquePicksViewModel
from nflpool.services.unique_picks_service import UniquePicksService
from nflpool.services.standings_service import StandingsService




class AdminController(BaseController):
    @pyramid_handlers.action(renderer='templates/admin/index.pt')
    def index(self):
        session = DbSessionFactory.create_session()
        su__query = session.query(Account.id).filter(Account.is_super_user == 1)\
            .filter(Account.id == self.logged_in_user_id).first()

        if su__query is None:
            print("You must be an administrator to view this page")
            self.redirect('/home')

        return {}

    # GET /admin/new_install
    @pyramid_handlers.action(renderer='templates/admin/new_install.pt',
                             request_method='GET',
                             name='new_install')
    def new_install_get(self):
        session = DbSessionFactory.create_session()
        su__query = session.query(Account.id).filter(Account.is_super_user == 1)\
            .filter(Account.id == self.logged_in_user_id).first()

        if su__query is None:
            print("You must be an administrator to view this page")
            self.redirect('/home')

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
        NewInstallService.get_team_info()
        NewInstallService.create_division_info()
        NewInstallService.create_conference_info()
        NewInstallService.create_pick_types()
        NewInstallService.create_pick_type_points()

        # redirect
        self.redirect('/admin/new_season')

    @pyramid_handlers.action(renderer='templates/admin/new_season.pt',
                             request_method='GET',
                             name='new_season')
    def new_season_get(self):
        session = DbSessionFactory.create_session()
        su__query = session.query(Account.id).filter(Account.is_super_user == 1)\
            .filter(Account.id == self.logged_in_user_id).first()

        if su__query is None:
            print("You must be an administrator to view this page")
            self.redirect('/home')

        vm = NewSeasonViewModel()
        return vm.to_dict()

    @pyramid_handlers.action(renderer='templates/admin/new_season.pt',
                             request_method='POST',
                             name='new_season')
    def new_season_post(self):
        vm = NewSeasonViewModel()
        vm.from_dict(self.request.POST)

        # Insert NFLPlayer info
        new_season_input = NewSeasonService.create_season(vm.new_season_input, vm.season_start_date_input)

        # redirect
        self.redirect('/admin/update_nflplayers')

    @pyramid_handlers.action(renderer='templates/admin/update_nflplayers.pt',
                             request_method='GET',
                             name='update_nflplayers')
    def update_nfl_players(self):
        session = DbSessionFactory.create_session()
        su__query = session.query(Account.id).filter(Account.is_super_user == 1)\
            .filter(Account.id == self.logged_in_user_id).first()

        if su__query is None:
            print("You must be an administrator to view this page")
            self.redirect('/home')

        vm = UpdateNFLPlayersViewModel()
        return vm.to_dict()

    @pyramid_handlers.action(renderer='templates/admin/update_nflplayers.pt',
                             request_method='POST',
                             name='update_nflplayers')
    def update_nfl_players_post(self):
        vm = UpdateNFLPlayersViewModel()
        vm.from_dict(self.request.POST)

        # Insert NFLPlayer info
        active_players = ActivePlayersService.add_active_nflplayers(vm.firstname, vm.lastname, vm.player_id,
                                                                    vm.team_id, vm.position, vm.season)

        # redirect
        self.redirect('/admin/update_nflschedule')

    @pyramid_handlers.action(renderer='templates/admin/update_nflschedule.pt',
                             request_method='GET',
                             name='update_nflschedule')
    def update_nfl_schedule(self):
        session = DbSessionFactory.create_session()
        su__query = session.query(Account.id).filter(Account.is_super_user == 1)\
            .filter(Account.id == self.logged_in_user_id).first()

        if su__query is None:
            print("You must be an administrator to view this page")
            self.redirect('/home')

        vm = UpdateNFLScheduleViewModel()
        return vm.to_dict()

    @pyramid_handlers.action(renderer='templates/admin/update_nflschedule.pt',
                             request_method='POST',
                             name='update_nflschedule')
    def update_nfl_schedule_post(self):
        vm = UpdateNFLScheduleViewModel()
        vm.from_dict(self.request.POST)

        # Insert NFL Schedule
        update_nflschedule = UpdateScheduleService.update_nflschedule(vm.game_id, vm.game_date, vm.away_team,
                                                                      vm.home_team, vm.week, vm.season)

        # redirect
        self.redirect('/admin')

    @pyramid_handlers.action(renderer='templates/admin/account-list.pt',
                             request_method='GET',
                             name='account-list')
    def list_accounts(self):

        # Show list of accounts
        account_list = AccountService.get_all_accounts()

        return {'account_list': account_list}

    @pyramid_handlers.action(renderer='templates/admin/update-weekly-stats.pt',
                             request_method='GET',
                             name='update-weekly-stats')
    def update_weekly_stats(self):
        session = DbSessionFactory.create_session()
        su__query = session.query(Account.id).filter(Account.is_super_user == 1)\
            .filter(Account.id == self.logged_in_user_id).first()

        if su__query is None:
            print("You must be an administrator to view this page")
            self.redirect('/home')

        vm = UpdateWeeklyStats()
        return vm.to_dict()

    @pyramid_handlers.action(renderer='templates/admin/update-weekly-stats.pt',
                             request_method='POST',
                             name='update-weekly-stats')
    def update_weekly_stats_post(self):
        vm = UpdateWeeklyStats()
        vm.from_dict(self.request.POST)

        # Insert weekly team and player stats
        #WeeklyStatsService.get_qb_stats()
        #WeeklyStatsService.get_rb_stats()
        #WeeklyStatsService.get_rec_stats()
        #WeeklyStatsService.get_sack_stats()
        #WeeklyStatsService.get_interception_stats()
        #WeeklyStatsService.get_team_rankings()
        #WeeklyStatsService.get_conference_standings()
        #WeeklyStatsService.get_points_for()
        #WeeklyStatsService.get_tiebreaker()
        StandingsService.update_player_pick_points()
        StandingsService.update_team_pick_points()


        # redirect
        self.redirect('/admin')

    @pyramid_handlers.action(renderer='templates/admin/update-unique-picks.pt',
                             request_method='GET',
                             name='update-unique-picks')
    def update_unique_picks(self):
        session = DbSessionFactory.create_session()
        su__query = session.query(Account.id).filter(Account.is_super_user == 1)\
            .filter(Account.id == self.logged_in_user_id).first()

        if su__query is None:
            print("You must be an administrator to view this page")
            self.redirect('/home')

        vm = UniquePicksViewModel()
        return vm.to_dict()

    @pyramid_handlers.action(renderer='templates/admin/update-unique-picks.pt',
                             request_method='POST',
                             name='update-unique-picks')
    def update_unique_picks_post(self):
        vm = UniquePicksViewModel()
        vm.from_dict(self.request.POST)

        # Find all unique picks for each player
        #team type picks
        picktype=1
        conf = 0
        div=1
        while conf < 2:
            rank = 1
            UniquePicksService.unique_team_picks(picktype, conf, div, rank)
            rank = 2
            UniquePicksService.unique_team_picks(picktype, conf, div, rank)
            rank = 4
            UniquePicksService.unique_team_picks(picktype, conf, div, rank)
            div += 1
            if div>4 :
                div = 1
                conf +=1

        picktype = 9
        conf = 0
        UniquePicksService.unique_team_picks(picktype, conf)
        conf = 1
        UniquePicksService.unique_team_picks(picktype, conf)

        picktype = 10
        UniquePicksService.unique_team_picks(picktype)

        picktype = 4
        conf = 0
        while picktype < 9:
            UniquePicksService.unique_player_picks(picktype, conf)
            conf +=1
            if conf > 1:
                picktype += 1
                conf = 0


        # redirect
        self.redirect('/admin')
