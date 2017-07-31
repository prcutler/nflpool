from nflpool.data.modelbase import SqlAlchemyBase
import sqlalchemy


class ActivePlayers(SqlAlchemyBase):
    __tablename__ = 'ActivePlayers'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, index=True)
    season = sqlalchemy.Column(sqlalchemy.Integer)
    team_id = sqlalchemy.Column(sqlalchemy.Integer)
    firstname = sqlalchemy.Column(sqlalchemy.String)
    lastname = sqlalchemy.Column(sqlalchemy.String)
    position = sqlalchemy.Column(sqlalchemy.String)
    player_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('TeamInfo.team_id'))


