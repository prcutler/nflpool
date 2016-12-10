import csv
import collections
from collections import namedtuple

nfl_pool_players = []
playerpicks = collections.namedtuple('player_picks',
                                        'timestamp, firstname, lastname, email, afc_east_first, afc_east_second,'
                                        'afc_east_last,afc_north_first, afc_north_second, afc_north_last,'
                                        'afc_south_first, afc_south_second, afc_south_last, afc_west_first,'
                                        'afc_west_second, afc_west_last, nfc_east_first, nfc_east_second,'
                                        'nfc_east_last, nfc_north_first, nfc_north_second,nfc_north_last,'
                                        'nfc_south_first, nfc_south_second, nfc_south_last, nfc_west_first,'
                                        'nfc_west_second,nfc_west_last, afc_wildcard1, afc_wildcard2,'
                                        'nfc_wildcard1, nfc_wildcard2, afc_rushing_leader,'
                                        'afc_passing_leader, afc_receiving_leader, afc_sacks_leader,'
                                        'afc_int_leader,afc_pf,nfc_rushing_leader, nfc_passing_leader,'
                                        'nfc_receiving_leader, nfc_sacks_leader,'
                                        'nfc_int_leader, nfc_pf,tiebreaker'

                                     )

with open('json/2016_playerpicks.csv') as infile:
    reader = csv.DictReader(infile)
    picks = collections.namedtuple('picks', reader.fieldnames)
    playerpicks = [picks(**row) for row in reader]


#with open('json/2016_playerpicks.csv', 'r') as playerpicks:
    # fieldnames = [timestamp,firstname,lastname,email,afc_east_first,afc_east_second,afc_east_last,
    #                  afc_north_first,afc_north_second,afc_north_last,afc_south_first,afc_south_second,
    #                  afc_south_last,afc_west_first,afc_west_second,afc_west_last,nfc_east_first,
    #                  nfc_east_second,nfc_east_last,nfc_north_first,nfc_north_second,nfc_north_last,
    #                  nfc_south_first,nfc_south_second,nfc_south_last,nfc_west_first,nfc_west_second,
    #                  nfc_west_last,afc_wildcard1,afc_wildcard2,nfc_wildcard1,nfc_wildcard2,afc_rushing_leader,
    #                  afc_passing_leader,afc_receiving_leader,afc_sacks_leader,afc_int_leader,afc_pf,
    #                  nfc_rushing_leader,nfc_passing_leader,nfc_receiving_leader,nfc_sacks_leader,
    #                  nfc_int_leader,nfc_pf,tiebreaker]


#    reader = csv.DictReader(playerpicks)
#    for row in playerpicks:
#        print(row)

print(playerpicks[0])

# TODO Make each tuple slice into its own tuple

#print(playerpicks[0])
#print(type(playerpicks[0]))
