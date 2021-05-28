from app import db, login_manager, mongo
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(email):

    return User.objects.get(email=email)

# Pass to document object to the class  to allow the wtf forms directive to create fields
class User(db.Document, UserMixin):
    user_id = db.IntField(unique = True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
    email = db.StringField(max_length=30, unique=True)
    password = db.StringField()
    imageURL = db.StringField(max_length=300, default="user.png")

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

class Recipe(db.Document): 
    recipe_id = db.IntField(unique = True)
    recipe_title = db.StringField(max_length=50)
    description = db.StringField()
    ingredients = db.ListField(db.StringField())
    directions = db.ListField(db.StringField())
    dishImageURL = db.StringField(max_length=300)
    category = db.StringField(default="Unassigned")
    author = db.StringField()
    date_added = db.DateTimeField(default=datetime.utcnow)
   
class Post(db.Document):
    post_id = db.IntField(unique = True)
    full_name = db.StringField(max_length=50)
    content = db.StringField()
    date_added = db.DateTimeField(default=datetime.utcnow)
    
# This a join table to link the posts to a recipe
class RecipePost(db.Document):
    recipe_id = db.IntField()
    post_id = db.IntField()