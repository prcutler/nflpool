from nflpool.data.dbsession import DbSessionFactory
import requests
from nflpool.data.weekly_nflplayer_stats import WeeklyNFLPlayerStats
import nflpool.data.secret as secret
from requests.auth import HTTPBasicAuth
from nflpool.data.seasoninfo import SeasonInfo


class WeeklyStatsService:
    # Open a connection to the database to get the current season year from the SeasonInfo table
    # Get weekly stats for each player for yards (passing, receiving, rushing), sacks and interceptions
    # TODO: Need to include a date / week field when storing in the database
    @staticmethod
    def get_qb_stats():

        session = DbSessionFactory.create_session()

        season_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season

        '''Adjust response for MSF 1.0 API for 2016 or older or use MSF API 1.1 if 2017 or newer'''
        if season == 2016:
            response = requests.get('https://api.mysportsfeeds.com/v1.1/pull/nfl/2016-2017-'
                                    'regular/cumulative_player_stats.json?position=QB&playerstats=Yds',
                                    auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))
        else:
            response = requests.get('https://api.mysportsfeeds.com/v1.1/pull/nfl/' + str(season) +
                                    '-regular/cumulative_player_stats.json?position=QB&playerstats=Yds',
                                    auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

        player_json = response.json()
        player_data = player_json["cumulativeplayerstats"]["playerstatsentry"]

        for players in player_data:
            try:
                player_id = players["player"]["ID"]
                passyds = players["stats"]["PassYds"]["#text"]

            except KeyError:
                continue

            # TODO Need week number

            if season == 2016:
                weekly_player_stats = WeeklyNFLPlayerStats(player_id=player_id, season=season,
                                                           passyds=passyds, week=17)
            else:
                weekly_player_stats = WeeklyNFLPlayerStats(player_id=player_id, season=season,
                                                           passyds=passyds, week=week)

            session.add(weekly_player_stats)

            session.commit()

    @staticmethod
    def get_rb_stats():

        session = DbSessionFactory.create_session()

        season_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season

        '''Adjust response for MSF 1.0 API for 2016 or older or use MSF API 1.1 if 2017 or newer'''
        if season == 2016:
            response = requests.get('https://api.mysportsfeeds.com/v1.1/pull/nfl/2016-2017-'
                                    'regular/cumulative_player_stats.json?position=RB&playerstats=Yds',
                                    auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))
        else:
            response = requests.get('https://api.mysportsfeeds.com/v1.1/pull/nfl/' + str(season) +
                                    '-regular/cumulative_player_stats.json?position=RB&playerstats=Yds',
                                    auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

        player_json = response.json()
        player_data = player_json["cumulativeplayerstats"]["playerstatsentry"]

        for players in player_data:
            try:
                player_id = players["player"]["ID"]
                rushyds = players["stats"]["RushYds"]["#text"]

            except KeyError:
                continue

            # TODO Need week number

            if season == 2016:
                weekly_player_stats = WeeklyNFLPlayerStats(player_id=player_id, season=season,
                                                           rushyds=rushyds, week=17)
            else:
                weekly_player_stats = WeeklyNFLPlayerStats(player_id=player_id, season=season,
                                                           rushyds=rushyds, week=week)

            session.add(weekly_player_stats)

            session.commit()

    @staticmethod
    def get_rec_stats():

        session = DbSessionFactory.create_session()

        season_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season

        '''Adjust response for MSF 1.0 API for 2016 or older or use MSF API 1.1 if 2017 or newer'''
        if season == 2016:
            response = requests.get('https://api.mysportsfeeds.com/v1.1/pull/nfl/2016-2017-'
                                    'regular/cumulative_player_stats.json?position=WR,TE&playerstats=Yds',
                                    auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))
        else:
            response = requests.get('https://api.mysportsfeeds.com/v1.1/pull/nfl/' + str(season) +
                                    '-regular/cumulative_player_stats.json?position=WR,TE&playerstats=Yds',
                                    auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

        player_json = response.json()
        player_data = player_json["cumulativeplayerstats"]["playerstatsentry"]

        for players in player_data:
            try:
                player_id = players["player"]["ID"]
                recyds = players["stats"]["RecYds"]["#text"]

            except KeyError:
                continue

            # TODO Need week number

            if season == 2016:
                weekly_player_stats = WeeklyNFLPlayerStats(player_id=player_id, season=season,
                                                           recyds=recyds, week=17)
            else:
                weekly_player_stats = WeeklyNFLPlayerStats(player_id=player_id, season=season,
                                                           recyds=recyds, week=week)

            session.add(weekly_player_stats)

            session.commit()

    @staticmethod
    def get_sack_stats():

        session = DbSessionFactory.create_session()

        season_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season

        '''Adjust response for MSF 1.0 API for 2016 or older or use MSF API 1.1 if 2017 or newer'''
        if season == 2016:
            response = requests.get('https://api.mysportsfeeds.com/v1.1/pull/nfl/2016-2017-'
                                    'regular/cumulative_player_stats.json?'
                                    'position=DE,DT,ILB,LB,MLB,NT,OLB&playerstats=Sacks',
                                    auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))
        else:
            response = requests.get('https://api.mysportsfeeds.com/v1.1/pull/nfl/' + str(season) +
                                    '-regular/cumulative_player_stats.json?'
                                    'position=DE,DT,ILB,LB,MLB,NT,OLB&playerstats=Sacks',
                                    auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

        player_json = response.json()
        player_data = player_json["cumulativeplayerstats"]["playerstatsentry"]

        for players in player_data:
            try:
                player_id = players["player"]["ID"]
                sacks = players["stats"]["Sacks"]["#text"]

            except KeyError:
                continue

            # TODO Need week number

            if season == 2016:
                weekly_player_stats = WeeklyNFLPlayerStats(player_id=player_id, season=season,
                                                           sacks=sacks, week=17)
            else:
                weekly_player_stats = WeeklyNFLPlayerStats(player_id=player_id, season=season,
                                                           sacks=sacks, week=week)

            session.add(weekly_player_stats)

            session.commit()

    @staticmethod
    def get_interception_stats():

        session = DbSessionFactory.create_session()

        season_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season

        '''Adjust response for MSF 1.0 API for 2016 or older or use MSF API 1.1 if 2017 or newer'''
        if season == 2016:
            response = requests.get('https://api.mysportsfeeds.com/v1.1/pull/nfl/2016-2017-'
                                    'regular/cumulative_player_stats.json?'
                                    'position=LB,SS,DT,DE,CB,FS,SS&playerstats=Int',
                                    auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))
        else:
            response = requests.get('https://api.mysportsfeeds.com/v1.1/pull/nfl/' + str(season) +
                                    '-regular/cumulative_player_stats.json?'
                                    'position=LB,SS,DT,DE,CB,FS,SS&playerstats=Int',
                                    auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

        player_json = response.json()
        player_data = player_json["cumulativeplayerstats"]["playerstatsentry"]

        for players in player_data:
            try:
                player_id = players["player"]["ID"]
                interceptions = players["stats"]["Interceptions"]["#text"]

            except KeyError:
                continue

            # TODO Need week number

            if season == 2016:
                weekly_player_stats = WeeklyNFLPlayerStats(player_id=player_id, season=season,
                                                           interceptions=interceptions, week=17)
            else:
                weekly_player_stats = WeeklyNFLPlayerStats(player_id=player_id, season=season,
                                                           interceptions=interceptions, week=week)

            session.add(weekly_player_stats)

            session.commit()

    # Get the weekly rank for each team in each division sorted by division
    # TODO: Need to include a date / week field when storing in the database
    @staticmethod
    def get_team_rankings():
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
    def get_tiebreaker():
        session = DbSessionFactory.create_session()

        season_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season

        response = requests.get('https://api.mysportsfeeds.com/v1.1/pull/nfl/' + str(season) +
                                '-regular/overall_team_standings.json?teamstats=TD',
                                auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))



