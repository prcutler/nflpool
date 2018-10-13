#############
Initial Setup
#############

First Time Setup
================

Creating the Administrator Account
----------------------------------

After installing the NFLPool Pyramid application and running it, click on ``Register`` from the home page and
create an account with the email address you used in the ``secret.py`` configuration file.  This will give you
administrative access to NFLPool at your domain and add ``/admin`` to the URL to access the **Admin** page.

New Installation
----------------

NFLPool will check if the database is empty when loading the ``admin`` page and direct you through installation,
including:

- Create a season
- Update the database with needed information
- Import active NFL players

New Season Creation
-------------------

You will need to enter the year for the season you are creating, such as 2018 in the first field.  The new
season will be created and pull the first game information including the date, time and teams playing from
MySportsFeeds.  This data is stored in the SeasonInfo table.  The season year is used in all API calls to MySportsFeeds,
including the next section.

Database Tables
---------------

NFLPool will then use the MySportsFeeds API to create the following tables:

- ConferenceInfo: Two columns - 0 and 1 for AFC and NFC respectively.
- DivisionInfo: Four columns - 0-4 for East, North, South and West for the four divisions.
- PickTypes: Two columns of ten rows for each of the different kinds of points available for each category.  Note that Type 2 is not used.
- PickTypePoints: Four columns of 21 rows.  Columns include a primary key, the ``pick_type_id`` that maches the ``PickTypes`` table and the available points for each kind of pick depending on the place (typically first, second or third place).
- TeamInfo: This table is created by calling the MySportsFeed API and getting the team information for each team, including the team name, city, team abbreviation and their conference and division ID.

You will then be redirected to the last step.

Update NFL Player Information
-----------------------------

Lastly, you will be redirected to add all the active NFL Players to the database in the
``ActiveNFLPlayers`` table.  Press the **Go** button and NFLPool will use the MySportsFeed API to import all
active NFL players, including their first name, last name, position, Player ID (from MySportsFeeds), position, the
season year and a primary key.

Congratulations!  Your NFLPool players are ready to register their accounts and make their picks for the new season.


