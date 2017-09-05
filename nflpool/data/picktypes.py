from nflpool.data.modelbase import SqlAlchemyBase
import sqlalchemy


# Point values for each category
class PickTypes(SqlAlchemyBase):
    __tablename__ = 'PickTypes'
    pick_type_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
