from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from app import  col_user
from mongoengine import ListField

#Creating the login form class
class LoginForm(FlaskForm):
    email = StringField("Email",  validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

#Creating the registration form class
class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired("Please enter your email address."), Email("This field requires a valid email address")])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    confirm_password =  PasswordField("Confirm Password", validators=[DataRequired(), Length(min=6), EqualTo("password")])
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    submit = SubmitField("Register Now")

    #Email validation. Checks if the inputted email has already been used
    def validate_email(self, email):
        user = col_user.find_one({"email": email.data})
        if user:
            raise ValidationError("Email is already in use. Please try another one.")
    

#Creating the recipe form class
class RecipeForm(FlaskForm):
    recipe_title = StringField("Name", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired(), Length(min=50)])
    dishImageURL = StringField("Image URL")
    ingredients  = ListField(StringField())
    directions  = ListField(StringField())
    submit = SubmitField("Upload Recipe")

#Creating the update account form class
class UpdateAccountForm(FlaskForm):
    first_name = StringField("First Name", validators=[])
    last_name = StringField("Last Name", validators=[])
    imageURL = FileField("Image URL", validators=[FileAllowed(["jpg", "png"])])
    submit = SubmitField("Update")

#Creating the post form class
class PostForm(FlaskForm):
    full_name = StringField("Name", validators=[DataRequired()])
    content = TextAreaField("Ingredients", validators=[DataRequired()])
    submit_post = SubmitField("Post Comment")