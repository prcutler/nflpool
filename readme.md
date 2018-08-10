[![Documentation Status](https://readthedocs.org/projects/nflpool/badge/?version=latest)](
http://nflpool.readthedocs.io/en/latest/?badge=latest)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Updates](https://pyup.io/repos/github/prcutler/nflpool/shield.svg)](https://pyup.io/repos/github/prcutler/nflpool/)
[![GitHub license](https://img.shields.io/github/license/prcutler/nflpool.svg)](https://github.com/prcutler/nflpool/blob/master/LICENSE)

# NFLPool

NFLPool is hosted at [nflpool.xyz](https://www.nflpool.xyz).

NFLPool is a variation of [MLBPool2](http://mlbpool2.com).
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
up for a MySportsFeed account to use the application.  The nflpool app uses JSON feeds from MySportsFeeds for 
all statistics.

NFLPool is uses the [Pyramid](https://www.trypyramid.com) Python web application framework.  
[nflpool.xyz](https://www.nflpool.xyz) is hosted on Digital Ocean running Fedora and nginx.

For for more information on the league or rules, [visit the website](http://mlbpool2.com/rules/nfl-pool-rules/).

The NFLPool application is licensed under the MIT license.

## Requirements
* NFLPool is under active development and these are subject to change
* Python 3.6+
* SQLite
* SQLAlchemy 1.2+
* Pyramid 1.9+
* [MySportsFeeds](https://www.mysportsfeeds.com) account.


## Documentation

NFLPool documentation is available on [ReadtheDocs](http://nflpool.readthedocs.io/en/latest/index.html), including 
an [Administrator's guide](http://nflpool.readthedocs.io/en/latest/admin-docs/index.html) to setting up NFLPool 
and updating it each season and a [User Guide](http://nflpool.readthedocs.io/en/latest/user-docs/index.html) for 
players.

## Contributing
NFLPool (and [MLBPool2](https://github.com/prcutler/mlbpool2)) are my first Python applications and I'm sure the
code is ugly in places - contributions welcome!  Please see the
[Code of Conduct](https://github.com/prcutler/nflpool/blob/master/CODE_OF_CONDUCT.md).

Imposter syndrome disclaimer: I want your help. No really, I do.

There might be a little voice inside that tells you you're not ready; that you need to do one more tutorial, 
or learn another framework, or write a few more blog posts before you can help me with this project.

I assure you, that's not the case.

While I don't have clear contributing guidelines at this time, please fork the repo and send me a pull request!  
I'm new to Python too, and I would love the help and learn how to make things better.

And you don't just have to write code. You can help out by writing documentation, tests, or even by giving 
feedback about NFLPool. (And yes, that includes giving feedback about the contribution guidelines.)

Thank you for contributing!

(Adapted from 
[Adrienne Lowe's Imposter Syndrome Disclaimer](https://github.com/adriennefriend/imposter-syndrome-disclaimer))

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

