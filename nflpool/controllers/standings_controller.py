import pyramid_handlers
from nflpool.controllers.base_controller import BaseController
from nflpool.services.nfl_player_rank_service import interception_leaders
from nflpool.viewmodels.standings_viewmodel import StandingsViewModel
from nflpool.services.standings_service import StandingsService



class StandingsController(BaseController):

    @pyramid_handlers.action(renderer='templates/standings/standings.pt')
    def index(self):
        current_standings = StandingsService.display_weekly_standings()

        return {'current_standings': current_standings}

    @pyramid_handlers.action(renderer='templates/standings/player-standings.pt')
    def player_standings_get(self):
        vm = StandingsViewModel()
        vm.from_dict(self.data_dict)

        print("la la la")
        player = self.request.matchdict['id']

        player_standings = StandingsService.display_player_standings(player)

        print("hi")

        return {'first_name': vm.first_name, 'last_name': vm.last_name, 'player_standings': player_standings}