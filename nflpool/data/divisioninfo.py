from nflpool.data.modelbase import SqlAlchemyBase
import sqlalchemy


class DivisionInfo(SqlAlchemyBase):
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    division = sqlalchemy.Column(sqlalchemy.String)
    division_id = sqlalchemy.Column(sqlalchemy.Integer)
    division_abbr = sqlalchemy.Column(sqlalchemy.String)
    conference_id = sqlalchemy.Column(sqlalchemy.Integer)
