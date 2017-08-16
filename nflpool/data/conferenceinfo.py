from nflpool.data.modelbase import SqlAlchemyBase
import sqlalchemy


# Point values for each category
class ConferenceInfo(SqlAlchemyBase):
    __tablename__ = 'ConferenceInfo'
    conf_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    conference = sqlalchemy.Column(sqlalchemy.String)
