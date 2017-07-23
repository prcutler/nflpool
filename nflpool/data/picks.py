import mongoengine


# Making all fields IntField - using Player ID numbers to store picks in the db, not names
class PlayerPicks(mongoengine.EmbeddedDocument):
    afc_east_first_pick = mongoengine.IntField()
    afc_east_second_pick = mongoengine.IntField()
    afc_east_last_pick = mongoengine.IntField()
    afc_north_first_pick = mongoengine.IntField()
    afc_north_second_pick = mongoengine.IntField()
    afc_north_last_pick = mongoengine.IntField()
    afc_south_first_pick = mongoengine.IntField()
    afc_south_second_pick = mongoengine.IntField()
    afc_south_last_pick = mongoengine.IntField()
    afc_west_first_pick = mongoengine.IntField()
    afc_west_second_pick = mongoengine.IntField()
    afc_west_last_pick = mongoengine.IntField()
    nfc_east_first_pick = mongoengine.IntField()
    nfc_east_second_pick = mongoengine.IntField()
    nfc_east_last_pick = mongoengine.IntField()
    nfc_north_first_pick = mongoengine.IntField()
    nfc_north_second_pick = mongoengine.IntField()
    nfc_north_last_pick = mongoengine.IntField()
    nfc_south_first_pick = mongoengine.IntField()
    nfc_south_second_pick = mongoengine.IntField()
    nfc_south_last_pick = mongoengine.IntField()
    nfc_west_first_pick = mongoengine.IntField()
    nfc_west_second_pick = mongoengine.IntField()
    nfc_west_last_pick = mongoengine.IntField()
    afc_wildcard1_pick = mongoengine.IntField()
    afc_wildcard2_pick = mongoengine.IntField()
    nfc_wildcard1_pick = mongoengine.IntField()
    nfc_wildcard2_pick = mongoengine.IntField()
    afc_rushing_leader_pick = mongoengine.IntField()
    afc_passing_leader_pick = mongoengine.IntField()
    afc_receiving_leader_pick = mongoengine.IntField()
    afc_sacks_leader_pick = mongoengine.IntField()
    afc_int_leader_pick = mongoengine.IntField()
    nfc_rushing_leader_pick = mongoengine.IntField()
    nfc_passing_leader_pick = mongoengine.IntField()
    nfc_receiving_leader_pick = mongoengine.IntField()
    nfc_sacks_leader_pick = mongoengine.IntField()
    nfc_int_leader_pick = mongoengine.IntField()
    afc_pf_pick = mongoengine.IntField()
    nfc_pf_pick = mongoengine.IntField()
    tiebreaker_pick = mongoengine.IntField()
    date = mongoengine.DateTimeField()

    meta = {
        'db_alias': 'core',
        'collection': 'users,'
    }