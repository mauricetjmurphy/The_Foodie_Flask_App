# Import the required modules
from flask import Flask
from app.config import Config
from flask_mongoengine import MongoEngine
from flask_pymongo import PyMongo
from flask_login import LoginManager

# Instantiate the flask app object
app = Flask(__name__)
# Configure the app object using the config class
app.config.from_object(Config)

# Instantiate the mongo engine object
db = MongoEngine()
db.init_app(app)

# Specifing the URI for pymongo
app.config["MONGO_URI"] = "mongodb://localhost:27017/Recipe_App"
# Instantiate the PyMongo object
mongo = PyMongo(app)

# Instantiate the login manager object
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# Import poutes below the app instantiation to prevent circular imports
from app import routes