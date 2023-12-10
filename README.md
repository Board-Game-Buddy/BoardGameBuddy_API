# BoardGameBuddy API

## About
BoardGameBuddy API serves as a microserves, housing the user databases. The `users` table holds the user's name, email, and profile picture (stored as an image url). The `userboardgame` table functions to hold the user's favorite boardgames and holds the user's ID as a foreign-key and the boardgame ID. 

This API includes endpoints for the following functionality: 
- create new users
- get all users 
- get a specific user with user data
- edit a user's data
- delete a user
- add a user's favorite board game
- get all user's favorite board games
- delete a user's favorite board game

This API consumes from a custom made BoardGameBuddy API found [HERE](https://github.com/Board-Game-Buddy/board-game-geek-data).

## Built with: 
- [Python 3.12.0](https://docs.python.org/3/)
- [Django 4.2.7](https://docs.djangoproject.com/en/5.0/intro/install/)
- [dj-database-url - 2.1.0](https://gist.github.com/jbothma/8a9a30399c2091d89763bff0a1952da4)
- [django-cors-headers - 4.3.1](https://github.com/adamchainz/django-cors-headers/tree/main)
- [djangorestframework - 3.14.0](https://www.django-rest-framework.org/)
- [gunicorn - 21.0.1](https://docs.gunicorn.org/en/stable/settings.html)
- [psycopg2 & psycopg2-binary - 2.9.9](https://www.psycopg.org/docs/install.html)
- [requests - 2.31.0](https://requests.readthedocs.io/en/latest/)
- [sqlparse - 0.4.4](https://sqlparse.readthedocs.io/en/latest/)
- [urllib3 - 2.1.0](https://urllib3.readthedocs.io/en/stable/)
- [virtualenv - 20.25.0](https://virtualenv.pypa.io/en/latest/)

## How to set up:
1. Install `virtualenv`
```
  $ pip3 install virtualenv
```
2. CD into the project and create a virtual environment

``` 
  $ cd boardgamebuddy_api
  $ python3 -m venv .venv
```

3. Activate your virtual environment

    On macOS and Linux:
```
  $ source .venv/bin/activate
```

      On Windows:
```
  $ env\Scripts\activate
```
4. Install all dependencies:
```
  $ pip install -r requirements.txt
```
## API Usage:

This App uses: 
- [board-game-geek-data](https://github.com/Board-Game-Buddy/board-game-geek-data)


## How to Run the test Suite: 

## Collaborators: 
- Lane Bretschneider | [LinkedIn](https://www.linkedin.com/in/lanebretschneider/)
- Reed Hillmar | [LinkedIn](https://www.linkedin.com/in/reed-hillmar/)
- Connor Richmond | [LinkedIn](https://www.linkedin.com/in/corichmond/)
- Noelle Hemphill | [LinkedIn](https://www.linkedin.com/in/noelle-hemphill/)