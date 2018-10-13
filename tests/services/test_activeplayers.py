import pytest


def test_add_active_nflplayers(activeplayer_json):
    # 3 A's of test: Arrange, Act, then Assert

    player_list = activeplayer_json

    for players in player_list:
        assert players["player"]["firstName"] is "Aaron"
        assert players["player"]["lastName"] is "Rodgers"
        assert players["player"]["id"] == 6914
        assert players["teamAsOfDate"]["id"] == 62
        assert players["player"]["primaryPosition"] is "QB"
