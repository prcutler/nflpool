

# NFLPool Design Overview

## Overview

NFLPool is an application written in Python to calculate the scores
of an annual fantasy-like football pool.  You can find more
information on NFLPool and its rules at the
[NFLPool website](https://www.nflpool.xyz).

NFLPool is my first application written in Python and may not
be considered very Pythonic as I learn Python.

## Current application architecture (prototype)

NFLPool is written in Python 3.5 and makes extensive
use of the following Python modules:

* Requests
* JSON
* Collections (Named Tuples)
* CSV

NFLPool is targeted at CentOS 7 on [Digital Ocean](https://m.do.co/c/7c558d1bbb4c).
Python 3 will need to be installed separately and run in a
Python virtual environment (virtualenv).

NFLPool players currently make their annual picks via
Google Forms, which is outputted to a CSV file.

NFLPool gets NFL team and player statistics from
[MySportsFeeds](http://mysportsfeeds.com).  MySportsFeeds
offers free use of their service to developers and for
non-commercial use and also
[offers extremely reasonable pricing via Patreon](https://www.patreon.com/mysportsfeeds).
MySportsFeeds offers statistics via JSON, XML and CSV.
NFLPool uses JSON to consume the team and player statistics.

## Future application architecture

NFLPool for fall 2017 will move to a web application using
[Pyramid](http://www.trypyramid.com), a Python web framework
and use MySQL to store data.

NFLPool will offer NFLPool players the ability to make their
picks via the web and store the player picks in MySQL.

All statistics will be fetched via the MySportsFeed API
using the Python Requests module and saved in the MySQL database
using the SQLAlchemy ORM for Python.

Players will then be able to view their overall results in
relation to other players or view the weekly history as the
NFL season progresses.

A goal of NFLPool is to copy the architecture to
[MLBPool2.com](http://www.mlbpool2.com), from where the
idea for NFLPool came from.  The big difference between
NFLPool and MLBPool is that players are allowed to make
changes to their picks (though worth half the points) at
mid-season and no changes are allowed in NFLPool.

## NFLPool code overview

### Picks

At the beginning of the season, NFLPool players pick the following:

* Division winners (8 teams, one per division)
* Division 2nd place (8 teams, one per division)
* Last place division (8 teams, one per division)
* Teams that will make the playoffs as Wild Cards (2 per conference)
* Individual stat leaders in passing, rushing, receiving, interceptions and sacks (1 pick in each for each conference) (10 total)
* Team with the most points scored in each conference (2 teams, one in each conference)
* Tiebreaker pick (Team with most special teams touchdowns) (1)

### Point Values

Each pick a player makes can be worth up to three different
point values.  If a player were to pick Aaron Rodgers as the
NFL's Passing Yards Leader, and Aaron Rodgers was in first place
the pick is worth 30 points; second place is worth 20 points;
and if he has the third highest passing yards in the NFL, he
is worth 10 points.  If the NFLPool player is the ONLY person
to have picked Aaron Rodgers, the number of points would be
doubled.

All possible point values are currently stored in
[pointvalues.py](https://github.com/prcutler/nflpool/blob/master/pointvalues.py).


### Player Picks

Player picks are saved in Google Forms and then exported
to a CSV file.  Prior to exporting, the column headers
were changed to their Python variables names.

A Python script will be written to store the player picks
as a list of dictionaries.  A list of named tuples could
work for NFLPool, but may not work for MLBPool2 as the picks
will need to be mutable as they can be changed at mid-season.

Example:

```picks(timestamp='9/6/2016 17:39:41', firstname='Chris', lastname='Stone', email='stone@usisales.com', afc_east_first='Patriots', afc_east_second='Jets', afc_east_last='Bills', afc_north_first='Steelers', afc_north_second='Bengals', afc_north_last='Browns', afc_south_first='Colts', afc_south_second='Colts', afc_south_last='Titans', afc_west_first='Chiefs', afc_west_second='Raiders', afc_west_last='Broncos', nfc_east_first='Giants', nfc_east_second='Cowboys', nfc_east_last='Eagles', nfc_north_first='Packers', nfc_north_second='Vikings', nfc_north_last='Bears', nfc_south_first='Panthers', nfc_south_second='Saints', nfc_south_last='Falcons', nfc_west_first='Cardinals', nfc_west_second='Seahawks', nfc_west_last='49ers', afc_wildcard1='Bengals', afc_wildcard2='Raiders', nfc_wildcard1='Vikings', nfc_wildcard2='Cowboys', afc_rushing_leader='LeSean McCoy', afc_passing_leader='Phillip Rivers', afc_receiving_leader='Antonio Brown', afc_sacks_leader='Kahlil Mack', afc_int_leader='Devin McCourty', afc_pf='Steelers', nfc_rushing_leader='Adrian Peterson', nfc_passing_leader='Matthew Stafford', nfc_receiving_leader='Odell Beckham Jr.', nfc_sacks_leader='Cameron Jordan', nfc_int_leader='Earl Thomas', nfc_pf='Panthers', tiebreaker='Panthers')```

### Fetching Statistics

NFL statistics are provided by [MySportsFeeds](http://mysportsfeeds.com).
 MySportsFeeds uses HTTP Basic Authentication, which the Requests module
 can automatically can handle.  In the secret-config.py file,
 enter your MySportsfeed username and password and save the
 file as secret.py.  Don't forget to add this to your .gitignore!

All API feeds will use this in nflpool, such as:

```
    response = requests.get(
    'https://www.mysportsfeeds.com/api/feed/pull/nfl/2016-2017-regular/playoff_team_standings.json?teamstats',
    auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))
```


The following API feeds are used:

* [Division Team Standings](https://www.mysportsfeeds.com/data-feeds/nfl/feedlist/feedsummary?feed=division_team_standings):
 This is used to rank each team in their division and will be used to assign
 points for division winners, division second place and division last place.

* [Playoff Team Standings](https://www.mysportsfeeds.com/data-feeds/nfl/feedlist/feedsummary?feed=playoff_team_standings):
 This ranks all teams in the NFL (1-32) and needs to be sorted by conference.  This is
 primarily used for the Wild Card picks, which would be the teams ranked
 five and six in each of the two conferences (AFC and NFC).

* [Cumulative Player Stats](https://www.mysportsfeeds.com/data-feeds/nfl/feedlist/feedsummary?feed=cumulative_player_stats):
This includes a JSON file for every player in the NFL and is used for
passing, rushing, receiving, sacks and interceptions.  These stats are cumulative.


* [Conference Team Standings](https://www.mysportsfeeds.com/data-feeds/nfl/feedlist/feedsummary?feed=conference_team_standings):
 This is used to find the team with the most points scored (Points For) in
 each of the two conferences (AFC and NFC).

* [Overall Team Standings](https://www.mysportsfeeds.com/data-feeds/nfl/feedlist/feedsummary?feed=overall_team_standings)
 This is used to determine the tiebreaker (if needed) of the
 team with the most special teams touchdowns.

Future:

[Active Players](https://www.mysportsfeeds.com/data-feeds/nfl/feedlist/feedsummary?feed=active_players)
will be used to import all players into the database.  NFLPool players
will then make their picks for the year based on the feed, sorted by conference.



### Calculating an NFLPool player's points

A dictionary for each player will need to be created.  The
key / value pair would be the point category and the number of
points the player earned for that category (which could be zero).
The list is then summed to find the player's total points to determine
where they rank in NFLPool.

#### Division Standings

Each Division has four teams.  If the Patriots are in first place,
and the player picked the Patriots, the player earns 30 points.
If the NFLPool player is the only player to have picked the Patriots,
the points are doubled to 60.

This continues for second place and last place for all eight divisions.

```
If PlayerPick = TeamInFirst then points = 30
If PlayerPick != TeaminFirst then points = 0
If PlayerPick is <= 1, then points = points x 2
```

Append points earned to player_points dictionary.

#### Playoff Team Standings

Each conference has 16 teams.  The teams ranked 5th or 6th are
the Wild Card teams.  The NFLPool player has picked two teams.
If one or two teams are equal to the teams in the 5th or 6th rank
by conference, the player earns 25 points per team.  If the NFLPool
player is the only player to have picked the team(s), the NFLPool player
earns double.

```
If PlayerPick = Rank5 in AFC, points = 25
If PlayerPick <= 1, then points = points x2

If PlayerPick = Rank6 in AFC, points = 25
If PlayerPick <= 1, then points = points x2

If PlayerPick = Rank5 in NFC, points = 25
If PlayerPick <= 1, then points = points x2

If PlayerPick = Rank6 in NFC, points = 25
If PlayerPick <= 1, then points = points x2

If PlayerPick != Rank5 OR Rank6, points = 0
```

Append points earned to player_points dictionary.

#### Individual Statistics

NFLPool players can earn up to four point values based on how their
picks perform.  Each player makes one pick for the NFL leader in
a statistical category:

* Passing (QB)
* Rushing (RB)
* Receiving (WR or TE)
* Sacks (D)
* Interceptions (D)

If an NFLPool player's pick is in first place in the NFL, the pick
is worth 30 points.  Second place, 20; third place, 10.  Zero points
are earned if the player they picked is not ranked in the top three.
The NFLPool player can earn double points if they are the only
NFLPool player to pick the NFL player in a category.

Using Passing and Quarterback pick as an example:

```
If PlayerPick = NFLPlayer Rank 1, then points = 30
Elif PlayerPick = NFLPlayer Rank 2, then points = 20
Elif PlayerPick = NFLPlayer Rank 3, then points = 10
Elif PlayerPick <= 1 then points = points x 2
Else: 0
```

Append points earned to player_points dictionary.

Repeat for the other four statistical categories.

#### Points For

The NFLPool player picks one team in each conference that
will score the most points.

```
If PlayerPick = AFCMostPF, points = 20
Elif PlayerPick <= 1, points = points x 2
Else points = 0

If PlayerPick = NFCMostPF, points = 20
Elif PlayerPick <= 1, points = points x 2
Else points = 0
```

#### Calculating NFLPool Leaders

Once all of the calculations are complete, the dictionary storing
the NFLPool player's point totals are summed and sorted by
most to least points.  The player with the most points wins.

## Misc. Notes

Players can choose the same team in multiple spots in the Division
Standings picks.  For example, an NFLPool Player could choose
the Green Bay Packers to win the NFC North and also choose the
Green Bay Packers to place second in the NFC North division.

NFLPool Players choices for Wild Cards are not unique.  If the
NFLPool Player team chooses the Oakland Raiders for the AFC
Wildcard #1, they can earn points if the Oakland Raiders finish
in the Wildcard 1 or Wildcard 2 spot.  This is the only category
where this applies.

The tiebreaker pick needs to be updated for the 2017 season and have
two variables (to be determined).

