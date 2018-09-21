from nflpool.data.dbsession import DbSessionFactory
import requests
from nflpool.data.weekly_nflplayer_stats import WeeklyNFLPlayerStats
import nflpool.data.secret as secret
from requests.auth import HTTPBasicAuth
from nflpool.data.seasoninfo import SeasonInfo
from nflpool.data.weekly_team_stats import WeeklyTeamStats
from nflpool.services.time_service import TimeService


def get_seasons():
    session = DbSessionFactory.create_session()
    season_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
    current_season = season_row.current_season

    return current_season


class WeeklyStatsService:
    # Open a connection to the database to get the current season year from the SeasonInfo table
    # Get weekly stats for each player for yards (passing, receiving, rushing), sacks and interceptions
    @staticmethod
    def get_qb_stats():

        week = TimeService.get_week()

        session = DbSessionFactory.create_session()

        season_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season

        response = requests.get('https://api.mysportsfeeds.com/v2.0/pull/nfl/' + str(season) +
                                '-regular/player_stats_totals.json?position=QB&stats=Yds',
                                auth=HTTPBasicAuth(secret.msf_api, secret.msf_v2pw))

        player_json = response.json()
        player_data = player_json["playerStatsTotals"]

        for players in player_data:
            try:
                player_id = players["player"]["id"]
                passyds = players["stats"]["passing"]["passYards"]

            except KeyError:
                continue

            weekly_player_stats = WeeklyNFLPlayerStats(player_id=player_id, season=season,
                                                       passyds=passyds, week=week)

            session.add(weekly_player_stats)

            session.commit()

    @staticmethod
    def get_rb_stats():

        session = DbSessionFactory.create_session()

        season_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season

        response = requests.get('https://api.mysportsfeeds.com/v2.0/pull/nfl/' + str(season) +
                                '-regular/player_stats_totals.json?position=RB&stats=Yds',
                                auth=HTTPBasicAuth(secret.msf_api, secret.msf_v2pw))

        player_json = response.json()
        player_data = player_json["playerStatsTotals"]

        for players in player_data:
            try:
                player_id = players["player"]["id"]
                rushyds = players["stats"]["rushing"]["rushYards"]

            except KeyError:
                continue

            week = TimeService.get_week()

            weekly_player_stats = WeeklyNFLPlayerStats(player_id=player_id, season=season,
                                                       rushyds=rushyds, week=week)

            session.add(weekly_player_stats)

            session.commit()

    @staticmethod
    def get_rec_stats():

        session = DbSessionFactory.create_session()

        season_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season

        response = requests.get('https://api.mysportsfeeds.com/v2.0/pull/nfl/' + str(season) +
                                '-regular/player_stats_totals.json?position=WR,TE&stats=Yds',
                                auth=HTTPBasicAuth(secret.msf_api, secret.msf_v2pw))

        player_json = response.json()
        player_data = player_json["playerStatsTotals"]

        for players in player_data:
            try:
                player_id = players["player"]["id"]
                recyds = players["stats"]["receiving"]["recYards"]

            except KeyError:
                continue

            week = TimeService.get_week()

            weekly_team_stats = WeeklyNFLPlayerStats(player_id=player_id, season=season,
                                                     recyds=recyds, week=week)

            session.add(weekly_team_stats)

            session.commit()

    @staticmethod
    def get_sack_stats():

        session = DbSessionFactory.create_session()

        season_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season

        response = requests.get('https://api.mysportsfeeds.com/v2.0/pull/nfl/' + str(season) +
                                '-regular/player_stats_totals.json?position=DE,DT,ILB,LB,MLB,NT,OLB&stats=Sacks',
                                auth=HTTPBasicAuth(secret.msf_api, secret.msf_v2pw))

        player_json = response.json()
        player_data = player_json["playerStatsTotals"]

        for players in player_data:
            try:
                player_id = players["player"]["id"]
                sacks = players["stats"]["sacks"]["sacks"]

            except KeyError:
                continue

            week = TimeService.get_week()

            weekly_player_stats = WeeklyNFLPlayerStats(player_id=player_id, season=season,
                                                       sacks=sacks, week=week)

            session.add(weekly_player_stats)

            session.commit()

    @staticmethod
    def get_interception_stats():

        session = DbSessionFactory.create_session()

        season_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season

        response = requests.get('https://api.mysportsfeeds.com/v2.0/pull/nfl/' + str(season) +
                                '-regular/player_stats_totals.json?position=LB,SS,DT,DE,CB,FS,SS,ILB,MLB,OLB&'
                                'stats=Int',
                                auth=HTTPBasicAuth(secret.msf_api, secret.msf_v2pw))

        player_json = response.json()
        player_data = player_json["playerStatsTotals"]

        for players in player_data:
            try:
                player_id = players["player"]["id"]
                interceptions = players["stats"]["interceptions"]["interceptions"]

            except KeyError:
                continue

            week = TimeService.get_week()

            weekly_player_stats = WeeklyNFLPlayerStats(player_id=player_id, season=season,
                                                       interceptions=interceptions, week=week)

            session.add(weekly_player_stats)

            session.commit()

    @staticmethod
    def get_rankings():

        session = DbSessionFactory.create_session()

        season_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season

        response = requests.get('https://api.mysportsfeeds.com/v2.0/pull/nfl/' + str(season) +
                                '-regular/standings.json', auth=HTTPBasicAuth(secret.msf_api, secret.msf_v2pw))

        standings_json = response.json()
        standings_data = standings_json["teams"]

        x = 0

        # print(type(standings_data), standings_data)

        for teams in standings_data:
            team_id = standings_data[x]["team"]["id"]
            division_rank = standings_data[x]["divisionRank"]["rank"]
            playoff_rank = standings_data[x]["playoffRank"]["rank"]

            week = TimeService.get_week()

            weekly_team_stats = WeeklyTeamStats(team_id=team_id, season=season, division_rank=division_rank,
                                                conference_rank=playoff_rank, week=week)

            x += 1

            session.add(weekly_team_stats)
            session.commit()

    @staticmethod
    def get_points_for():
        session = DbSessionFactory.create_session()

        season_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season

        response = requests.get('https://api.mysportsfeeds.com/v2.0/pull/nfl/' + str(season) +
                                '-regular/team_stats_totals.json?stats=pointsFor',
                                auth=HTTPBasicAuth(secret.msf_api, secret.msf_v2pw))

        points_for_json = response.json()
        points_for_data = points_for_json["teamStatsTotals"]

        x = 0

        for teams in points_for_data:
            team_id = int(points_for_data[x]["team"]["id"])
            points_for = points_for_data[x]["stats"]["standings"]["pointsFor"]

            week = TimeService.get_week()

            x += 1

            session.query(WeeklyTeamStats).filter(WeeklyTeamStats.team_id == team_id)\
                .filter(WeeklyTeamStats.season == season).filter(WeeklyTeamStats.week == week) \
                .update({"points_for": points_for})

            session.commit()

    @staticmethod
    def get_tiebreaker():
        session = DbSessionFactory.create_session()

        season_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season

        response = requests.get('https://api.mysportsfeeds.com/v2.0/pull/nfl/' + str(season) +
                                '-regular/team_stats_totals.json?stats=TD',
                                auth=HTTPBasicAuth(secret.msf_api, secret.msf_v2pw))

        x = 0

        tiebreaker_json = response.json()
        tiebreaker_data = tiebreaker_json["teamStatsTotals"]

        for teams in tiebreaker_data:
            team_id = tiebreaker_data[x]["team"]["id"]
            kr_td = tiebreaker_data[x]["stats"]["kickoffReturns"]["krTD"]
            pr_td = tiebreaker_data[x]["stats"]["puntReturns"]["prTD"]

            tiebreaker_td = (int(kr_td)+int(pr_td))

            week = TimeService.get_week()

            x += 1

            session.query(WeeklyTeamStats).filter(WeeklyTeamStats.team_id == team_id)\
                .filter(WeeklyTeamStats.season == season).filter(week == week) \
                .update({"tiebreaker_td": tiebreaker_td})
            session.query(WeeklyTeamStats).filter(WeeklyTeamStats.team_id == team_id) \
                    .filter(WeeklyTeamStats.season == season).filter(week == week) \
                .update({"tiebreaker_team": team_id})

            session.commit()



