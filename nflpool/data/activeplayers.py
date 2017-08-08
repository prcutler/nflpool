from nflpool.data.modelbase import SqlAlchemyBase
import sqlalchemy


class ActiveNFLPlayers(SqlAlchemyBase):
    __tablename__ = 'ActiveNFLPlayers'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, index=True)
    season = sqlalchemy.Column(sqlalchemy.Integer)
    team_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('TeamInfo.team_id'))
    firstname = sqlalchemy.Column(sqlalchemy.String)
    lastname = sqlalchemy.Column(sqlalchemy.String)
    position = sqlalchemy.Column(sqlalchemy.String, index=True)
    player_id = sqlalchemy.Column(sqlalchemy.Integer, index=True)


