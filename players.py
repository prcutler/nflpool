

class Players:
    def __init__(self, firstname, lastname, email, twitter):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.twitter = twitter


class PlayerPicks(Players):
    def __init__(self, afc_east_first_pick, afc_east_second_pick, afc_east_last_pick, afc_north_first_pick,
                 afc_north_second_pick, afc_north_last_pick, afc_south_first_pick, afc_south_second_pick,
                 afc_south_last_pick, afc_west_first_pick, afc_west_second_pick, afc_west_last_pick,
                 nfc_east_first_pick, nfc_east_second_pick, nfc_east_last_pick, nfc_north_first_pick,
                 nfc_north_second_pick, nfc_north_last_pick, nfc_south_first_pick, nfc_south_second_pick,
                 nfc_south_last_pick, nfc_west_first_pick, nfc_west_second_pick, nfc_west_last_pick,
                 afc_wildcard1_pick, afc_wildcard2_pick, nfc_wildcard1_pick, nfc_wildcard2_pick,
                 afc_rushing_leader_pick, afc_passing_leader_pick, afc_sacks_leader_pick, afc_int_leader_pick,
                 nfc_rushing_leader_pick, nfc_passing_leader_pick, nfc_receiving_leader_pick,
                 nfc_sacks_leader_pick, nfc_int_leader_pick, afc_pf_pick, nfc_pf_pick, tiebreaker_pick
                 ):
        self.afc_east_first_pick = afc_east_first_pick
        self.afc_east_second_pick = afc_east_second_pick
        self.afc_east_last_pick = afc_east_last_pick
        self.afc_north_first_pick = afc_north_first_pick
        self.afc_north_second_pick = afc_north_second_pick
        self.afc_north_last_pick = afc_north_last_pick
        self.afc_south_first_pick = afc_south_first_pick
        self.afc_south_second_pick = afc_south_second_pick
        self.afc_south_last_pick = afc_south_last_pick
        self.afc_west_first_pick = afc_west_first_pick
        self.afc_west_second_pick = afc_west_second_pick
        self.afc_west_last_pick = afc_west_last_pick
        self.nfc_east_first_pick = nfc_east_first_pick
        self.nfc_east_second_pick = nfc_east_second_pick
        self.nfc_east_last_pick = nfc_east_last_pick
        self.nfc_north_first_pick = nfc_north_first_pick
        self.nfc_north_second_pick = nfc_north_second_pick
        self.nfc_north_last_pick = nfc_north_last_pick
        self.nfc_south_first_pick = nfc_south_first_pick
        self.nfc_south_second_pick = nfc_south_second_pick
        self.nfc_south_last_pick = nfc_south_last_pick
        self.nfc_west_first_pick = nfc_west_first_pick
        self.nfc_west_second_pick = nfc_west_second_pick
        self.nfc_west_last_pick = nfc_west_last_pick
        self.afc_wildcard1_pick = afc_wildcard1_pick
        self.afc_wildcard2_pick = afc_wildcard2_pick
        self.nfc_wildcard1_pick = nfc_wildcard1_pick
        self.nfc_wildcard2_pick = nfc_wildcard2_pick
        self.afc_rushing_leader_pick = afc_rushing_leader_pick
        self.afc_passing_leader_pick = afc_passing_leader_pick
        self.afc_receiving_leader_pick = afc_passing_leader_pick
        self.afc_sacks_leader_pick = afc_sacks_leader_pick
        self.afc_int_leader_pick = afc_int_leader_pick
        self.nfc_rushing_leader_pick = nfc_rushing_leader_pick
        self.nfc_passing_leader_pick = nfc_passing_leader_pick
        self.nfc_receiving_leader_pick = nfc_receiving_leader_pick
        self.nfc_sacks_leader_pick = nfc_sacks_leader_pick
        self.nfc_int_leader_pick = nfc_int_leader_pick
        self.afc_pf_pick = afc_pf_pick
        self.nfc_pf_pick = nfc_pf_pick
        self.tiebreaker_pick = tiebreaker_pick