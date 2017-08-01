from nflpool.data.modelbase import SqlAlchemyBase
import sqlalchemy


class DivisionInfo(SqlAlchemyBase):
    __tablename__ = 'DivisionInfo'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, index=True)
    division = sqlalchemy.Column(sqlalchemy.String)
    division_id = sqlalchemy.Column(sqlalchemy.Integer)
    division_abbr = sqlalchemy.Column(sqlalchemy.String)
    conference_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('ConferenceInfo.conference_id'))

