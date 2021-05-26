import os

#Config object to store to store all config settings for the app
class Config(object):
    SECRET_KEY =  os.environ.get('SECRET_KEY') 
    
    MONGODB_SETTINGS = {"db" : "Recipe_App"}