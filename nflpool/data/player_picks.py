from nflpool.data.modelbase import SqlAlchemyBase
import sqlalchemy


# Point values for each category
class PlayerPicks(SqlAlchemyBase):
    __tablename__ = 'PlayerPicksv2'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey('Account.id'))
    season = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    date_submitted = sqlalchemy.Column(sqlalchemy.DATETIME)

    conf_id = sqlalchemy.Column(sqlalchemy.Integer)
    division_id = sqlalchemy.Column(sqlalchemy.Integer)
    rank = sqlalchemy.Column(sqlalchemy.Integer)
    team = sqlalchemy.Column(sqlalchemy.Integer)
    multiplier = sqlalchemy.Column(sqlalchemy.Integer)
    player_id = sqlalchemy.Column(sqlalchemy.Integer)
    pick_type = sqlalchemy.Column(sqlalchemy.Integer)
