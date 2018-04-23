#####################################
NFLPool Installation and Requirements
#####################################

NFLPool Requirements
####################

NFLPool requires Python 3.6 or higher, Pyramid 1.9 and SQLite.  NFLPool uses the following Python modules:

- Passlib (for hashing user passwords)
- Pendulum (for date and datetime management)
- Pyramid Handlers
- Pytest (for testing)
- Requests
- Rollbar (for error reporting)
- Sphinx (for documentation)
- SQLAlchemy (database ORM)

Third Party Requirements
########################

NFPool requires the use of four third party services including `MySportsFeeds`_ for NFL statistics,
`Mailjet`_ (or Amazon SES) for email integration for user registration and password resets,
`Rollbar`_ for application error reporting, and `Slack`_ for administrative messaging.

MySportsFeeds
-------------

`MySportsFeeds`_ offers competitive pricing for commercial customers for sports statistics including the NFL, NHL,
NBA and MLB.  MySportsFeeds also offers free use for developers and non-commercial customers for past seasons, and a
`Patreon`_ for as low as $1 / month for post-game statistics (which is the minimum you will need for NFLPool).  You
will need to contact `MySportsFeeds`_ to finish creating an account from the "Contact Us" page on their website.

Email
-----

You will need a third party service to integrate email into NFLPool.  Email integration is required for user
registration and password resets.  NFLPool currently uses `Mailjet`_ and could be replaced by
`Amazon Simple Email Service`_ which is covered later in installation.


Error Reporting with Rollbar
----------------------------

`Rollbar`_ is used for error reporting.  Visit the `Rollbar`_ website to create and account and obtain your API key.
If you are using Github, you can link it with your Github repository and Rollbar will automatically create a new
issue for you in your Github repo when an error is reported.  Rollbar can also be integrated with Slack to message
you with errors.  Both email and / or Slack are helpful in case your application has an error or crashes.

Slack
-----

`Slack`_ is used via a bot that messages your Slack channel when a new user registers or submits their picks for
the season. You will need to create a `Slack app`_ with an incoming webhook and the webhook URL.

If you don't want to use Slack, it should be fairly simple to remove the feature, which is covered later in the
installation documentation.

Installation
############

You will need to rename three files.  In the root of your Pyramid application, rename ``development-example.ini``
and ``production-example.ini`` to ``development.ini`` and ``production.ini``.  In the ``data`` directory rename
``secret-config.py`` to ``secret.py``.

Pyramid Configuration
---------------------

In the ``development.ini`` and ``production.ini`` you will need to:

- Set the mode (``dev`` or ``prod``).  Dev mode will disable emails from sending.

- Mail server: Depending if you're using Mailjet or Amazon SES, enter your username, password, server and port information for your email service.

- Logging settings: Enter the name of the logfile you wish to create and the relative path.  By default, the logfile is saved in the root directory of your Pyramid application.

- Rollbar: Enter your Rollbar API token, the environment (dev or prod) and if using Git, which branch (default is master).

Application Configuration
-------------------------

In the ``data`` directory, configure your application settings in ``secret.py``.

Enter your MySportsFeeds credentials:

- msf_username = 'yourusername'

- msf_pw = 'yourpassword'

.. note::  MySportsFeeds currently uses HTTPAuth Basic for user authentication.  In 2018, MySportsFeeds will be releasing the 2.0 version of their API which will be moving to a token based authentication.


- su_email = 'administrator email address'

- slack_webhook_url = 'your Slack webhook URL'

To disable Slack, comment out the ``slack_webhook_url``.  In the ``controllers`` directory, comment out
all methods of ``message`` and ``SlackService`` in the ``account_controller.py`` and ``picks_controller.py`` files.

Application Installation
------------------------

Create a Python virtual environment.  Run the ``setup.py`` file to install all necessary Python modules and start
the Pyramid server.

.. note:: Installing a Python virtual environment and starting the Pyramid application are out of scope for NFLPool documentation.  Visit the `Pyramid documentation`_ for more information.

.. _`Rollbar`: https://www.rollbar.com
.. _`MySportsFeeds`: https://www.mysportsfeeds.com
.. _`Mailjet`: https://www.mailjet.com
.. _`Slack`: https://www.slack.com
.. _`Patreon`: https://www.patreon.com/mysportsfeeds
.. _`Amazon Simple Email Service`: https://aws.amazon.com/ses/
.. _`Slack app`: https://api.slack.com/slack-apps
.. _`Pyramid documentation`: https://docs.pylonsproject.org/projects/pyramid/en/1.9-branch/narr/install.html#installing-chapter
