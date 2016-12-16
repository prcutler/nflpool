import json
import csv
import os

from player_class import Players


def main():
    filename = get_data_file()
    data = load_file(filename)


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


if __name__ == '__main__':
    main()
