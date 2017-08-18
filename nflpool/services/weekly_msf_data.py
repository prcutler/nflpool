from nflpool.data.dbsession import DbSessionFactory
import requests
from nflpool.data.weekly_nflplayer_stats import WeeklyStats


class WeeklyStatsService:
    @staticmethod
    def get_weekly_stats():
        return []

    # Open a connection to the database to get the current season year from the SeasonInfo table
    # Get weekly stats for each player for yards (passing, receiving, rushing), sacks and interceptions
    # TODO: Need to include a date / week field when storing in the database
    @staticmethod
    def get_nflplayer_stats(cls, season: int, player_id: int, passyds = int, rushyds = int, recyds = int,
                              sacks: int, interceptions: int, week: int):
        session = DbSessionFactory.create_session()

        season_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season

        response = requests.get('https://api.mysportsfeeds.com/v1.1/pull/nfl/' + str(season) +
                                '-regular/cumulative_player_stats.json?playerstats=Yds,Sacks,Int',
                                auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

        player_json = response.json()
        player_data = player_json["cumulativeplayerstats"]["playerstatsentry"]

        for players in player_data:
            try:
                player_id = players["player"]["ID"]
                passyds = players["stats"]["PassYds"]["#text"]
                rushyds = players["stats"]["RushYds"]["#text"]
                recyds = players["stats"]["RecYds"]["#text"]
                sacks = players["stats"]["Sacks"]["#text"]
                interceptions = players["stats"]["Interceptions"]["#text"]
            except KeyError:
                continue

        # TODO: Will need KeyError check

            # TODO Need week number

            weekly_player_stats = WeeklyStats(player_id=player_id, season=season, player_id, passyds=passyds,
                                              rushyds=rushyds, recyds=recyds, sacks=sacks,
                                              interceptions=interceptions)

            session.add(weekly_player_stats)

            session.commit()

    # Get the weekly rank for each team in each division sorted by division
    # TODO: Need to include a date / week field when storing in the database
    @staticmethod
    def get_team_rankings:
        session = DbSessionFactory.create_session()

        season_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season

        response = requests.get('https://api.mysportsfeeds.com/v1.1/pull/nfl/' + str(season) +
                                '-regular/division_team_standings.json?teamstats=W,L,T',
                                auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

    # TODO: Get conference standings for wildcard and PF
    @staticmethod
    def get_conference_standings():
        session = DbSessionFactory.create_session()

        season_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season

        response = requests.get('https://api.mysportsfeeds.com/v1.1/pull/nfl/' + str(season) +
                                '-regular/conference_team_standings.json?teamstats=W,L,T',
                                auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

    # TODO: Get tiebreaker information
    @staticmethod
    def get_tiebreaker:
        session = DbSessionFactory.create_session()

        season_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season

        response = requests.get('https://api.mysportsfeeds.com/v1.1/pull/nfl/' + str(season) +
                                '-regular/overall_team_standings.json?teamstats=TD',
                                auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))



