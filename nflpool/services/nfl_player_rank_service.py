from nflpool.data.teaminfo import TeamInfo
from nflpool.data.dbsession import DbSessionFactory
from nflpool.data.divisioninfo import DivisionInfo
from nflpool.data.conferenceinfo import ConferenceInfo
from nflpool.data.picktypes import PickTypes
from nflpool.data.weekly_nflplayer_stats import WeeklyNFLPlayerStats
from itertools import groupby


def interception_leaders():
    session = DbSessionFactory.create_session()

    interception_query = session.query(WeeklyNFLPlayerStats.interceptions, WeeklyNFLPlayerStats.player_id).\
        order_by(WeeklyNFLPlayerStats.interceptions.desc()).limit(20).all()

    print(interception_query)

    interception_list = [list(interception_query) for interception_query in interception_query]
    print(interception_list)

    sorted_interceptions = sorted(interception_list, reverse=True)
    rank = 0
    for _, grp in groupby(sorted_interceptions, key=lambda xs: xs[0]):
        r = rank + 1
        for x in grp:
            x.append(r)
            rank += 1
            print(sorted_interceptions)



