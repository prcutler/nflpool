from nflpool.data.modelbase import SqlAlchemyBase
import sqlalchemy


# TODO Do I need to do a foreign key on the Integers to the team and player tables?
# Point values for each category
class WeeklyStats(SqlAlchemyBase):
    __tablename__ = 'WeeklyStats'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    season = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    week = sqlalchemy.Column(sqlalchemy.Integer, index=True)

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

    #Individual Stats - Value and then player
    afc_rushing_first = sqlalchemy.Column(sqlalchemy.Integer)
    afc_rushing_second = sqlalchemy.Column(sqlalchemy.Integer)
    afc_rushing_third = sqlalchemy.Column(sqlalchemy.Integer)
    afc_rushing_fourth = sqlalchemy.Column(sqlalchemy.Integer)
    afc_rushing_fifth = sqlalchemy.Column(sqlalchemy.Integer)
    
    afc_rushing_first_player = sqlalchemy.Column(sqlalchemy.Integer)
    afc_rushing_second_player = sqlalchemy.Column(sqlalchemy.Integer)
    afc_rushing_third_player = sqlalchemy.Column(sqlalchemy.Integer)
    afc_rushing_fourth_player = sqlalchemy.Column(sqlalchemy.Integer)
    afc_rushing_fifth_player = sqlalchemy.Column(sqlalchemy.Integer)

    afc_passing_first = sqlalchemy.Column(sqlalchemy.Integer)
    afc_passing_second = sqlalchemy.Column(sqlalchemy.Integer)
    afc_passing_third = sqlalchemy.Column(sqlalchemy.Integer)
    afc_passing_fourth = sqlalchemy.Column(sqlalchemy.Integer)
    afc_passing_fifth = sqlalchemy.Column(sqlalchemy.Integer)
    
    afc_passing_first_player = sqlalchemy.Column(sqlalchemy.Integer)
    afc_passing_second_player = sqlalchemy.Column(sqlalchemy.Integer)
    afc_passing_third_player = sqlalchemy.Column(sqlalchemy.Integer)
    afc_passing_fourth_player = sqlalchemy.Column(sqlalchemy.Integer)
    afc_passing_fifth_player = sqlalchemy.Column(sqlalchemy.Integer)

    afc_receiving_first = sqlalchemy.Column(sqlalchemy.Integer)
    afc_receiving_second = sqlalchemy.Column(sqlalchemy.Integer)
    afc_receiving_third = sqlalchemy.Column(sqlalchemy.Integer)
    afc_receiving_fourth = sqlalchemy.Column(sqlalchemy.Integer)
    afc_receiving_fifth = sqlalchemy.Column(sqlalchemy.Integer)
    
    afc_receiving_first_player = sqlalchemy.Column(sqlalchemy.Integer)
    afc_receiving_second_player = sqlalchemy.Column(sqlalchemy.Integer)
    afc_receiving_third_player = sqlalchemy.Column(sqlalchemy.Integer)
    afc_receiving_fourth_player = sqlalchemy.Column(sqlalchemy.Integer)
    afc_receiving_fifth_player = sqlalchemy.Column(sqlalchemy.Integer)

    afc_sacks_first = sqlalchemy.Column(sqlalchemy.Integer)
    afc_sacks_second = sqlalchemy.Column(sqlalchemy.Integer)
    afc_sacks_third = sqlalchemy.Column(sqlalchemy.Integer)
    afc_sacks_fourth = sqlalchemy.Column(sqlalchemy.Integer)
    afc_sacks_fifth = sqlalchemy.Column(sqlalchemy.Integer)
    
    afc_sacks_first_player = sqlalchemy.Column(sqlalchemy.Integer)
    afc_sacks_second_player = sqlalchemy.Column(sqlalchemy.Integer)
    afc_sacks_third_player = sqlalchemy.Column(sqlalchemy.Integer)
    afc_sacks_fourth_player = sqlalchemy.Column(sqlalchemy.Integer)
    afc_sacks_fifth_player = sqlalchemy.Column(sqlalchemy.Integer)

    afc_int_first = sqlalchemy.Column(sqlalchemy.Integer)
    afc_int_second = sqlalchemy.Column(sqlalchemy.Integer)
    afc_int_third = sqlalchemy.Column(sqlalchemy.Integer)
    afc_int_fourth = sqlalchemy.Column(sqlalchemy.Integer)
    afc_int_fifth = sqlalchemy.Column(sqlalchemy.Integer)
    
    afc_int_first_player = sqlalchemy.Column(sqlalchemy.Integer)
    afc_int_second_player = sqlalchemy.Column(sqlalchemy.Integer)
    afc_int_third_player = sqlalchemy.Column(sqlalchemy.Integer)
    afc_int_fourth_player = sqlalchemy.Column(sqlalchemy.Integer)
    afc_int_fifth_player = sqlalchemy.Column(sqlalchemy.Integer)

    nfc_rushing_first = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_rushing_second = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_rushing_third = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_rushing_fourth = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_rushing_fifth = sqlalchemy.Column(sqlalchemy.Integer)

    nfc_rushing_first_player = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_rushing_second_player = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_rushing_third_player = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_rushing_fourth_player = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_rushing_fifth_player = sqlalchemy.Column(sqlalchemy.Integer)

    nfc_passing_first = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_passing_second = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_passing_third = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_passing_fourth = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_passing_fifth = sqlalchemy.Column(sqlalchemy.Integer)

    nfc_passing_first_player = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_passing_second_player = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_passing_third_player = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_passing_fourth_player = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_passing_fifth_player = sqlalchemy.Column(sqlalchemy.Integer)

    nfc_receiving_first = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_receiving_second = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_receiving_third = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_receiving_fourth = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_receiving_fifth = sqlalchemy.Column(sqlalchemy.Integer)

    nfc_receiving_first_player = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_receiving_second_player = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_receiving_third_player = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_receiving_fourth_player = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_receiving_fifth_player = sqlalchemy.Column(sqlalchemy.Integer)

    nfc_sacks_first = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_sacks_second = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_sacks_third = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_sacks_fourth = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_sacks_fifth = sqlalchemy.Column(sqlalchemy.Integer)

    nfc_sacks_first_player = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_sacks_second_player = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_sacks_third_player = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_sacks_fourth_player = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_sacks_fifth_player = sqlalchemy.Column(sqlalchemy.Integer)

    nfc_int_first = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_int_second = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_int_third = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_int_fourth = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_int_fifth = sqlalchemy.Column(sqlalchemy.Integer)

    nfc_int_first_player = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_int_second_player = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_int_third_player = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_int_fourth_player = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_int_fifth_player = sqlalchemy.Column(sqlalchemy.Integer)

    # Conference Team with most Points For
    afc_pf = sqlalchemy.Column(sqlalchemy.Integer)
    nfc_pf = sqlalchemy.Column(sqlalchemy.Integer)

    # Tiebreaker
    specialteams_td = sqlalchemy.Column(sqlalchemy.Integer)
    specialteams_td_team = sqlalchemy.Column(sqlalchemy.Integer)
