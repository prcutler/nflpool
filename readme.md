# NFLPool

NFLPool is hosted at [nflpool.xyz](https://www.nflpool.xyz).

NFLPool is a variation of [MLBPool](http://mlbpool2.com).
Unlike fantasy football, players make their picks once, before the season starts.  Players don't have to worry
about getting their picks in every week or micro managing their team. Before the NFL season begins, players choose
the teams they believe will win and lose each division; wildcard winners; and which players will lead in certain
offensive and defensive statistics.  Points are assigned to each category and the player who has the most points 
at the end of the NFL season after week 17 wins.  Unlike MLBPool2, players do not have the ability to change 
their picks at the halfway point of the season.  If you make a unique pick - the only person to choose a player 
or team in a given category - you earn double points for that pick.

## nflpool application

The NFLPool application is written in Python 3 and uses statistics from [MySportsFeeds](http://mysportsfeeds.com/)
who offer free developer access for non-commercial purposes.  You will need to sign
up for a MySportsFeed account to use the application.  The nflpool app uses the JSON feed from MySportsFeeds for 
all statistics.

NFLPool is using the [Pyramid](https://www.trypyramid.com) framework using nginx.  I use DigitalOcean running
Fedora 26 as my server.

For for more information on the league or rules, [visit the website](http://mlbpool2.com/rules/nfl-pool-rules/).

The nflpool application is licensed using the GNU GPL v3.0.

## Requirements
* nflpool is under active development and these are subject to change
* Python 3.5.2+
* SQLite
* SQLAlchemy 1.13
* Pyramid 1.9
* [MySportsFeeds](https://www.mysportsfeeds.com) account.


## Installation

1. Create an account with [MySportsFeeds](https://www.mysportsfeeds.com).
2. Edit the `secret.config.py` file and enter your MySportsFeeds username and password.  Enter the email
 address for the administrator.  Save this file as `secret.py`.
3. More soon after the new app running Pyramid is deployed.

## Contributing
This is my first ever Python application and I'm sure the code is ugly, but I'm learning.
Pull requests welcome!

## Credits

I started learning Python in early 2016 as a hobby with a goal of building the scoring automation for NFLPool 
and MLBPool2 instead of having to calculate each player's score manually.

I would not have learned Python without the help of:

* [Python for Everyone on Coursera](https://www.coursera.org/learn/python) by Dr. Charles Severance, 
which taught me the basic fundamentals of Python.
* [Talk Python Training by Michael Kennedy](https://training.talkpython.fm/), host of the most popular Python 
podcast, [Talk Python](http://talkpython.fm/). His courses were key in the development of this website and I was 
able to apply my Python knowledge thanks to the following courses:
  * [Python Jumpstart by Building 10 Apps](https://training.talkpython.fm/courses/explore_python_jumpstart/python-language-jumpstart-building-10-apps)
  * [Python for Entrepreneurs](https://training.talkpython.fm/courses/explore_entrepreneurs/python-for-entrepreneurs-build-and-launch-your-online-business)
  * [Consuming HTTP Services in Python](https://training.talkpython.fm/courses/details/consuming-http-and-soap-services-in-python-with-json-xml-and-screen-scraping)
  * [MongoDB for Python for Developers](https://training.talkpython.fm/courses/details/mongodb-for-python-for-developers-featuring-orm-odm-mongoengine)

* Lastly, and most importantly, my wife, who has years of programming experience and put up
                        with all of my stupid questions.

