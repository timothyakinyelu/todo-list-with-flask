# TODO-LIST
## A simple task management App written with Flask 

#### Create a .env file and fill the columns
    FLASK_APP=application
    FLASK_ENV=development
    DEBUG=True
    APP_SETTINGS=application.config.DevelopmentConfig
    DATABASE_URI=sqlite:///db.sqlite
    TEST_DATABASE_URI=sqlite:///test.sqlite

### Run Command:
    pipenv install #this is if you are using a virtual environment if not "pip install"
    flask run

### To create the sqlite db, in your terminal run:
    The sqlite db will be created when you run the application.
