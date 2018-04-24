########################
Managing NFLPool Players
########################

NFLPool Player Management
-------------------------

From the **Admin** page, you can view all active accounts for everyone who has ever created an account in NFLPool.
Under the **Account Management** header on the **Admin** page, click *View All Accounts* link located at
``/admin/account-list``.  This will show you a list of rows including the NFLPool player's name, email address,
when they created their account and their Twitter handle (which is optional)

Update League Fees
------------------

From the **Admin** page, you can update if a player has paid the annual league fee (if your league has one).
Under the **Account Management** header on the **Admin** page, click the link for
*Update players who have paid for the current season.* located at ``admin/update-paid``.

This page will display a drop down menu of all player accounts.  Choose the account you wish to mark as paid from
the drop down menu and press **Submit**.

.. note::

   When you update to a new season, the ``paid`` column in the ``Account`` table is reset each season to 0.  0 equals
   the player has not paid yet and when you press **Submit** above, it will change it to a 1 to mark the player as paid.


