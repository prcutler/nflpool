from nflpool.data.seasoninfo import SeasonInfo
from nflpool.data.dbsession import DbSessionFactory


class NewSeasonService:
    @staticmethod
    def get_install():
        return []

    @classmethod
    def create_season(cls, season):
        session = DbSessionFactory.create_session()
        season_row = session.query(SeasonInfo)

        if season_row.count() == 0:
            print("New install, adding a season")
            new_season = SeasonInfo()
            new_season.current_season = season
            session.add(new_season)
            session.commit()
        else:
            print("Existing season found, updating to new year")

            update_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
            update_row.current_season = season

            session.commit()
