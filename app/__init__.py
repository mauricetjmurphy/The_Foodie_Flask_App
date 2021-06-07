# Import the required modules
from flask import Flask
from app.config import Config
from flask_mongoengine import MongoEngine
from flask_pymongo import PyMongo
from flask_login import LoginManager
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

# Instantiate the flask app object
app = Flask(__name__)
app.config.from_object(Config)

# Instantiate the mongo engine object
mone = MongoEngine()
mone.init_app(app)

cluster = MongoClient("mongodb://Maurice:<testpassword@recipeapp-shard-00-00.f09a9.mongodb.net:27017,recipeapp-shard-00-01.f09a9.mongodb.net:27017,recipeapp-shard-00-02.f09a9.mongodb.net:27017/Recipes?ssl=true&replicaSet=atlas-hhj5sz-shard-0&authSource=admin&retryWrites=true&w=majority")
db = cluster["Recipes"]


# Specifing the URI 
app.config["MONGO_URI"] = "mongodb://Maurice:testpassword@recipeapp-shard-00-00.f09a9.mongodb.net:27017,recipeapp-shard-00-01.f09a9.mongodb.net:27017,recipeapp-shard-00-02.f09a9.mongodb.net:27017/Recipes?ssl=true&replicaSet=atlas-hhj5sz-shard-0&authSource=admin&retryWrites=true&w=majority"
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Instantiate the PyMongo object
mongo = PyMongo(app)

# Instantiate the login manager object
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# Import poutes below the app instantiation to prevent circular imports
from app import routes