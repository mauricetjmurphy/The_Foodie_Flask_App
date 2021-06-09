
from app import  login_manager, mdb, col_user
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


@login_manager.user_loader
def load_user(email):

    return  User(email=email)

# Pass to document object to the class  to allow the wtf forms directive to create fields
class User(mdb.Document,UserMixin):
    user_id = mdb.IntField(unique = True)
    first_name = mdb.StringField(max_length=50)
    last_name = mdb.StringField(max_length=50)
    email = mdb.StringField(max_length=30, unique=True)
    password = mdb.StringField()
    imageURL = mdb.StringField(max_length=300, default="user.png")

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

    # def set_password(self, password):
    #     self.password = generate_password_hash(password)

    # def check_password(self, password):
    #     return check_password_hash(self.password, password)

    

class Recipe(mdb.Document): 
    recipe_id = mdb.IntField(unique = True)
    recipe_title = mdb.StringField(max_length=50)
    description = mdb.StringField()
    ingredients = mdb.ListField(mdb.StringField())
    directions = mdb.ListField(mdb.StringField())
    dishImageURL = mdb.StringField(max_length=300)
    category = mdb.StringField(default="Unassigned")
    author = mdb.StringField()
    date_added = mdb.DateTimeField(default=datetime.utcnow)
   
class Post(mdb.Document):
    post_id = mdb.IntField(unique = True)
    full_name = mdb.StringField(max_length=50)
    content = mdb.StringField()
    date_added = mdb.DateTimeField(default=datetime.utcnow)
    
# This a join table to link the posts to a recipe
class RecipePost(mdb.Document):
    recipe_id = mdb.IntField()
    post_id = mdb.IntField()