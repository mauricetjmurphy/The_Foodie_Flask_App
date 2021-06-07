from wtforms.validators import Email
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
from app.forms import LoginForm, RegisterForm, RecipeForm, UpdateAccountForm, PostForm
from flask_login import login_user, current_user, logout_user, login_required

# Decorators (app routes)
# @app.route("/login", methods=["GET", "POST"])
# def login():
#     # Check if user is already logged in
#     if current_user.is_authenticated:
#         flash("User is already logged in!", "danger")
#         return redirect(url_for('index'))

#     # Assign the login form object to the form variable
#     form = LoginForm()
#     if form.validate_on_submit():
#         email = form.email.data
#         password = form.password.data
#         user = User(email = email)
#         print(user)
#         if user and user.get_password(password):
#             login_user(user, remember=False)
#             flash(f" {user.first_name}, you are successfully logged in!", 'success')
#             return redirect(url_for('index'))

#     return render_template('login.html', form=form)

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    
    # user = mongo.db.user.find()
    # user = User.objects().first()
    # user = User.select().where(User.email == email).first()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User(email = email)
        # user = db["user"].find({"email": email})
        print(user)

        if user:
            login_user(user)
            flash(f" {user.first_name}, you are successfully logged in!", 'success')
            return redirect(url_for("index"))
    return render_template("login.html", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
    
        user_id = db["user"].count()
        print(f"user_id: ------------{user_id}---------------")
        user_id += 1
        email = form.email.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        db["user"].insert_one({"email": email, "first_name": first_name, "last_name": last_name, "password": password})
        # User( email=email, first_name=first_name, last_name=last_name, password=password).save()
        # user.set_password(password)
        flash("You are successfully registered", "success")
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)


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
@login_required
def index():
    page = get_page()

    all_recipes = mongo.db.recipe.find().sort('recipe_id', pymongo.DESCENDING)
    recipes = mongo.db.recipe.find().sort('recipe_id', pymongo.DESCENDING)
    pagination = Pagination(per_page= 6, page=page, total=recipes.count(), record_name='recipes')
    recipe_list = paginate_list(recipes, page, 6)

    return render_template('index.html', index=True, all_recipes=all_recipes, recipeData=recipe_list, pagination=pagination)


@app.route("/contact")
@login_required
def contact():
    return render_template('contact.html', contact=True)


@app.route("/about")
@login_required
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

@app.route("/recipe/new", methods=["GET", "POST"])
# @login_required
def new_recipe():
    post_form = PostForm()
    form = RecipeForm()
    if form.validate_on_submit():
        recipe_id = Recipe.objects.count()
        recipe_id += 1
        recipe_title = form.recipe_title.data
        description = form.description.data
        
        ingredients = request.form.getlist('ingredient-field[]')
        directions = request.form.getlist('step-field[]')
        category = request.form.get('category')
        
        dishImageURL = form.dishImageURL.data
        author = current_user.email
        recipe = Recipe(recipe_id=recipe_id, recipe_title=recipe_title, description=description, ingredients=ingredients, directions=directions, category=category, dishImageURL=dishImageURL, author=author)
        recipe.save()
        flash("Another wonderful recipe added to your collection.", "success")
        return redirect(url_for('index'))
    return render_template("add_recipe.html", title='New Recipe', form=form, post_form=post_form,  login=True, legend='Add a new recipe')


