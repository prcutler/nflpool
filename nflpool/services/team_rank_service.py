from nflpool.data.dbsession import DbSessionFactory
from nflpool.data.divisioninfo import DivisionInfo
from nflpool.data.conferenceinfo import ConferenceInfo
from nflpool.data.picktypes import PickTypes
from nflpool.data.teaminfo import TeamInfo
from nflpool.data.player_picks import PlayerPicks


def division_winners():
    session = DbSessionFactory.create_session()

    season_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
    season = season_row.current_season

    today = datetime.date.today()
    days = abs(today - season_start)
    week = int((days / 7) + 1)

