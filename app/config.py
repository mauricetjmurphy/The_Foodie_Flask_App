from dotenv import load_dotenv
import os

load_dotenv()

#Config object to store to staore all config settings for the app
class Config(object):

    # Set Flask config variables
    FLASK_ENV = 'production'
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    
    # Specifing the URI 
    MONGODB_SETTINGS = {
        "db": "Recipes",
        'username':'admin',
        'password':'adminpassword'
        }
    MONGO_URI = "mongodb://admin:adminpassword@recipeapp-shard-00-00.f09a9.mongodb.net:27017,recipeapp-shard-00-01.f09a9.mongodb.net:27017,recipeapp-shard-00-02.f09a9.mongodb.net:27017/Recipes?ssl=true&replicaSet=atlas-hhj5sz-shard-0&authSource=admin&retryWrites=true&w=majority"
    SECRET_KEY = os.getenv('SECRET_KEY')
    