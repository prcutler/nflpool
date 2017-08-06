from nflpool.data.modelbase import SqlAlchemyBase
import sqlalchemy


# Point values for each category
class PlayerPicks(SqlAlchemyBase):
    __tablename__ = 'PlayerPicks'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('Account.id'))
    season = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    date_submitted = sqlalchemy.Column(sqlalchemy.DATETIME)

    # Division Points
    afc_east_first = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    afc_east_second = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    afc_east_last = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    afc_north_first = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    afc_north_second = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    afc_north_last = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    afc_south_first = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    afc_south_second = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    afc_south_last = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    afc_west_first = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    afc_west_second = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    afc_west_last = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    nfc_east_first = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    nfc_east_second = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    nfc_east_last = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    nfc_north_first = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    nfc_north_second = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    nfc_north_last = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    nfc_south_first = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    nfc_south_second = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    nfc_south_last = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    nfc_west_first = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    nfc_west_second = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    nfc_west_last = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    #Playoff Wildcards
    afc_wildcard1 = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    afc_wildcard2 = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    nfc_wildcard1 = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    nfc_wildcard2 = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    #Individual Stats
    afc_rushing_first = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    afc_rushing_second = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    afc_rushing_third = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    afc_passing_first = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    afc_passing_second = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    afc_passing_third = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    afc_receiving_first = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    afc_receiving_second = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    afc_receiving_third = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    afc_sacks_first = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    afc_sacks_second = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    afc_sacks_third = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    afc_int_first = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    afc_int_second = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    afc_int_third = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    nfc_rushing_first = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    nfc_rushing_second = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    nfc_rushing_third = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    nfc_passing_first = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    nfc_passing_second = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    nfc_passing_third = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    nfc_receiving_first = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    nfc_receiving_second = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    nfc_receiving_third = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    nfc_sacks_first = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    nfc_sacks_second = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    nfc_sacks_third = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    nfc_int_first = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    nfc_int_second = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    nfc_int_third = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    # Conference Team with most Points For
    afc_pf = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    nfc_pf = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    # Tiebreaker
    specialteams_td = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
