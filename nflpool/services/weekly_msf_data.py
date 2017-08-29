from nflpool.data.dbsession import DbSessionFactory
import requests
from nflpool.data.weekly_nflplayer_stats import WeeklyNFLPlayerStats
import nflpool.data.secret as secret
from requests.auth import HTTPBasicAuth
from nflpool.data.seasoninfo import SeasonInfo
from nflpool.data.weekly_team_stats import WeeklyTeamStats
import datetime


class WeeklyStatsService:
    # Open a connection to the database to get the current season year from the SeasonInfo table
    # Get weekly stats for each player for yards (passing, receiving, rushing), sacks and interceptions
    # TODO: Need to include a date / week field when storing in the database
    @staticmethod
    def get_qb_stats():

        session = DbSessionFactory.create_session()

        season_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season
        season_start = session.query(SeasonInfo).filter(SeasonInfo.season_start_date == '1').first()

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
                passyds = players["stats"]["PassYards"]["#text"]

            except KeyError:
                continue

            # TODO Need week number

            if season == 2016:
                week = 17
            else:
                today = datetime.date.today()
                days = abs(today - season_start)
                week = int((days / 7) + 1)

            weekly_player_stats = WeeklyNFLPlayerStats(player_id=player_id, season=season,
                                                       passyds=passyds, week=week)

            session.add(weekly_player_stats)

            session.commit()

    @staticmethod
    def get_rb_stats():

        session = DbSessionFactory.create_session()

        season_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season
        season_start = session.query(SeasonInfo).filter(SeasonInfo.season_start_date == '1').first()

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
                rushyds = players["stats"]["RushYards"]["#text"]

            except KeyError:
                continue

            # TODO Need week number

            if season == 2016:
                week = 17
            else:
                today = datetime.date.today()
                days = abs(today - season_start)
                week = int((days / 7) + 1)

            weekly_player_stats = WeeklyNFLPlayerStats(player_id=player_id, season=season,
                                                           rushyds=rushyds, week=week)

            session.add(weekly_player_stats)

            session.commit()

    @staticmethod
    def get_rec_stats():

        session = DbSessionFactory.create_session()

        season_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season
        season_start = session.query(SeasonInfo).filter(SeasonInfo.season_start_date == '1').first()

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
                recyds = players["stats"]["RecYards"]["#text"]

            except KeyError:
                continue

            # TODO Need week number

            if season == 2016:
                week = 17
            else:
                today = datetime.date.today()
                days = abs(today - season_start)
                week = int((days / 7) + 1)

            weekly_team_stats = WeeklyNFLPlayerStats(player_id=player_id, season=season,
                                                           recyds=recyds, week=week)

            session.add(weekly_team_stats)

            session.commit()

    @staticmethod
    def get_sack_stats():

        session = DbSessionFactory.create_session()

        season_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season
        season_start = session.query(SeasonInfo).filter(SeasonInfo.season_start_date == '1').first()

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
                week = 17
            else:
                today = datetime.date.today()
                days = abs(today - season_start)
                week = int((days / 7) + 1)

            weekly_player_stats = WeeklyNFLPlayerStats(player_id=player_id, season=season,
                                                           sacks=sacks, week=week)

            session.add(weekly_player_stats)

            session.commit()

    @staticmethod
    def get_interception_stats():

        session = DbSessionFactory.create_session()

        season_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season
        season_start = session.query(SeasonInfo).filter(SeasonInfo.season_start_date == '1').first()

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
                week = 17
            else:
                today = datetime.date.today()
                days = abs(today - season_start)
                week = int((days / 7) + 1)

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
        season_start = session.query(SeasonInfo).filter(SeasonInfo.season_start_date == '1').first()

        if season == 2016:
            response = requests.get('https://api.mysportsfeeds.com/v1.1/pull/nfl/2016-2017'
                                    '-regular/division_team_standings.json?teamstats=W,L,T',
                                    auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))
        else:
            response = requests.get('https://api.mysportsfeeds.com/v1.1/pull/nfl/' + str(season) +
                                    '-regular/division_team_standings.json?teamstats=W,L,T',
                                    auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

        team_json = response.json()
        team_data = team_json["divisionteamstandings"]["division"]

        x = 0
        y = 0
        z = 0
        a = 0

        while x < len(team_data):
            rank = (team_data[x]["teamentry"][1]["rank"])
            team_id = (team_data[x]["teamentry"][1]["team"]["ID"])

            x += 1

            # TODO Need week number

            if season == 2016:
                week = 17
            else:
                today = datetime.date.today()
                days = abs(today - season_start)
                week = int((days / 7) + 1)

            weekly_team_stats = WeeklyTeamStats(team_id=team_id, season=season,
                                                division_rank=rank, week=week)

            session.add(weekly_team_stats)
            session.commit()

        while y < len(team_data):
            rank = (team_data[y]["teamentry"][0]["rank"])
            team_id = (team_data[y]["teamentry"][0]["team"]["ID"])

            y += 1

            # TODO Need week number

            if season == 2016:
                week = 17
            else:
                today = datetime.date.today()
                days = abs(today - season_start)
                week = int((days / 7) + 1)

            weekly_team_stats = WeeklyTeamStats(team_id=team_id, season=season,
                                                division_rank=rank, week=week)

            session.add(weekly_team_stats)
            session.commit()

        while z < len(team_data):
            rank = (team_data[z]["teamentry"][2]["rank"])
            team_id = (team_data[z]["teamentry"][2]["team"]["ID"])

#            print(team_id, ":", rank)
            z += 1

            # TODO Need week number

            if season == 2016:
                week = 17
            else:
                today = datetime.date.today()
                days = abs(today - season_start)
                week = int((days / 7) + 1)

            weekly_team_stats = WeeklyTeamStats(team_id=team_id, season=season,
                                                division_rank=rank, week=week)

            session.add(weekly_team_stats)
            session.commit()

        while a < len(team_data):
            rank = (team_data[a]["teamentry"][3]["rank"])
            team_id = (team_data[a]["teamentry"][3]["team"]["ID"])

#            print(team_id, ":", rank)
            a += 1

            # TODO Need week number

            if season == 2016:
                week = 17
            else:
                today = datetime.date.today()
                days = abs(today - season_start)
                week = int((days / 7) + 1)

            weekly_team_stats = WeeklyTeamStats(team_id=team_id, season=season,
                                                division_rank=rank, week=week)

            session.add(weekly_team_stats)
            session.commit()

    # TODO: This needs to become an update statement, not an insert as it's duplicating rows

    @staticmethod
    def get_conference_standings():
        session = DbSessionFactory.create_session()

        season_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season

        if season == 2016:
            response = requests.get('https://api.mysportsfeeds.com/v1.1/pull/nfl/2016-2017'
                                    '-regular/conference_team_standings.json?teamstats=W,L,T,PF',
                                    auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))
        else:
            response = requests.get('https://api.mysportsfeeds.com/v1.1/pull/nfl/' + str(season) +
                                    '-regular/conference_team_standings.json?teamstats=W,L,T,PF',
                                    auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

        x = 0
        y = 0

        data = response.json()
        teamlist = data["conferenceteamstandings"]["conference"][0]["teamentry"]

        for afc_teams in teamlist:
            team_id = int(data["conferenceteamstandings"]["conference"][0]["teamentry"][x]["team"]["ID"])
            conference_rank = data["conferenceteamstandings"]["conference"][0]["teamentry"][x]["rank"]
            points_for = data["conferenceteamstandings"]["conference"][0]["teamentry"][x]["stats"]["PointsFor"][
                "#text"]

            x += 1

            session.query(WeeklyTeamStats).filter(WeeklyTeamStats.team_id == team_id). \
                update({"conference_rank": conference_rank})
            session.query(WeeklyTeamStats).filter(WeeklyTeamStats.team_id == team_id). \
                update({"points_for": points_for})

            session.commit()

        for nfc_team_list in teamlist:
            team_id = int(data["conferenceteamstandings"]["conference"][1]["teamentry"][y]["team"]["ID"])
            conference_rank = data["conferenceteamstandings"]["conference"][1]["teamentry"][y]["rank"]
            points_for = data["conferenceteamstandings"]["conference"][1]["teamentry"][y]["stats"]["PointsFor"][
                "#text"]

            y += 1

            session.query(WeeklyTeamStats).filter(WeeklyTeamStats.team_id == team_id). \
                update({"conference_rank": conference_rank})
            session.query(WeeklyTeamStats).filter(WeeklyTeamStats.team_id == team_id). \
                update({"points_for": points_for})

            session.commit()

    # TODO: This needs to become an update statement, not an insert as it's duplicating rows

    @staticmethod
    def get_tiebreaker():
        session = DbSessionFactory.create_session()

        season_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season

        if season == 2016:
            response = requests.get('https://api.mysportsfeeds.com/v1.1/pull/nfl/2016-2017'
                                    '-regular/overall_team_standings.json?teamstats=TD',
                                    auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))
        else:
            response = requests.get('https://api.mysportsfeeds.com/v1.1/pull/nfl/' + str(season) +
                                    '-regular/overall_team_standings.json?teamstats=TD',
                                    auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

        team_json = response.json()
        team_data = team_json["overallteamstandings"]["teamstandingsentry"]

        for teams in team_data:
            team_id = teams["team"]["ID"]
            kr_td = teams["stats"]["KrTD"]["#text"]
            pr_td = teams["stats"]["PrTD"]["#text"]

            tiebreaker_td = (int(kr_td)+int(pr_td))

            session.query(WeeklyTeamStats).filter(WeeklyTeamStats.team_id == team_id).\
                update({"tiebreaker_td": tiebreaker_td})
            session.query(WeeklyTeamStats).filter(WeeklyTeamStats.team_id == team_id). \
                update({"tiebreaker_team": team_id})

            session.commit()



