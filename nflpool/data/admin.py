from nflpool.data.modelbase import SqlAlchemyBase
import sqlalchemy


class AdminInfo(SqlAlchemyBase):
    __tablename__ = 'AdminInfo'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    current_season = sqlalchemy.Column(sqlalchemy.Integer)



