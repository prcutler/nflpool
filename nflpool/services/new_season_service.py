from sqlalchemy.orm import joinedload
import sqlalchemy.orm
from nflpool.data.activeplayers import ActiveNFLPlayers
from nflpool.data.admin import AdminInfo
import requests
import nflpool.data.secret as secret
from requests.auth import HTTPBasicAuth
from nflpool.data.dbsession import DbSessionFactory


class NewSeasonService:

    @staticmethod
    def get_season():
        return []

    @classmethod
    def create_season(cls, season: int):

        session = DbSessionFactory.create_session()

        new_season = AdminInfo()
        season.current_season = new_season


