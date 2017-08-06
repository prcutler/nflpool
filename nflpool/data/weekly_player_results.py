from nflpool.data.modelbase import SqlAlchemyBase
import sqlalchemy


class WeeklyPlayerResults(SqlAlchemyBase):
    __tablename__ = 'WeeklyPlayerResults'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, index=True)
    season = sqlalchemy.Column(sqlalchemy.Integer)
    week = sqlalchemy.Column(sqlalchemy.Integer)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('Account.id'))
    week_points = sqlalchemy.Column(sqlalchemy.Integer)
