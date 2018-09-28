from nflpool.data.dbsession import DbSessionFactory
from nflpool.data.divisioninfo import DivisionInfo
from nflpool.data.conferenceinfo import ConferenceInfo
from nflpool.data.picktypes import PickTypes
from nflpool.data.weekly_nflplayer_stats import WeeklyNFLPlayerStats
from nflpool.data.activeplayers import ActiveNFLPlayers
from nflpool.data.teaminfo import TeamInfo
from itertools import groupby


def interception_leaders():
    session = DbSessionFactory.create_session()

    afc_interception_query = (
        session.query(
            WeeklyNFLPlayerStats.interceptions, WeeklyNFLPlayerStats.player_id
        )
        .join(ActiveNFLPlayers)
        .outerjoin(TeamInfo, ActiveNFLPlayers.team_id == TeamInfo.team_id)
        .filter(TeamInfo.conference_id == 0)
        .filter(WeeklyNFLPlayerStats.interceptions)
        .limit(20)
        .all()
    )

    print(afc_interception_query)

    afc_interception_list = [
        list(afc_interception_query)
        for afc_interception_query in afc_interception_query
    ]
    print(afc_interception_list)

    afc_sorted_interceptions = sorted(afc_interception_list, reverse=True)
    rank = 0
    for _, grp in groupby(afc_sorted_interceptions, key=lambda xs: xs[0]):
        r = rank + 1
        for x in grp:
            x.append(r)
            rank += 1

    print(afc_sorted_interceptions)
