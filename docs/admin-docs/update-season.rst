########################
Updating to a New Season
########################

New Season Update
-----------------

Similar to the first time installation, you will need to update the season information each year.  From the **Admin**
page, choose the link under the **Update to a New Season** header located at ``admin/new_season``.
Enter the year for the season you are creating, such as 2018.  The first game information, including the date and time
and teams playing will be automatically filled from the MySportsFeeds API.  This will update the
``SeasonInfo`` table and this information is overridden each year when the administrator updates to a new season.

Update NFL Player Information
-----------------------------

After updating to the new season, you will be redirected to add all the active NFL Players to the database in the
``ActiveNFLPlayers`` table.  Press the **Go** button and NFLPool will use the MySportsFeed API to import all
active NFL players, including their first name, last name, position, Player ID (from MySportsFeeds), position, the
season year and a primary key.

.. note::

   When you update to a new season, the ``paid`` column in the ``Account`` table is reset each season to 0 resetting
   all players as not having paid the annual league fee for the new season (if you have a fee).

Congratulations!  Your NFLPool players are ready to make their picks for the new season.


