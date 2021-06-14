# Import the required modules
from flask import Flask
from app.config import Config
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

# Instantiate the flask app object
app = Flask(__name__)
app.config.from_object(Config)

# Instantiate the mongo engine object
mdb = MongoEngine()
mdb.init_app(app)

# Instantiate the mongo client object, datebase and collections
cluster = MongoClient("mongodb://admin:adminpassword@recipeapp-shard-00-00.f09a9.mongodb.net:27017,recipeapp-shard-00-01.f09a9.mongodb.net:27017,recipeapp-shard-00-02.f09a9.mongodb.net:27017/Recipes?ssl=true&replicaSet=atlas-hhj5sz-shard-0&authSource=admin&retryWrites=true&w=majority")
db = cluster["Recipes"]
col_recipe = db["recipe"]
col_user = db['user']
col_post = db['post']
col_recipePost = db['recipePost']

# Instantiate the login manager object
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# Import poutes below the app instantiation to prevent circular imports
from app import routes