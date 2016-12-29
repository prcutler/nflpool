import json
import csv
from collections import namedtuple

from player_class import Players


def main():
    filename = get_data_file()
    data = load_file(filename)
    division_standings()
    playoff_standings()
    playoff_standings()
    player_stats()
    points_for()
    tiebreaker()
    player_score()


# Import player picks into a Class
def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data',
                        '2016_playerpicks.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)
        player_picks = []
        for row in reader:
            p = Players.create_from_dict(row)
            player_picks.append(p)

    return player_picks


# Get Division Standings for each team
def division_standings:
    pass


# Get Playoff Standings for each team (need number 5 & 6 in each conference)
def playoff_standings:
    pass


# Get individual statistics for each category
def player_stats:
    pass


# Get points for for the number one team in each conference:
def points_for:
    pass


# Get the tiebreaker information
def tiebreaker:
    pass


# Calculate the player scores
def player_score:
    pass


if __name__ == '__main__':
    main()
