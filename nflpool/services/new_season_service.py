from nflpool.data.seasoninfo import SeasonInfo
from nflpool.data.dbsession import DbSessionFactory


class NewSeasonService:
    @staticmethod
    def get_install():
        return []

    @staticmethod
    def create_season(season):

        session = DbSessionFactory.create_session()

        new_season = SeasonInfo()

        new_season.current_season = season

        session.add(new_season)

        session.commit()
        return []


