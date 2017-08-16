from nflpool.data.modelbase import SqlAlchemyBase
import sqlalchemy


class SeasonInfo(SqlAlchemyBase):
    __tablename__ = 'SeasonInfo'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    current_season = sqlalchemy.Column(sqlalchemy.String)



