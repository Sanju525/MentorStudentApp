
# Mentor Student App
This project is based on `Django` a Python-based free and open-source web framework that follows the model-view-controller architectural pattern, dealing with Student Accounts, Attendance, MarksSubmission, and Notification functionalities for students done by mentor.

[Deployed on Heroku](https://mentorstudentapp.herokuapp.com)

## Creating Database tables
In this project we will be using `MyMentor` app and `MyStudent` app for creating database tables using `models.py` file from both applications.
>> To create tables use the following commands
```
python manage.py makemigrations
python manage.py migrate
```
This will create the tables in the DATABASE using the database_engine defined in `settings.py` file in MyProject directory.

