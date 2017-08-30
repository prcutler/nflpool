from nflpool.data.seasoninfo import SeasonInfo
from nflpool.data.dbsession import DbSessionFactory


class NewSeasonService:
    @staticmethod
    def get_install():
        return []

    '''After first time installation or before a new season starts, this will update the season year
    in the database.  This is used to for the MySportsFeeds API to get the correct year of stats needed.'''
    # TODO Add logging
    @classmethod
    def create_season(cls, season, season_start_date):
        session = DbSessionFactory.create_session()
        season_row = session.query(SeasonInfo)

        if season_row.count() == 0:
            print("New install, adding a season")
            new_season = SeasonInfo()
            new_season.current_season = season
            new_season.season_start_date = season_start_date
            session.add(new_season)
            session.commit()
        else:
            print("Existing season found, updating to new year")

            update_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
            update_row.current_season = season
            update_row.season_start_date = season_start_date

            session.commit()
