#NFLPool To-Do List

## Overview

There is a lot to be done to get NFLPool ready for the 2017 season. 
This list in no way is complete.

##Database Setup
* NFL Player List: Determine if needed and if so, create import script
to put all active NFL players in their own table
* Define NFLPool Players fields needed and create script to import
NFLPool Player picks (all in one table or one table per year?)
* Write scripts to import weekly statistics for NFL player stats, 
conference leaders (points for), and division leaders
* Document database model
* Currently using SQLite for the database.  This will need to move to
MySQL for production

##JSON Importer
* nflpool currently imports each JSON manually by changing the name of 
the file.  This needs to use requests to download via network and not
from file
* Write settings.py file with MySportsFeed API login information
* Write BeautifulSoup script to scrape NFL.com for wild card leaders
for each conference

##Scoring
* Create script to read NFLPool Player pics, look at the statistics,
and calculate each NFLPool Player's score

##Web front-end for nflpool.xyz
* Not even going to worry about this right now.