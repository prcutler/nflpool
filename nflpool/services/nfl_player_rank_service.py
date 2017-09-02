from nflpool.data.teaminfo import TeamInfo
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

    afc_interception_query = session.query(WeeklyNFLPlayerStats.interceptions, WeeklyNFLPlayerStats.player_id).\
        join(ActiveNFLPlayers).\
        outerjoin(TeamInfo, ActiveNFLPlayers.team_id == TeamInfo.team_id).\
        filter(TeamInfo.conference_id == 0).\
        filter(WeeklyNFLPlayerStats.interceptions.desc()).limit(20).all()

    # This query pulls all interception leaders for both the AFC and not NFC - not what I need
#    interception_query = session.query(WeeklyNFLPlayerStats.interceptions, WeeklyNFLPlayerStats.player_id). \
#        order_by(WeeklyNFLPlayerStats.interceptions.desc()).limit(20).all()

#    int_list = session.query(ActiveNFLPlayers.player_id, ActiveNFLPlayers.firstname,
#                             ActiveNFLPlayers.lastname). \
#        join(TeamInfo, ActiveNFLPlayers.team_id == TeamInfo.team_id) \
#        .filter(TeamInfo.conference_id == conf_id) \
#        .filter(ActiveNFLPlayers.position.in_([cb, db, fs, ss, mlb, lb, olb, ilb])) \
#        .filter(ActiveNFLPlayers.season == SeasonInfo.current_season) \
#        .order_by(ActiveNFLPlayers.lastname).all()

#    picks_query = session.query(PlayerPicks.pick_type, ConferenceInfo.conference, DivisionInfo.division,
#                                TeamInfo.name, PlayerPicks.rank,
#                                ActiveNFLPlayers.firstname, ActiveNFLPlayers.lastname) \
#        .outerjoin(ConferenceInfo) \
#        .outerjoin(DivisionInfo) \
#        .outerjoin(TeamInfo) \
#        .outerjoin(ActiveNFLPlayers, and_(PlayerPicks.player_id == ActiveNFLPlayers.player_id,
#                                          PlayerPicks.season == ActiveNFLPlayers.season)). \
#        filter(PlayerPicks.user_id == user_id,
#               PlayerPicks.season == season)

    print(afc_interception_query)

    afc_interception_list = [list(afc_interception_query) for afc_interception_query in afc_interception_query]
    print(afc_interception_list)

    afc_sorted_interceptions = sorted(afc_interception_list, reverse=True)
    rank = 0
    for _, grp in groupby(afc_sorted_interceptions, key=lambda xs: xs[0]):
        r = rank + 1
        for x in grp:
            x.append(r)
            rank += 1

    print(afc_sorted_interceptions)



