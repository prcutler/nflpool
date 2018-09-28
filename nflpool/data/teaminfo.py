from nflpool.data.modelbase import SqlAlchemyBase
import sqlalchemy


class TeamInfo(SqlAlchemyBase):
    __tablename__ = "TeamInfo"
    team_id = sqlalchemy.Column(sqlalchemy.Integer, index=True, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    city = sqlalchemy.Column(sqlalchemy.String)
    team_abbr = sqlalchemy.Column(sqlalchemy.String)
    conference_id = sqlalchemy.Column(sqlalchemy.Integer)
    division_id = sqlalchemy.Column(sqlalchemy.Integer)
