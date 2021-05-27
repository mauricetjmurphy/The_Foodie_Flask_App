from app import app, mongo, login_manager
from flask import render_template, url_for, request, json, Response, flash, redirect, session, abort
from flask_login import login_user, current_user, logout_user, login_required
from app.forms import LoginForm, RegisterForm
from app.models import User, Recipe, Post, RecipePost

# Decorators (app routes)
@app.route("/login", methods=["GET", "POST"])
def login():
    # Check if user is already logged in
    if current_user.is_authenticated:
            return redirect(url_for('index'))

    # Assign the login form object to the form variable
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

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_id = User.objects.count()
        user_id += 1
        email = form.email.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        user = User(user_id=user_id, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        flash("You are successfully registered", "success")
        return redirect(url_for('index'))

    return render_template('register.html', form=form, login=True)

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


@app.route("/recipe/<int:recipe_id>", methods=["GET", "POST"])
def recipe(recipe_id):

    recipe = Recipe.objects(recipe_id=recipe_id).get_or_404()
    return render_template('recipe.html', about=True, recipe=recipe)


@app.route("/recipe/new", methods=["GET", "POST"])

def new_recipe():

    return render_template('new_recipe.html', about=True)

@app.route("/account", methods=["GET", "POST"])

def account():

    return render_template('account.html', about=True)


@app.route("/category")

def category():

    return render_template('account.html', about=True)