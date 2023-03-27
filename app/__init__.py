from flask import Flask
#import the config class from the config module that has the app configurations like SECRET_KEY, ETC
from config import Config
#IMPORT THE CLASSES FROM FLASK-SQLALCHEMY
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager




app = Flask(__name__)
app.config.from_object(Config)



#CREATE AN INSTANCE OF THE SQLALCHEMY CLASS TO CONNECT APP TO THE DATABASE
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)



#import all of the routes from the route file into the current package
from app import routes, models

