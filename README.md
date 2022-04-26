# TIGR MANAGR


MANAGR is a project management web app built in Flask.

This app is created in order to satisfy the Final Project from the Psychology and Design Thinking Course.

## Tech stack 

- Frontend : TailwindCSS
- Backend : Flask
- Database : Heroku Cloud Postgres
- API : (AUTH) Google OAuth

## Milestone 
<table>
    <tr>
        <th>Target</th>
        <th>Status</th>
    </tr>
    <tr>
        <td>Created table TODO</td>
        <td></td>
    </tr>
    <tr>
        <td>Created table BOARD</td>
        <td></td>
    </tr>
    <tr>
        <td>Created basic CRUD functionality</td>
        <td></td>
    </tr>
    <tr>
        <td>Setup Auth</td>
        <td>V</td>
    </tr>
    <tr>
        <td>Auth functionalities</td>
        <td></td>
    </tr>
</table>

## Getting Started

These instructions will give you a copy of the project up and running on
your local machine for development and testing purposes.

## Dependencies

- [Python3](www.python.org)
- [pip](https://pip.pypa.io/en/stable/installation/)
- Flask
- SQLAlchemy
- Authlib

## Installing

Clone the git repo by running :
```
$ git clone https://github.com/tigrplus/tigrmanagr.git
```

After the cloning is successful, go to the folder by running :
```
$ cd ~/tigrmanagr
```

If you don't have Flask, install Flask by running :
```
$ pip install Flask
```

If you don't have sqlalchemy, install it by running :
```
$ pip install SQLAlchemy 
```

If you don't have authlib, install it by running :
```
$ pip install Authlib
```

To start the app run the following :
```
$ flask run
```
If it doesn't work use this command :
```
$ python3 -m flask run
```

You should see this in your terminal/console :
```
* Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Go to your web browser of choice and open the following url :
```
http://127.0.0.1:5000/
```
