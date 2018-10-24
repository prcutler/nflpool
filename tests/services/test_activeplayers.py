import pytest
from nflpool.data.activeplayers import ActiveNFLPlayers
from nflpool.data.seasoninfo import SeasonInfo


def test_season_row(db_session):
    season_row = db_session.query(SeasonInfo.id).first()
    print(season_row)
    # season_id = season_row.current_season
    assert season_row[0] == 1


def test_season(db_session):
    season_row = db_session.query(SeasonInfo).filter(SeasonInfo.id == "1").first()
    season = season_row.current_season
    assert season == 2018


def test_activeplayers_json_response():
    import nflpool.data.secret as secret
    from requests.auth import HTTPBasicAuth
    import requests

    response = requests.get(
        "https://api.mysportsfeeds.com/v2.0/pull/nfl/players.json?season=2018&rosterstatus=ROSTER",
        auth=HTTPBasicAuth(secret.msf_api, secret.msf_v2pw),
    )
    assert response.status_code == 200


def test_add_active_nflplayers(activeplayer_json, db_session):
    # 3 A's of test: Arrange, Act, then Assert

    player_list = activeplayer_json

    for players in player_list:
        try:
            firstname = players["player"]["firstName"]
            lastname = players["player"]["lastName"]
            player_id = players["player"]["id"]
            team_id = players["teamAsOfDate"]["id"]
            position = players["player"]["primaryPosition"]
        except KeyError:
            continue

        assert players["player"]["firstName"] is "Aaron"
        assert players["player"]["lastName"] is "Rodgers"
        assert players["player"]["id"] == 6914
        assert players["teamAsOfDate"]["id"] == 62
        assert players["player"]["primaryPosition"] is "QB"

        season_row = db_session.query(SeasonInfo).filter(SeasonInfo.id == "1").first()
        season = season_row.current_season

        active_players = ActiveNFLPlayers(
            firstname=firstname,
            lastname=lastname,
            player_id=player_id,
            team_id=team_id,
            position=position,
            season=season,
        )

        db_session.add(active_players)
