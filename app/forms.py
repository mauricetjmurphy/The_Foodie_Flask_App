from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, FileField, DateTimeField, FieldList, FormField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError, InputRequired
from app.models import User
from app import mongo
from flask_login import current_user
from mongoengine import ListField

#Creating the form classes
class LoginForm(FlaskForm):
    email = StringField("Email",  validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired("Please enter your email address."), Email("This field requires a valid email address")])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=30)])
    confirm_password =  PasswordField("Confirm Password", validators=[DataRequired(), Length(min=6, max=30), EqualTo("password")])
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    submit = SubmitField("Register Now")

    #Email validation. Checks if the inputted email has already been used
    def validate_email(self, email):
        user = mongo.db.user.find_one_or_404({"email": email.data})
        if user:
            raise ValidationError("Email is already in use. Please try another one.")
    

class IngredientsForm(FlaskForm):
        ingredient = StringField()

class DirectionsForm(FlaskForm):
    direction = TextAreaField()

class RecipeForm(FlaskForm):
    recipe_title = StringField("Name", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired(), Length(min=50)])
    dishImageURL = StringField("Image URL")
    ingredients  = ListField(StringField())
    directions  = ListField(StringField())
    submit = SubmitField("Upload Recipe")

class UpdateAccountForm(FlaskForm):
    first_name = StringField("First Name", validators=[])
    last_name = StringField("Last Name", validators=[])
    imageURL = FileField("Image URL", validators=[FileAllowed(["jpg", "png"])])
    submit = SubmitField("Update")

    def validate_first_name(self, first_name):
        if first_name.data != current_user.first_name:
            user = User.objects(first_name=first_name.data).first()
            if user:
                raise ValidationError("Please enter a new name")

    def validate_last_name(self, last_name):
        if last_name.data != current_user.last_name:
            user = User.objects(last_name=last_name.data).first()
            if user:
                raise ValidationError("Please enter a new name")

class PostForm(FlaskForm):
    full_name = StringField("Name", validators=[DataRequired()])
    content = TextAreaField("Ingredients", validators=[DataRequired()])
    submit_post = SubmitField("Post Comment")