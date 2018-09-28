from nflpool.data.modelbase import SqlAlchemyBase
import sqlalchemy


class WeeklyPlayerResults(SqlAlchemyBase):
    __tablename__ = "WeeklyPlayerResults"
    primary_key = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True
    )
    pick_id = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    season = sqlalchemy.Column(sqlalchemy.Integer)
    week = sqlalchemy.Column(sqlalchemy.Integer)
    points_earned = sqlalchemy.Column(sqlalchemy.Integer)
