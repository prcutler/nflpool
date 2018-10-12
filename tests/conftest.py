import pytest


@pytest.fixture()
def activeplayer_json():
    player_list = [
        {
            "player": {
                "id": 6914,
                "firstName": "Aaron",
                "lastName": "Rodgers",
                "primaryPosition": "QB",
                "alternatePositions": [],
                "jerseyNumber": 12,
                "currentTeam": {"id": 62, "abbreviation": "GB"},
                "currentRosterStatus": "ROSTER",
                "currentInjury": {
                    "description": "knee",
                    "playingProbability": "QUESTIONABLE",
                },
                "height": "6'2\"",
                "weight": 225,
                "birthDate": "1983-12-02",
                "age": 34,
                "birthCity": "Chico, CA",
                "birthCountry": "USA",
                "officialImageSrc": "http://static.nfl.com/static/content/public/static/img/fantasy/transparent/200x200/ROD339293.png",
                "socialMediaAccounts": [],
                "externalMappings": [
                    {"source": "NFL.com Stats Leaders", "id": "ROD339293"}
                ],
            },
            "teamAsOfDate": {"id": 62, "abbreviation": "GB"},
        }
    ]

    return player_list
