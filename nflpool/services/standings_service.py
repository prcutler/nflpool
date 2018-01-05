from nflpool.data.dbsession import DbSessionFactory
from sqlalchemy.orm import joinedload
from nflpool.data.player_picks import PlayerPicks
from nflpool.data.weekly_player_results import WeeklyPlayerResults
from _datetime import datetime
from nflpool.data.seasoninfo import SeasonInfo


def get_seasons():
    session = DbSessionFactory.create_session()
    season_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
    current_season = season_row.current_season

    return current_season


def get_week():
    session = DbSessionFactory.create_session()

    season_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
    season_start = season_row.season_start_date
    season_start = datetime.strptime(season_start, "%Y-%m-%d")

    diff = datetime.now() - season_start
    print(diff.days)
    week = int((diff.days / 7) + 1)
    print(week)

#    week = 17           # ------------------------------- TESTING ------------------- remove this line after test.
    return week


class StandingsService:
    def display_player_standings(player_id, season=None):
        if season is None:
            season = get_seasons()

        sqlstr = "SELECT coalesce(w.points_earned,0) as points, a.first_name, a.last_name, w.pick_id, p.pick_type, p.rank, p.multiplier, t.name, "
        sqlstr += "c.conference, d.division, ap.firstname, ap.lastname "
        sqlstr += "FROM PlayerPicks p, Account a "
        sqlstr += "LEFT JOIN WeeklyPlayerResults w on p.pick_id = w.pick_id "
        sqlstr += "AND w.week = (SELECT MAX(week) from WeeklyPlayerResults  WHERE season=" + str(season) + ") "
        sqlstr += "LEFT JOIN  DivisionInfo d on p.division_id=d.division_id "
        sqlstr += "LEFT JOIN ConferenceInfo c ON p.conf_id= c.conf_id "
        sqlstr += "LEFT JOIN TeamInfo t ON p.team_id = t.team_id "
        sqlstr += "LEFT JOIN ActiveNFLPlayers ap ON p.player_id = ap.player_id AND p.season = ap.season "
        sqlstr += "WHERE "
        sqlstr += "p.user_id = a.id "
        sqlstr += "AND p.season = " + str(season) + " "
        sqlstr += "AND p.user_id = '" + player_id +"'"

        session = DbSessionFactory.create_session()
        standings = session.execute(sqlstr)

        dict_standings = [dict(row) for row in standings]

        session.close()
        return dict_standings

    def display_weekly_standings(season=None):

        # return list that contains player standings for most recent week in results table
        if season is None:
            season = get_seasons()

        sqlstr = "SELECT SUM(w.points_earned) as total_points, a.first_name, a.last_name, a.id from WeeklyPlayerResults w, PlayerPicks p, Account a "
        sqlstr += "WHERE w.pick_id = p.pick_id AND p.user_id = a.id "
        sqlstr += "AND w.season = " + str(season) + " "
        sqlstr += "AND w.week = (SELECT MAX(week) from WeeklyPlayerResults WHERE season = " + str(season) + ") "
        sqlstr += "GROUP BY p.user_id "
        sqlstr += "ORDER BY total_points DESC"

        session = DbSessionFactory.create_session()
        standings = session.execute(sqlstr)

        dict_standings = [dict(row) for row in standings]

        session.close()
        return dict_standings

    def update_player_pick_points():
        season = get_seasons()
        week = get_week()

        session = DbSessionFactory.create_session()

        # starting values
        conf = 0
        i = 4

        while (conf < 2):
            # start with pick type 4 and continue through 8

            if i == 4:
                cattype = "passyds"
            elif i == 5:
                cattype ="rushyds"
            elif i == 6:
                cattype ="recyds"
            elif i == 7:
                cattype ="sacks"
            elif i == 8:
                cattype = "interceptions"


            sqlstr = "INSERT INTO WeeklyPlayerResults (pick_id, season, week, points_earned) "
            sqlstr += "SELECT t1.pick_id as pick_id, t1.season as season, t1.week as week, pts.points*t1.multiplier as points_earned "
            sqlstr += "FROM "
            sqlstr += "(SELECT p.pick_id, p.user_id, p.multiplier, p.player_id, "
            sqlstr += "(SELECT count(*) from WeeklyNFLPlayerStats as w2, ActiveNFLPlayers as ap, "
            sqlstr += "TeamInfo as t "
            sqlstr += "WHERE "
            sqlstr += "w2.player_id = ap.player_id "
            sqlstr += "AND ap.team_id = t.team_id "
            sqlstr += "AND t.conference_id = " + str(conf) + " "
            sqlstr += "AND W2." + cattype + ">w." + cattype + ")+1 as rank, "
            sqlstr += "w.week, "
            sqlstr += "w.season "
            sqlstr += "FROM WeeklyNFLPlayerStats w, PlayerPicks p "
            sqlstr += "WHERE w.player_id = p.player_id "
            sqlstr += "AND  w.season = " + str(season) + " "
            sqlstr += "AND w.week = " + str(week) + " "
            sqlstr += "AND p.pick_type = " + str(i) + " "
            sqlstr += "AND p.conf_id = " + str(conf) + " "
            sqlstr += "AND w." + cattype + " not null "
            sqlstr += "ORDER BY rank) as t1, PickTypePoints pts "
            sqlstr += "WHERE "
            sqlstr += "pts.pick_type_id = " + str(i) + " "
            sqlstr += "AND t1.rank = pts.place"

            session.execute(sqlstr)
            session.commit()

            # increment counters
            if i == 8:
                conf += 1
                i=0

            i += 1

        session.close()

    def update_team_pick_points():
        session = DbSessionFactory.create_session()

        season = get_seasons()
        week = get_week()

        # this does all type 1 points
        sqlstr = "INSERT INTO WeeklyPlayerResults(pick_id, season, week, points_earned) "
        sqlstr += "SELECT pp.pick_id, w.season, w.week, p.points * pp.multiplier as points_earned "
        sqlstr += "FROM PlayerPicks pp "
        sqlstr += "LEFT JOIN WeeklyTeamStats w on pp.rank=w.division_rank and pp.team_id=w.team_id "
        sqlstr += "LEFT JOIN TeamInfo t on pp.team_id= t.team_id "
        sqlstr += "LEFT JOIN PickTypePoints p on pp.pick_type = p.pick_type_id "
        sqlstr += "WHERE pp.pick_type = 1 "
        sqlstr += "AND w.season = " + str(season) + " "
        sqlstr += "AND w.week = " + str(week) + " "
        sqlstr += "AND pp.conf_id = t.conference_id "
        sqlstr += "AND pp.division_id = t.division_id "
        sqlstr += "AND p.place = w.division_rank "
        sqlstr += "ORDER BY pp.user_id"

        session.execute(sqlstr)
        session.commit()

        # type 3 points:
        conf = 0
        while conf<2:
            sqlstr = "INSERT INTO WeeklyPlayerResults(pick_id, season, week, points_earned) "
            sqlstr += "SELECT t1.pick_id as pick_id, t1.season as season, t1.week as week, pts.points * t1.multiplier as points_earned "
            sqlstr += "FROM (SELECT p.pick_id, p.user_id, p.multiplier, p.team_id, "
            sqlstr += "(SELECT count(*) FROM WeeklyTeamStats as w2, TeamInfo as t "
            sqlstr += "WHERE w2.team_id = t.team_id "
            sqlstr += "AND t.conference_id = " + str(conf) + " "
            sqlstr += "AND W2.points_for > w.points_for)+1 as rank, "
            sqlstr += "w.week, w.season "
            sqlstr += "FROM WeeklyTeamStats w, PlayerPicks p "
            sqlstr += "WHERE w.team_id = p.team_id "
            sqlstr += "AND w.season = " + str(season) + " "
            sqlstr += "AND w.week = " + str(week) + " "
            sqlstr += "AND p.pick_type = 3 "
            sqlstr += "AND p.conf_id = " + str(conf) + " "
            sqlstr += "AND w.points_for not null "
            sqlstr += "ORDER BY rank) as t1, PickTypePoints pts "
            sqlstr += "WHERE "
            sqlstr += "pts.pick_type_id = 3 "
            sqlstr += "AND t1.rank = pts.place"

            session.execute(sqlstr)
            session.commit()
            conf +=1

        # type 9 points - wildcard
        sqlstr = "INSERT INTO WeeklyPlayerResults (pick_id, season, week, points_earned) "
        sqlstr += "SELECT p.pick_id, w.season, w.week, pts.points*p.multiplier as points_earned from PlayerPicks p, WeeklyTeamStats w, PickTypePoints pts "
        sqlstr += "WHERE p.pick_type = 9 "
        sqlstr += "AND p.pick_type = pts.pick_type_id "
        sqlstr += "AND w.conference_rank in (5,6) "
        sqlstr += "AND w.team_id = p.team_id "
        sqlstr += "AND w.season = " + str(season) + " "
        sqlstr += "AND w.week = " + str(week)

        session.execute(sqlstr)
        session.commit()

        session.close()

