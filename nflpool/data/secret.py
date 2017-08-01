import os
import nflpool

# You will need an account from MySportsFeed to access their API.  They offer free access to developers
# Edit below with your credentials and then save as secret.py

msf_username = 'prcutler'
msf_pw = 'r6RWPADULVd3wj'

base_url = 'https://www.mysportsfeeds.com/api/feed/pull/nfl/'


def db_location():
    top_folder = os.path.dirname(nflpool.__file__)
    rel_folder = os.path.join('db', 'nflpooldb.sqlite')

    db_file = os.path.join(top_folder, rel_folder)
