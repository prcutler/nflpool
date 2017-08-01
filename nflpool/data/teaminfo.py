from nflpool.data.modelbase import SqlAlchemyBase
import sqlalchemy


class TeamInfo(SqlAlchemyBase):
    __tablename__ = 'TeamInfo'
    team_id = sqlalchemy.Column(sqlalchemy.Integer, index=True, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    city = sqlalchemy.Column(sqlalchemy.String)
    team_abbr = sqlalchemy.Column(sqlalchemy.String)
    conference = sqlalchemy.Column(sqlalchemy.String)
    division = sqlalchemy.Column(sqlalchemy.String)
    division_abbr = sqlalchemy.Column(sqlalchemy.String)
    division_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('DivisionInfo.division_id'))


