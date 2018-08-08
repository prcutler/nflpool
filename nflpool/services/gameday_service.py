import pendulum
from nflpool.data.seasoninfo import SeasonInfo
from nflpool.data.dbsession import DbSessionFactory
from nflpool.services.time_service import TimeService


# Set the timezone we will be working with
timezone = pendulum.timezone('America/New_York')

# Don't change this - change the now_time in TimeService
now_time = TimeService.get_time()


def season_opener():

    session = DbSessionFactory.create_session()

    season_start_query = session.query(SeasonInfo.season_start_date).first()
    # print("Season Start Query:", season_start_query)

    # season_start_query is returned as a tuple and need to get the first part of the tuple:
    season_opener_date = str(season_start_query[0])

    # Convert the start date to a string that Pendulum can work with
    # season_start_date_convert = \
    #    pendulum.from_format(season_opener_date, '%Y-%m-%d %H:%M:%S', timezone).to_datetime_string()

    # Use the string above in a Pendulum instance and get the time deltas needed
    season_start_date = pendulum.parse(season_opener_date, tz=timezone)

    session.close()

    return season_start_date


class GameDayService:
    @staticmethod
    def admin_check():
        session = DbSessionFactory.create_session()

        season_start_query = session.query(SeasonInfo.season_start_date).first()

        session.close()

        return season_start_query

    @staticmethod
    def season_opener_date():
        """Get the time of the season opener's game"""

        season_opener_date = season_opener()

        return season_opener_date

    @staticmethod
    def timezone():
        tz = pendulum.timezone('America/New_York')

        return tz

    @staticmethod
    def time_due():
        season_start_date = season_opener()
        time_due = season_start_date.format('h:m A')
        # print("Season start date", season_start_date, "time_due", time_due)

        return time_due

    @staticmethod
    def picks_due():
        season_start_date = season_opener()
        picks_due_date = season_start_date.to_formatted_date_string()
        # print("picks_due_date", picks_due_date)

        return picks_due_date

    @staticmethod
    def delta_days():

        season_start_date = season_opener()
        now = now_time

        delta = season_start_date - now
        days = delta.days

        return days

    @staticmethod
    def delta_hours():

        season_start_date = season_opener()
        now = now_time

        delta = season_start_date - now
        hours = delta.hours

        return hours

    @staticmethod
    def delta_minutes():

        season_start_date = season_opener()
        now = now_time

        delta = season_start_date - now
        minutes = delta.minutes

        return minutes

