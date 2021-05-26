# Import the required modules
from flask import Flask
from app.config import Config
from flask_mongoengine import MongoEngine

# Instantiate the flask app object
app = Flask(__name__)
# Configure the app object using the config class
app.config.from_object(Config)

# Instantiate the mongo engine object
db = MongoEngine()
db.init_app(app)

# Import poutes below the app instantiation to prevent circular imports
from app import routes