from nflpool.data.modelbase import SqlAlchemyBase
import sqlalchemy


class ConferenceInfo(SqlAlchemyBase):
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    conference = sqlalchemy.Column(sqlalchemy.String)
    conference_id = sqlalchemy.Column(sqlalchemy.Integer)
