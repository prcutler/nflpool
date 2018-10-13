#############
Sending Email
#############

NFLPool sends a user an email after creating an account or when a user requests a password reset.

Changing the email settings
===========================

Due to the way the NFLPool application is built and integrated with 3rd party email services, email is hard coded.
You will need to update the links in two files in the ``nflpool\email`` directory:

- ``password_reset.html``: Replace all references to ``nflpool.xyz`` with your domain.  If you are using an image embedded in your email, you will also need to replace the URL ``http://paulcutler.org/files/trophy2.png`` with a link to where your image is hosted.

- ``welcome.html``: Replace all references to ``nflpool.xyz`` with your domain.  If you are using an image embedded in your email, you will also need to replace the URL ``http://paulcutler.org/files/trophy2.png`` with a link to where your image is hosted.
