

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

### Point Values

Each pick a player makes can be worth up to three different
point values.  If a player were to pick Aaron Rodgers as the
NFL's Passing Yards Leader, if Aaron Rodgers was in first place
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

```[cutler]