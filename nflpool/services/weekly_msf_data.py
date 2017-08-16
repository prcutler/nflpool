from nflpool.data.dbsession import DbSessionFactory


class WeeklyStatsService:
    @staticmethod
    def get_weekly_stats():
        return []

    # Open a connection to the database to get the current season year from the SeasonInfo table
    @staticmethod
    def get_nflplayer_stats():
        session = DbSessionFactory.create_session()

        season_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season

        response = requests.get('https://api.mysportsfeeds.com/v1.1/pull/nfl/' + str(season) +
                                '-regular/cumulative_player_stats.json?playerstats=Att,Comp,Yds,TD',
                                auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

# TODO Look at stats to pull in Postman for .json?= above