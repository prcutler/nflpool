from nflpool.data.dbsession import DbSessionFactory
from sqlalchemy.orm import joinedload
from nflpool.data.player_picks import PlayerPicks
from nflpool.data.weekly_player_results import WeeklyPlayerResults


class StandingsService:
    @staticmethod
    def get_seasons():
        session = DbSessionFactory.create_session()

        seasons = session.query(WeeklyResults)
