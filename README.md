# fuel-log-app
Python web application to log car refuelings.

Django + PostgreSQL + Heroku

# Deployment
This application was deployed with Heroku, check the link:
https://fuel-log-app.herokuapp.com/

You can <b>register</b> or <b>login</b> as a test user:
* login: testuser
* password: testpass1

# Application mission
This application will help you to keep a log of your refuelings.  
It will remind you when you last time refueled your car and at which gas stations. 
You will be also able to notice changes in the fuel price.

# Inspiration
This application is based on YT Tutorial by Dennis Ivy:

https://www.youtube.com/watch?v=llbtoQTt4qw&ab_channel=DennisIvy

# How to run app locally?

To run app in local environment, use below commands:

* `pip install virtualenv`
* `virtualenv “name as you like”`
* `source env/bin/activate`
* `pip install django`
* `pip install -r requirement.txt`
* `python manage.py runserver`

You will need to add connection to your local database or change database settings (in file settings.py).
