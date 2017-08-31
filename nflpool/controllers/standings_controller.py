import pyramid_handlers
from nflpool.controllers.base_controller import BaseController
from nflpool.services.new_season_service import NewSeasonService
from nflpool.services.nfl_player_rank_service import interception_leaders


class StandingsController(BaseController):
    @pyramid_handlers.action(renderer='templates/standings/standings.pt')
    def index(self):
        # data / service access
        interceptions = interception_leaders()

        return {'interceptions': interceptions}
