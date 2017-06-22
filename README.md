# Facebook scraper

Use this code to scrape the text of timeline posts of Facebook friends. After cloning and cd'ing into this repo, do the following:

* Create and activate a virtualenv using the following commands:
```
virtualenv env
source env/bin/activate
```

* Install all dependencies using pip.

* Enter your Facebook login and password in the file "facebook.py" where indicated.

* Run the command "python facebook.py" with the username of the timeline you are scraping. Like this:
```
python facebook.py baricks > baricks.txt
```
