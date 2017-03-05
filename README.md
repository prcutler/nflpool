# NFLPool

NFLPool is a variation of [MLBPool](http://mlbpool2.com).
Unlike fantasy football, players make their picks once, before the season starts.  Players don't have to worry
about getting their picks in every week or micro managing their team. Before the NFL season begins, players choose
the teams they believe will win and lose each division; wildcard winners; and which players will lead in certain
offensive and defensive statistics.  Points are assigned to each category and the player who has the most points at the end
of the NFL season after week 17 wins.  Unlike MLBPool2, players do not have the ability to change their picks at the halfway
point of the season.  If you make a unique picks - the only person to choose a player or team in a given category -
you earn double points for that pick.

## nflpool application

The NFLPool application is written in Python 3 and uses statistics from [MySportsFeeds](http://mysportsfeeds.com/)
who offer free developer access for non-commercial purposes.  You will need to sign
up for a MySportsFeed account to use the application.  The nflpool app uses the JSON feed from MySportsFeeds for all statistics.

This is my first ever Python applications and I'm sure the code is ugly, but I'm learning.
Pull requests welcome!

Future versions will include a web application to output the results
via JSON to be displayed on the web.

For for more information on the league or rules, [visit the website](http://mlbpool2.com/rules/nfl-pool-rules/).

The nflpool application is licensed using the GNU GPL v3.0.

##Requirements
* Python 3.5.2+
* SQLite3
* [MySportsFeeds](https://www.mysportsfeeds.com) account.

###Python modules
* requests
* json
* csv

