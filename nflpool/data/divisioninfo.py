from nflpool.data.modelbase import SqlAlchemyBase
import sqlalchemy


# Point values for each category
class DivisionInfo(SqlAlchemyBase):
    __tablename__ = "DivisionInfo"
    division_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    division = sqlalchemy.Column(sqlalchemy.String)
