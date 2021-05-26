# Import the required modules
from flask import Flask

# Instantiate the flask app object
app = Flask(__name__)

# Import poutes below the app instantiation to prevent circular imports
from app import routes