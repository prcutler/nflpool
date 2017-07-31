from nflpool.data.modelbase import SqlAlchemyBase
import sqlalchemy


# Point values for each category
class PlayerPicks(SqlAlchemyBase):
    __tablename__ = 'PlayerPicks'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    player_id = sqlalchemy.Column(sqlalchemy.Integer)
    season = sqlalchemy.Column(sqlalchemy.Integer)

    # Division Points
    afc_east_first = sqlalchemy.Column(sqlalchemy.Integer)
    afc_east_second = sqlalchemy.Column(sqlalchemy.Integer)
    afc_east_last = sqlalchemy.Column(sqlalchemy.Integer)

    afc_north_first = sqlalchemy.Column(sqlalchemy.Integer)
    afc_north_second = sqlalchemy.Column(sqlalchemy.Integer)
    afc_north_last =  = sqlalchemy.Column(sqlalchemy.Integer)

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
    afc_rushing_first = sqlalchemy.Column(sqlalchemy.Integer)
    afc_rushing_second = sqlalchemy.Column(sqlalchemy.Integer)
    afc_rushing_third = sqlalchemy.Column(sqlalchemy.Integer)

    afc_passing_first = sqlalchemy.Column(sqlalchemy.Integer)
    afc_passing_second = sqlalchemy.Column(sqlalchemy.Integer)
    afc_passing_third = sqlalchemy.Column(sqlalchemy.Integer)

    afc_receiving_first = sqlalchemy.Column(sqlalchemy.Integer)
    afc_receiving_second = sqlalchemy.Column(sqlalchemy.Integer)
    afc_receiving_third = sqlalchemy.Column(sqlalchemy.Integer)

    afc_sacks_first = sqlalchemy.Column(sqlalchemy.Integer)
    afc_sacks_second = sqlalchemy.Column(sqlalchemy.Integer)
    afc_sacks_third = sqlalchemy.Column(sqlalchemy.Integer)

    afc_int_first = sqlalchemy.Column(sqlalchemy.Integer)
    afc_int_second = sqlalchemy.Column(sqlalchemy.Integer)
    afc_int_third = sqlalchemy.Column(sqlalchemy.Integer)

    nfc_rushing_first = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_rushing_second = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_rushing_third = sqlalchemy.Column(sqlalchemy.Integer)

    nfc_passing_first = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_passing_second = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_passing_third = = sqlalchemy.Column(sqlalchemy.Integer)

    nfc_receiving_first = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_receiving_second = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_receiving_third = sqlalchemy.Column(sqlalchemy.Integer)

    nfc_sacks_first = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_sacks_second = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_sacks_third = sqlalchemy.Column(sqlalchemy.Integer)

    nfc_int_first = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_int_second = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_int_third = sqlalchemy.Column(sqlalchemy.Integer)

    # Conference Team with most Points For
    afc_pf = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_pf = sqlalchemy.Column(sqlalchemy.Integer)

    # Tiebreaker
    specialteams_td = sqlalchemy.Column(sqlalchemy.Integer)
