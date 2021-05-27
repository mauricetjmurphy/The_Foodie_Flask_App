from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, FileField, DateTimeField, FieldList, FormField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from app.models import User
from app import mongo
from flask_login import current_user

class LoginForm(FlaskForm):
    email = StringField("Email",  validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=30)])
    confirm_password =  PasswordField("Confirm Password", validators=[DataRequired(), Length(min=6, max=30), EqualTo("password")])
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    submit = SubmitField("Register Now")

    

class IngredientsForm(FlaskForm):
        ingredient = StringField()

class DirectionsForm(FlaskForm):
    direction = TextAreaField()

class RecipeForm(FlaskForm):
    recipe_title = StringField("Name", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired(), Length(min=50)])
    ingredients  = FieldList(FormField(IngredientsForm), min_entries=20, max_entries=20)
    directions  = FieldList(FormField(DirectionsForm), min_entries=10, max_entries=20)
    dishImageURL = StringField("Image URL")
    submit = SubmitField("Upload Recipe")
