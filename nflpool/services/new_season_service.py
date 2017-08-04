from nflpool.data.seasoninfo import SeasonInfo
from nflpool.data.dbsession import DbSessionFactory


class NewSeasonService:
    @staticmethod
    def get_install():
        return []

    @staticmethod
    def create_season(season):
        session = DbSessionFactory.create_session()

        if session.query(SeasonInfo.current_season).count == 0:

            print("There is no season in the database")
            new_season = SeasonInfo()

            new_season.current_season = season
            session.add(new_season)
            session.commit()

            return []

        else:
            row_data = session.query(SeasonInfo).filter(SeasonInfo.id == '1')
            print(row_data)

            new_season = SeasonInfo()
            print("Adding a new season")

            new_season.current_season = season
            session.add(new_season)
            session.commit()

            return []
