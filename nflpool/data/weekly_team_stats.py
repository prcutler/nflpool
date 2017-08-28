from nflpool.data.modelbase import SqlAlchemyBase
import sqlalchemy


# Store all individual NFL Player stats in this table
class WeeklyTeamStats(SqlAlchemyBase):
    __tablename__ = 'WeeklyTeamStats'
    primary_key = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    season = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    week = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    team_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('TeamInfo.team_id'))
    division_rank = sqlalchemy.Column(sqlalchemy.Integer)
    conference_rank = sqlalchemy.Column(sqlalchemy.Integer)
    points_for = sqlalchemy.Column(sqlalchemy.Integer)
    tiebreaker_td = sqlalchemy.Column(sqlalchemy.Integer)
    tiebreaker_team = sqlalchemy.Column(sqlalchemy.Integer)
