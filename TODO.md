#NFLPool To-Do List

## Overview

There is a lot to be done to get NFLPool ready for the 2017 season. 
This list in no way is complete.

##Database Setup - 0.1
* Define NFLPool Players fields needed and create script to import
NFLPool Player picks (all in one table or one table per year?)
* Document database model
* Currently using SQLite for the database.  This will need to move to
MySQL for production.  Maybe.

##Scoring - 0.2
* Write scripts to import weekly statistics for NFL player stats,
conference leaders (points for), division standings, and division leaders
* Create script to read NFLPool Player picks, look at the statistics,
and calculate each NFLPool Player's score

##Weekly Results - 0.3
* Update database to include week column and store data weekly instead of
cumulative results
* Add functionality to figure out what NFL week (1-17) is when making weekly results

##Web front-end for nflpool.xyz
* Not even going to worry about this right now.
* Account creation via oauth
* Add functionality to automatically figure out what year it is when making picks


##Completed
* NFL Player List: Determine if needed and if so, create import script
to put all active NFL players in their own table
* nflpool currently imports each JSON manually by changing the name of
the file.  This needs to use requests to download via network and not
from file
* Write settings.py file with MySportsFeed API login information
* Import player picks from CSV:
 * Add user_id column
 * Remove primary key from table creation setup script




