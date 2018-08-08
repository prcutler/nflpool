from nflpool.data.seasoninfo import SeasonInfo
from nflpool.data.dbsession import DbSessionFactory
import requests
import pendulum
import nflpool.data.secret as secret
from requests.auth import HTTPBasicAuth


class NewSeasonService:
    @staticmethod
    def get_install():
        return []

    '''After first time installation or before a new season starts, this will update the season year
    in the database.  This is used to for the MySportsFeeds API to get the correct year of stats needed.'''
    # TODO Add logging
    @classmethod
    def create_season(cls, season):
        session = DbSessionFactory.create_session()
        season_row = session.query(SeasonInfo)

        if season_row.count() == 0:
            print("New install, adding a season")

            response = requests.get('https://api.mysportsfeeds.com/v1.2/pull/nfl/' + str(season) +
                                    '-regular/full_game_schedule.json',
                                    auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

            gameday_json = response.json()
            gameday_data = gameday_json["fullgameschedule"]["gameentry"][0]

            first_game_date = gameday_data["date"]
            first_game_time = gameday_data["time"]
            away_team = gameday_data["awayTeam"]["Name"]
            home_team = gameday_data["homeTeam"]["Name"]

            first_game = first_game_date + "T" + "0" + first_game_time[:-2]
            first_game_calc = pendulum.parse(first_game)

            if first_game_calc.hour <= 11:
                first_game = first_game_calc.add(hours=12)
                first_game_instance = pendulum.instance(first_game)

            new_season = SeasonInfo(season_start_date=first_game_instance, season_start_time=first_game_time,
                                    home_team=home_team, away_team=away_team, current_season=season)

            session.add(new_season)
            session.commit()

        else:
            print("Existing season found, updating to new year")

            response = requests.get('https://api.mysportsfeeds.com/v1.2/pull/nfl/' + str(season) +
                                    '-regular/full_game_schedule.json',
                                    auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

            gameday_json = response.json()
            gameday_data = gameday_json["fullgameschedule"]["gameentry"][0]

            first_game_date = gameday_data["date"]
            first_game_time = gameday_data["time"]
            away_team = gameday_data["awayTeam"]["Name"]
            home_team = gameday_data["homeTeam"]["Name"]

            first_game = first_game_date + "T" + "0" + first_game_time[:-2]
            first_game_calc = pendulum.parse(first_game)

            if first_game_calc.hour <= 11:
                first_game = first_game_calc.add(hours=12)

            update_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
            update_row.current_season = season
            update_row.season_start_date = pendulum.instance(first_game)
            update_row.season_start_time = first_game_time
            update_row.away_team = away_team
            update_row.home_team = home_team

            session.commit()
