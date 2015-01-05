fyn-shorten
===========

Requirements: Python 2.7, Django 1.7.2, wget 2.2

This URL shortener shortens any URL based on a dictionary of words matching the URL components.
So when other URL shorteners give you completely random URLs, this one will try to give you some sensical alias for your URL.

*For loading the wordbank, we have created and registered a django command called wordbank.*


Having said that, let's dive deep.

Get Going
=========

*You can skip steps 1 & 2 and refer to step 5, if you want to automatically download the sqlite file from web.*

1. Download the db.sqlite3 file from the repository https://github.com/akshatam/fyn-db.
2. Copy the db.sqlite3 into the directory of the code, fyn-shorten/tinyurl/
3. cd into the repo-home.
4. Run python startServer.py, in case you want to reload the wordbank, pass the option -r or --reload.
5. In case you wish to automatically download the sqlite file, pass the option -a or --auto-db
  - Example: python startServer.py (Quickly starts server)
  - Example: python startServer.py -r (Takes a while to load the updates into the database.)
  - Example: python startServer.py -a (Automatically downloads the file db.sqlite3)

Access
======

Once the server is up and running, access the application at server-ip:8000/
