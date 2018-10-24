import pytest
from tests.schema import dal, Base
from sqlalchemy.orm import scoped_session


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


@pytest.fixture(scope="session")
def session(request):
    dal.conn_string = "sqlite:///test_nflpooldb.sqlite"
    dal.connect()

    dal.Session = scoped_session(dal.Session)
    dal.session = dal.Session()
    dal.Session.registry.clear()

    request.addfinalizer(Base.metadata.drop_all)
    return dal.session


@pytest.fixture(scope="function")
def db_session(request, session):
    request.addfinalizer(session.rollback)
    return session
