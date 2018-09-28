import pendulum
from nflpool.data.seasoninfo import SeasonInfo
from nflpool.data.dbsession import DbSessionFactory


class TimeService:
    @staticmethod
    def get_time():
        """Create a service to get the time - there were too many instances of getting the current time in
        the codebase making testing difficult."""
        # Change now_time for testing
        # Use this one for production:
        now_time = pendulum.now(tz=pendulum.timezone("America/New_York"))
        # Use this one for testing:
        # now_time = pendulum.datetime(2018, 9, 18, 6, 21, tz='America/New_York')

        return now_time

    @staticmethod
    def get_week():
        session = DbSessionFactory.create_session()
        season_row = session.query(SeasonInfo).filter(SeasonInfo.id == "1").first()

        season_start = pendulum.parse(season_row.season_start_date)

        diff = TimeService.get_time() - season_start
        week = int((diff.days / 7) + 1)

        return week
