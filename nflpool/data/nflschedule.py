from nflpool.data.modelbase import SqlAlchemyBase
import sqlalchemy


class NFLSchedule(SqlAlchemyBase):
    __tablename__ = 'NFLSchedule'
    game_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    game_date = sqlalchemy.Column(sqlalchemy.DateTime, index=True)
    away_team = sqlalchemy.Column(sqlalchemy.Integer)
    home_team = sqlalchemy.Column(sqlalchemy.Integer)
    week = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    season = sqlalchemy.Column(sqlalchemy.Integer)
