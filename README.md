fyn-shorten
===========

Requirements: Python 2.7, Django 1.7.2

This URL shortener shortens any URL based on a dictionary of words matching the URL components.
So when other URL shorteners give you completely random URLs, this one will try to give you some sensical alias for your URL.

*For loading the wordbank, we have created and registered a django command called wordbank.*
** To use word bank you must first clean the words.txt, using python startServer.py from repo root. **

Having said that, let's dive deep.

Get Going
=========

1. Download the db.sqlite3 file from the repository https://github.com/akshatam/fyn-db.
2. Copy the db.sqlite3 into the directory of the code, fyn-shorten/tinyurl/
3. cd into the app directory, i.e. C:\...\> fyn-shorten\tinyurl\
4. For safety just do python manage.py migrate
5. Also just make sure full word list is loaded properly just do the following 
  - From repo root, execute c:...> python startServer.py
  - cd tinyurl
  - python manage.py wordbank
6.Run python manage.py runserver 0.0.0.0:8000

Access
======

Once the server is up and running, access the application at <server-ip>:8000/
