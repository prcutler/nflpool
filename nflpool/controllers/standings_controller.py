import pyramid_handlers
from nflpool.controllers.base_controller import BaseController
from nflpool.viewmodels.standings_viewmodel import StandingsViewModel
from nflpool.services.standings_service import StandingsService
from nflpool.data.dbsession import DbSessionFactory
from nflpool.data.seasoninfo import SeasonInfo
from nflpool.data.weekly_player_results import WeeklyPlayerResults


class StandingsController(BaseController):
    @pyramid_handlers.action(renderer='templates/standings/standings.pt')
    def index(self):
        """Get a list of all seasons played from the database and display a bulleted list for the user to
        choose which season to view standings for"""
        seasons_played = StandingsService.all_seasons_played()

        return {'seasons': seasons_played}

    @pyramid_handlers.action(renderer='templates/standings/season.pt',
                             request_method='GET',
                             name='season')
    def season(self):

        season = self.request.matchdict['id']

        # TODO - Need to pass the season variable above to StandingsService.display_weekly_standings(season)

        current_standings = StandingsService.display_weekly_standings(season)

        session = DbSessionFactory.create_session()
        # season_row = session.query(SeasonInfo.current_season).filter(SeasonInfo.id == '1').first()
        # season = season_row.current_season

        week_query = session.query(WeeklyPlayerResults.week).order_by(WeeklyPlayerResults.week.desc()).first()
        week = week_query[0]

        if week >= 17:
            week = 'Final'
        else:
            week = 'Week ' + str(week_query[0])

        return {'current_standings': current_standings, 'season': season, 'week': week}

    @pyramid_handlers.action(renderer='templates/standings/player-standings.pt',
                             request_method='GET',
                             name='player-standings')
    def player_standings_get(self):
        # vm = StandingsViewModel()
        # vm.from_dict(self.data_dict)

        season = self.request.matchdict['id']
        player = self.request.matchdict['element']
        print(season, player)

        player_standings = StandingsService.display_player_standings(player, season)

        first_name = (player_standings[0]['first_name'])
        last_name = (player_standings[0]['last_name'])

        return {'first_name': first_name, 'last_name': last_name, 'player_standings': player_standings}