from pymongo import mongo_client
from app import db, login_manager, mongo, mone
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(email):

    return  User(email = email)

# Pass to document object to the class  to allow the wtf forms directive to create fields
class User(mone.Document):
    user_id = mone.IntField(unique = True)
    first_name = mone.StringField(max_length=50)
    last_name = mone.StringField(max_length=50)
    email = mone.StringField(max_length=30, unique=True)
    password = mone.StringField()
    imageURL = mone.StringField(max_length=300, default="user.png")

    def __repr__(self):
        return f"User('{self.user_id}', '{self.first_name}','{self.last_name}'),'{self.email}') '{self.imageURL}')"

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False  

    def set_password(self, password):
        self.password = generate_password_hash((password))

    def get_password(self, password):
        return check_password_hash(self.password, password)

class Recipe(mone.Document): 
    recipe_id = mone.IntField(unique = True)
    recipe_title = mone.StringField(max_length=50)
    description = mone.StringField()
    ingredients = mone.ListField(mone.StringField())
    directions = mone.ListField(mone.StringField())
    dishImageURL = mone.StringField(max_length=300)
    category = mone.StringField(default="Unassigned")
    author = mone.StringField()
    date_added = mone.DateTimeField(default=datetime.utcnow)
   
class Post(mone.Document):
    post_id = mone.IntField(unique = True)
    full_name = mone.StringField(max_length=50)
    content = mone.StringField()
    date_added = mone.DateTimeField(default=datetime.utcnow)
    
# This a join table to link the posts to a recipe
class RecipePost(mone.Document):
    recipe_id = mone.IntField()
    post_id = mone.IntField()