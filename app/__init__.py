from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
import secrets
from datetime import timedelta

secret_key =  "5AD9A0CB517457F7"
app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = app.config['SECRET_KEY']
app.config['JWT_EXPIRATION_DELTA'] = timedelta(hours=1)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)