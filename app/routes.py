from flask import render_template, url_for, request, json, Response, flash, redirect, session, abort
from app import app
from app import app, mongo
from flask_login import login_user, current_user, logout_user, login_required
from app.forms import LoginForm, RegisterForm, RecipeForm, UpdateAccountForm, PostForm
from app.models import User, Recipe, Post, RecipePost

# Decorators (app routes)
@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/contact")

def contact():
    
    return render_template('contact.html', contact=True)


@app.route("/about")

def about():

    return render_template('about.html', about=True)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
            return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
       
        user = User.objects(email=email).first()
        session['user_id'] = user.user_id
        if user and user.get_password(password):
            login_user(user)
            flash(f" {user.first_name}, you are successfully logged in!", 'success')
            return redirect(url_for('index'))
  
        else:
            flash("Sorry something went wrong", "danger")
    return render_template('login.html', form=form, login=True)


@app.route("/recipe/new", methods=["GET", "POST"])

def new_recipe():

    return render_template('new_recipe.html', about=True)

@app.route("/account", methods=["GET", "POST"])

def account():

    return render_template('account.html', about=True)


@app.route("/category")

def category():

    return render_template('account.html', about=True)