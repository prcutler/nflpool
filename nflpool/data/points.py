from nflpool.data.modelbase import SqlAlchemyBase
import sqlalchemy


# Point values for each category
class Points(SqlAlchemyBase):
    __tablename__ = 'Points'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    # Division Points
    afc_east_first_pts = sqlalchemy.Column(sqlalchemy.Integer)
    afc_east_second_pts = sqlalchemy.Column(sqlalchemy.Integer)
    afc_east_last_pts = sqlalchemy.Column(sqlalchemy.Integer)

    afc_north_first_pts = sqlalchemy.Column(sqlalchemy.Integer)
    afc_north_second_pts = sqlalchemy.Column(sqlalchemy.Integer)
    afc_north_last_pts = sqlalchemy.Column(sqlalchemy.Integer)

    afc_south_first_pts = sqlalchemy.Column(sqlalchemy.Integer)
    afc_south_second_pts = sqlalchemy.Column(sqlalchemy.Integer)
    afc_south_last_pts = sqlalchemy.Column(sqlalchemy.Integer)

    afc_west_first_pts = sqlalchemy.Column(sqlalchemy.Integer)
    afc_west_second_pts = sqlalchemy.Column(sqlalchemy.Integer)
    afc_west_last_pts = sqlalchemy.Column(sqlalchemy.Integer)

    nfc_east_first_pts = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_east_second_pts = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_east_last_pts = sqlalchemy.Column(sqlalchemy.Integer)

    nfc_north_first_pts = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_north_second_pts = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_north_last_pts = sqlalchemy.Column(sqlalchemy.Integer)

    nfc_south_first_pts = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_south_second_pts = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_south_last_pts = sqlalchemy.Column(sqlalchemy.Integer)

    nfc_west_first_pts = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_west_second_pts = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_west_last_pts = sqlalchemy.Column(sqlalchemy.Integer)

    #Playoff Wildcards
    afc_wildcard1_pts = sqlalchemy.Column(sqlalchemy.Integer)
    afc_wildcard2_pts = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_wildcard1_pts = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_wildcard2_pts = sqlalchemy.Column(sqlalchemy.Integer)

    #Individual Stats
    afc_rushing_first_pts = sqlalchemy.Column(sqlalchemy.Integer)
    afc_rushing_second_pts = sqlalchemy.Column(sqlalchemy.Integer)
    afc_rushing_third_pts = sqlalchemy.Column(sqlalchemy.Integer)

    afc_passing_first_pts = sqlalchemy.Column(sqlalchemy.Integer)
    afc_passing_second_pts = sqlalchemy.Column(sqlalchemy.Integer)
    afc_passing_third_pts = sqlalchemy.Column(sqlalchemy.Integer)

    afc_receiving_first_pts = sqlalchemy.Column(sqlalchemy.Integer)
    afc_receiving_second_pts = sqlalchemy.Column(sqlalchemy.Integer)
    afc_receiving_third_pts = sqlalchemy.Column(sqlalchemy.Integer)

    afc_sacks_first_pts = sqlalchemy.Column(sqlalchemy.Integer)
    afc_sacks_second_pts = sqlalchemy.Column(sqlalchemy.Integer)
    afc_sacks_third_pts = sqlalchemy.Column(sqlalchemy.Integer)

    afc_int_first_pts = sqlalchemy.Column(sqlalchemy.Integer)
    afc_int_second_pts = sqlalchemy.Column(sqlalchemy.Integer)
    afc_int_third_pts = sqlalchemy.Column(sqlalchemy.Integer)

    nfc_rushing_first_pts = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_rushing_second_pts = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_rushing_third_pts = sqlalchemy.Column(sqlalchemy.Integer)

    nfc_passing_first_pts = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_passing_second_pts = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_passing_third_pts = = sqlalchemy.Column(sqlalchemy.Integer)

    nfc_receiving_first_pts = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_receiving_second_pts = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_receiving_third_pts = sqlalchemy.Column(sqlalchemy.Integer)

    nfc_sacks_first_pts = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_sacks_second_pts = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_sacks_third_pts = sqlalchemy.Column(sqlalchemy.Integer)

    nfc_int_first_pts = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_int_second_pts = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_int_third_pts = sqlalchemy.Column(sqlalchemy.Integer)

    # Conference Team with most Points For
    afc_pf_pts = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_pf_pts = sqlalchemy.Column(sqlalchemy.Integer)

    # Tiebreaker
    specialteams_td_pts = sqlalchemy.Column(sqlalchemy.Integer)