@app.route("/recipe/<int:recipe_id>", methods=["GET", "POST"])
@login_required
def recipe(recipe_id):
    post_form = PostForm()
    if post_form.validate_on_submit():
        post_id = Post.objects.count()
        post_id += 1
        full_name = post_form.full_name.data
        content = post_form.content.data
        post = Post(post_id=post_id, full_name=full_name, content=content)
        post.save()
        recipePost = RecipePost(recipe_id=recipe_id, post_id=post_id)
        recipePost.save()

        flash('Your post has been added', 'success')
        return redirect(url_for('recipe', recipe_id=recipe_id))
        form.full_name.data = ''
        form.content.data = ''

    posts = list( Recipe.objects.aggregate(*[
        {
            '$lookup': {
                'from': 'recipe_post', 
                'localField': 'recipe_id', 
                'foreignField': 'recipe_id', 
                'as': 'r1'
            }
        }, {
            '$unwind': {
                'path': '$r1', 
                'includeArrayIndex': 'r1_id', 
                'preserveNullAndEmptyArrays': False
            }
        }, {
            '$lookup': {
                'from': 'post', 
                'localField': 'r1.post_id', 
                'foreignField': 'post_id', 
                'as': 'r2'
            }
        }, {
            '$unwind': {
                'path': '$r2', 
                'includeArrayIndex': 'string', 
                'preserveNullAndEmptyArrays': False
            }
        }, {
            '$match': {
                'recipe_id': recipe_id
            }
        }, {
            '$sort': {
                'recipe_id': 1
            }
        }
    ]))

    num_posts = len(posts)

    user=current_user
    recipe = Recipe.objects(recipe_id=recipe_id).get_or_404()
    return render_template('recipe.html', about=True, num_posts=num_posts, recipe=recipe, posts=posts, post_form=post_form, user=user)


@app.route("/recipe/<int:recipe_id>/update",  methods=["GET", "POST"])
@login_required
def update_recipe(recipe_id):
    recipe = Recipe.objects(recipe_id=recipe_id).get_or_404()
    if recipe.author != current_user.email:
        flash("Sorry you can't update a recipe that you havn't created!", "danger")
        return redirect(url_for('recipe', recipe_id=recipe_id))
    form = RecipeForm()
    # Add add fields that you want to update
    if form.validate_on_submit():
        recipe_title = form.recipe_title.data
        description = form.description.data

        ingredients = request.form.getlist('ingredient-field[]')
        directions = request.form.getlist('step-field[]')

        dishImageURL = form.dishImageURL.data
        category = request.form.get('category')
        author = current_user.email
        
        mongo.db.recipe.remove({"recipe_id": recipe_id})

        recipe = Recipe(recipe_id=recipe_id, recipe_title=recipe_title, description=description, ingredients=ingredients, directions=directions, dishImageURL=dishImageURL, category=category, author=author)
        recipe.save()

        flash("Your recipe has been updated!", 'success')
        return redirect(url_for('recipe', recipe_id=recipe_id))
    elif request.method == 'GET':
        form.recipe_title.data = recipe.recipe_title
        form.description.data =  recipe.description          
        form.dishImageURL.data = recipe.dishImageURL
    
    return render_template('update_recipe.html', about=True, recipe=recipe, form=form, legend='Update recipe')


@app.route("/recipe/<int:recipe_id>/delete",  methods=["POST"])
@login_required
def delete_recipe(recipe_id):
    recipe = Recipe.objects(recipe_id=recipe_id).first()
    if recipe.author != current_user.email:
        flash("Sorry you can't delete a recipe that you havn't created!", "danger")
        return redirect(url_for('recipe', recipe_id=recipe_id))
    mongo.db.recipe.remove({"recipe_id":recipe_id}, True)
    flash("Your recipe has been deleted!", 'success')
    return redirect(url_for('index'))


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

@app.route("/account/delete",  methods=['GET','POST'])
def delete_account():
    user_id = current_user.user_id
    logout_user()
    mongo.db.user.delete_one({"user_id": user_id})
    flash("Your account has been deleted!", 'success')
    return redirect(url_for('login'))

@app.route("/contact-form", methods=["GET", "POST"])
def contact_form():
    flash("Thank you for your message, we will be in touch as soon as we can!", 'success')
    return redirect(url_for('contact'))


# @ app.errorhandler(404)
# def not_found(error):
#     return render_template('errors/404.html'), 404


@ app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500