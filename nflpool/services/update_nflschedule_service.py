import requests
from nflpool.data.dbsession import DbSessionFactory
from nflpool.data.nflschedule import NFLSchedule
import nflpool.data.secret as secret
from requests.auth import HTTPBasicAuth
from nflpool.data.seasoninfo import SeasonInfo


class ActivePlayersService:
    @classmethod
    def update_nflschedule(cls, season: int, game_id: int, game_date: str, away_team: int,
                              home_team: int, week: int):

        session = DbSessionFactory.create_session()

        season_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season

        response = requests.get('https://api.mysportsfeeds.com/v1.1/pull/nfl/' + str(season) +
                                '-regular/full_game_schedule.json',
                                auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

        schedule_query = response.json()
        schedule = player_info["fullgameschedule"]["gameentry"]

        for teams in schedule:
            try:
                game_id = schedule["id"]
                week = schedule["week"]
                game_date = schedule["game_date"]
                away_team = schedule["away_team"]["ID"]
                home_team = schedule["home_team"]["ID"]
            except KeyError:
                continue

            schedule_info = NFLSchedule(game_id=game_id, game_date=game_date, away_team=away_team,
                                        home_team=home_team, week=week, season=season)

            session.add(schedule_info)

            session.commit()
