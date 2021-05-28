import unittest
from app import app, db, mongo
from flask import request, jsonify, session
from flask_paginate import Pagination
import pymongo
from datetime import datetime
from PIL import Image
import secrets
import os
from flask import render_template, url_for, request, json, Response, flash, redirect, session, abort
from app.models import User, Recipe, Post, RecipePost
from app.forms import LoginForm, RegisterForm, RecipeForm, UpdateAccountForm
from flask_login import login_user, current_user, logout_user, login_required
from flask_restplus import Resource

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

#This function is used to find what page number the user is currently on in order to help paginate list of results.        
def get_page():
    return request.args.get('page', 1, type=int) 

#This function will take the query, page number the user is currently on and the 
#number of results wanted per page and slice the list of query results accordingly.
def paginate_list(query, page_number, per_page):
    array = [item for item in query]
    paginated_array = array[((page_number*per_page)-per_page):(page_number*per_page)]
    return paginated_array

@app.route("/")
@app.route("/index")
def index():
    page = get_page()

    recipes = mongo.db.recipe.find().sort('recipe_id', pymongo.DESCENDING)
    pagination = Pagination(per_page= 6, page=page, total=recipes.count(), record_name='recipes')
    recipe_list = paginate_list(recipes, page, 6)

    return render_template('index.html', index=True, recipeData=recipe_list, pagination=pagination)


@app.route("/contact")

def contact():
    
    return render_template('contact.html', contact=True)


@app.route("/about")

def about():

    return render_template('about.html', about=True)

@app.route("/category/<category>")
@login_required
def category(category):
    dish_category = Recipe.objects(category=category)
    
    page = get_page()
    pagination = Pagination(per_page= 12, page=page, total=dish_category.count(), record_name='recipes')
    page_list = paginate_list(dish_category, page, 12)

    return render_template('category.html', about=True, category=category, dish_category=dish_category, pageData=page_list, pagination=pagination)

@app.route("/recipe/<int:recipe_id>", methods=["GET", "POST"])
def recipe(recipe_id):

    recipe = Recipe.objects(recipe_id=recipe_id).get_or_404()
    return render_template('recipe.html', about=True, recipe=recipe)


@app.route("/recipe/new", methods=["GET", "POST"])

def new_recipe():

    return render_template('new_recipe.html', about=True)



def save_image(form_image):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_image.filename)
    image_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/images/profile-images', image_fn )

    output_size = (125, 125)
    i = Image.open(form_image)
    i.thumbnail(output_size)
    i.save(picture_path)

    return image_fn

@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    imageURL = url_for('static', filename="images/" + current_user.imageURL)
    user = current_user
    print(current_user.user_id)
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.imageURL.data:
            picture_file= save_image(form.imageURL.data)
            current_user.imageURL = picture_file
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        
        current_user.save()
        flash('Your account has been updated', 'success')
        return redirect(url_for('account'))
    elif request.method == "GET":
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
  
    return render_template('account.html',  form=form, imageURL=imageURL, user=user)
