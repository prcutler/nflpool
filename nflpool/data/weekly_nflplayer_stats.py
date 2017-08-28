from nflpool.data.modelbase import SqlAlchemyBase
import sqlalchemy


# Store all individual NFL Player stats in this table
class WeeklyNFLPlayerStats(SqlAlchemyBase):
    __tablename__ = 'WeeklyNFLPlayerStats'
    primary_key = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    season = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    week = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    player_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('ActiveNFLPlayers.player_id'))
    passyds = sqlalchemy.Column(sqlalchemy.Integer)
    rushyds = sqlalchemy.Column(sqlalchemy.Integer)
    recyds = sqlalchemy.Column(sqlalchemy.Integer)
    sacks = sqlalchemy.Column(sqlalchemy.REAL)
    interceptions = sqlalchemy.Column(sqlalchemy.Integer)
