from nflpool.data.modelbase import SqlAlchemyBase
import sqlalchemy


class TeamInfo(SqlAlchemyBase):
    team_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    city = sqlalchemy.Column(sqlalchemy.String)
    abbreviation = sqlalchemy.Column(sqlalchemy.String)
    conference = sqlalchemy.Column(sqlalchemy.String)
    division = sqlalchemy.Column(sqlalchemy.String)

