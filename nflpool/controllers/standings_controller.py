import pyramid_handlers
from nflpool.controllers.base_controller import BaseController
from nflpool.viewmodels.standings_viewmodel import StandingsViewModel
from nflpool.services.standings_service import StandingsService



class StandingsController(BaseController):

    @pyramid_handlers.action(renderer='templates/standings/standings.pt')
    def index(self):
        current_standings = StandingsService.display_weekly_standings()

        return {'current_standings': current_standings}

    @pyramid_handlers.action(renderer='templates/standings/player-standings.pt',
                             request_method='GET',
                             name='player-standings')
    def player_standings_get(self):
        vm = StandingsViewModel()
        vm.from_dict(self.data_dict)

        player = self.request.matchdict['id']

        player_standings = StandingsService.display_player_standings(player)

        first_name = (player_standings[0]['first_name'])
        last_name = (player_standings[0]['last_name'])

        return {'first_name': first_name, 'last_name': last_name, 'player_standings': player_standings}