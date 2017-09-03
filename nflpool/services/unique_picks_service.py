from nflpool.data.dbsession import DbSessionFactory
from nflpool.data.divisioninfo import DivisionInfo
from nflpool.data.conferenceinfo import ConferenceInfo
from nflpool.data.picktypes import PickTypes
from nflpool.data.teaminfo import TeamInfo
from nflpool.data.player_picks import PlayerPicks
from nflpool.data.seasoninfo import SeasonInfo



class UniquePicksService:

    @staticmethod
    def unique_picks():
        session = DbSessionFactory.create_session()

        season_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
        current_season = season_row.current_season

        con = DbSessionFactory.create_session()
        txtstr = "UPDATE PlayerPicks SET multiplier=2 WHERE team_id  IN (SELECT team_id \
                  FROM (select DISTINCT(team_id) , COUNT(team_id) AS ct FROM PlayerPicks WHERE pick_type=1 \
                  AND conf_id = 0 AND division_id = 1 AND rank = 4 AND season = {} GROUP BY team_id) WHERE ct=1 \
                  AND pick_type=1 AND conf_id = 0 AND division_id = 1 AND rank = 4 \
                  and season= {})".format(current_season, current_season)

        con.execute(txtstr)
        con.commit()



