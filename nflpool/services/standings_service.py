from nflpool.data.dbsession import DbSessionFactory
from sqlalchemy.orm import joinedload
from nflpool.data.picks import PlayerPicks
from nflpool.data.weekly_results import WeeklyResults



class StandingsService:
    @staticmethod
    def get_seasons():
        session = DbSessionFactory.create_session()

        seasons = session.query(WeeklyResults)
