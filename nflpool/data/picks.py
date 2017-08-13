from nflpool.data.modelbase import SqlAlchemyBase
import sqlalchemy


# Point values for each category
class PlayerPicks(SqlAlchemyBase):
    __tablename__ = 'PlayerPicks_old'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey('Account.id'))
    season = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    date_submitted = sqlalchemy.Column(sqlalchemy.DATETIME)

    # Division Points
    afc_east_first = sqlalchemy.Column(sqlalchemy.Integer)
    afc_east_second = sqlalchemy.Column(sqlalchemy.Integer)
    afc_east_last = sqlalchemy.Column(sqlalchemy.Integer)

    afc_north_first = sqlalchemy.Column(sqlalchemy.Integer)
    afc_north_second = sqlalchemy.Column(sqlalchemy.Integer)
    afc_north_last = sqlalchemy.Column(sqlalchemy.Integer)

    afc_south_first = sqlalchemy.Column(sqlalchemy.Integer)
    afc_south_second = sqlalchemy.Column(sqlalchemy.Integer)
    afc_south_last = sqlalchemy.Column(sqlalchemy.Integer)

    afc_west_first = sqlalchemy.Column(sqlalchemy.Integer)
    afc_west_second = sqlalchemy.Column(sqlalchemy.Integer)
    afc_west_last = sqlalchemy.Column(sqlalchemy.Integer)

    nfc_east_first = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_east_second = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_east_last = sqlalchemy.Column(sqlalchemy.Integer)

    nfc_north_first = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_north_second = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_north_last = sqlalchemy.Column(sqlalchemy.Integer)

    nfc_south_first = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_south_second = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_south_last = sqlalchemy.Column(sqlalchemy.Integer)

    nfc_west_first = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_west_second = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_west_last = sqlalchemy.Column(sqlalchemy.Integer)

    #Playoff Wildcards
    afc_wildcard1 = sqlalchemy.Column(sqlalchemy.Integer)
    afc_wildcard2 = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_wildcard1 = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_wildcard2 = sqlalchemy.Column(sqlalchemy.Integer)

    #Individual Stats
    afc_rushing_pick = sqlalchemy.Column(sqlalchemy.Integer)
    afc_passing_pick = sqlalchemy.Column(sqlalchemy.Integer)
    afc_receiving_pick = sqlalchemy.Column(sqlalchemy.Integer)
    afc_sacks_pick = sqlalchemy.Column(sqlalchemy.Integer)
    afc_int_pick = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_rushing_pick = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_passing_pick = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_receiving_pick = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_sacks_pick = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_int_pick = sqlalchemy.Column(sqlalchemy.Integer)

    # Conference Team with most Points For
    afc_pf = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_pf = sqlalchemy.Column(sqlalchemy.Integer)

    # Tiebreaker
    specialteams_td = sqlalchemy.Column(sqlalchemy.Integer)
