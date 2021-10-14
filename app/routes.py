from app import app, col_recipe, col_user, col_post, col_recipePost
from flask import request
from flask_paginate import Pagination
import pymongo
from datetime import datetime
from PIL import Image
import secrets
import os
import glob
from flask import render_template, url_for, request, flash, redirect
from app.models import User
from app.forms import LoginForm, RegisterForm, RecipeForm, UpdateAccountForm, PostForm
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash



# Decorators (app routes)
# Login route that provides the user a form to enter their credentials. They are checked against the database for authentication.
@app.route("/login", methods=["GET", "POST"])
def login():
    # Check if user is already logged in
    if current_user.is_authenticated:
        flash("User is already logged in!", "danger")
        return redirect(url_for('index'))

    # Assign the login form object to the form variable
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        user = User(email=email)
        u = col_user.find_one({"email" :email})

        #Checking hashed password
        if u and check_password_hash(u["password"], form.password.data):
            login_user(user)
            # Flash messaging to display success and warning messages to the user
            flash(f" {u['first_name']}, you are successfully logged in!", 'success')
            return redirect(url_for('index'))
        else:
            flash("Unsuccessful, please check username and password", 'danger')
            return redirect(url_for('login'))
    return render_template('login.html', form=form)


# Logout route to log the user out.
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


# Registration route. A form sends the users details to the database and Flask-login creates the user session.
@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
    
        email = form.email.data
        password_data = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        password = generate_password_hash(password_data)
        col_user.insert_one({ "email":email, "first_name":first_name, "last_name":last_name, "password":password, "imageURL": "user.png"})

        login_user(User(email=email))

        flash("You are successfully registered", "success")
        return redirect(url_for('index'))    
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

# Index route displays the homepage. Using two helper functions above with flask-paginate to paginate the recipe objects.
@app.route("/")
@app.route("/index")
 # The @login_required decorator ensures the user is logged in before being able to access this page.
def index():
    page = get_page()

    all_recipes = col_recipe.find().sort('_id', pymongo.DESCENDING)
    recipes = col_recipe.find().sort('_id', pymongo.DESCENDING)
    pagination = Pagination(per_page= 6, page=page, total=recipes.count(), record_name='recipes')
    recipe_list = paginate_list(recipes, page, 6)

    return render_template('index.html', index=True, all_recipes=all_recipes, recipeData=recipe_list, pagination=pagination)


# Contact route 
@app.route("/contact")
def contact():
    email=current_user.email
    user = col_user.find_one({"email": email})
    return render_template('contact.html', contact=True)


# About route
@app.route("/about")
def about():
    return render_template('about.html', about=True)

# Category route queries all recipes of a certain category, paginates them and display them in the template.
@app.route("/category/<category>")
def category(category):
    page = get_page()
    
    dish_category = col_recipe.find({"category": category})
    pagination = Pagination(per_page= 12, page=page, total=dish_category.count(), record_name='category_recipes')
    page_list = paginate_list(dish_category, page, 12)
    return render_template('category.html', about=True, category=category,  pageData=page_list, pagination=pagination, dish_category=dish_category)

# New recipe route contains a form for submitting new recipe data
@app.route("/recipe/new", methods=["GET", "POST"])
# @login_required
def new_recipe():
    post_form = PostForm()
    form = RecipeForm()
    
    if request.method == "POST":
        recipe_title = request.form.get('recipe_title')
        description = request.form.get('description')
        # Get list method is used to collect the list of dynamic form field data
        ingredients = request.form.getlist('ingredient-field[]')
        directions = request.form.getlist('step-field[]')
        category = request.form.get('category')
        
        dishImageURL = request.form.get('dishImageURL')
        author = current_user.email
        # datetime sets the current date and time
        d = datetime.now()

        col_recipe.insert_one({"recipe_id": "", "recipe_title":recipe_title, "description":description, "ingredients":ingredients, "directions":directions, "dishImageURL":dishImageURL, "category":category, "author":author, "date_added": d})
        recipe = col_recipe.find_one({"recipe_title":recipe_title})
        col_recipe.update_one({"recipe_title":recipe_title},  {"$set" : {"recipe_id": str(recipe["_id"])}})
        flash("Another wonderful recipe added to your collection.", "success")
        return redirect(url_for('index'))
    return render_template("add_recipe.html", title='New Recipe', form=form, post_form=post_form,  login=True, legend='Add a new recipe')


#Recipe route displays a selected recipe. Route template also includes a form for submitting posts.
@app.route("/recipe/<recipe_id>", methods=["GET", "POST"])
# @login_required
def recipe(recipe_id):
    post_form = PostForm()
    email=current_user.email
    user = col_user.find_one({"email": email})
    recipe = col_recipe.find_one({"recipe_id": recipe_id})

    if request.method == 'GET':
        post_form.full_name.data = user["first_name"] + " " + user["last_name"]

    if post_form.validate_on_submit():
        full_name = post_form.full_name.data
        content = post_form.content.data
        d = datetime.now()
        col_post.insert_one({"full_name":full_name, "content":content, "date_added": d})

        post = col_post.find_one({"content": content})
        col_post.update_one({"content": content}, { '$set': {"post_id": str(post["_id"])}})
        col_recipePost.insert_one({"recipe_id":recipe_id, "post_id": str(post["_id"])})

        flash('Your post has been added', 'success')
        return redirect(url_for('recipe', recipe_id=recipe_id))

    # MongoDB aggregatiuon filters and matches recipe using the  join collection recipePost
    posts = list(col_recipe.aggregate([
            {
                '$lookup': {
                    'from': 'recipePost', 
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
                    'preserveNullAndEmptyArrays': False
                }
            }, {
                '$match': {
                    'recipe_id': recipe_id
                }
            }, {
                '$sort': {
                    'post_id': 1
                }
            }
        ]))
    
    num_posts = len(list(posts))
    return render_template('recipe.html', about=True, recipe=recipe, user=user, post_form=post_form, posts=posts, num_posts=num_posts)

#Route for updating a recipe
@app.route("/recipe/<recipe_id>/update",  methods=["GET", "POST"])
# @login_required
def update_recipe(recipe_id):
    recipe = col_recipe.find_one({"recipe_id": recipe_id})
    if recipe["author"] != current_user.email:
        flash("Sorry you can't update a recipe that you have not created!", "danger")
        return redirect(url_for('recipe', recipe_id=recipe_id))
    form = RecipeForm()
    # Form for updating the recipe
    if request.method == "POST":
        recipe_title = request.form.get('recipe_title')
        description = request.form.get('description')
        # Get list method is used to collect the list of dynamic form field data
        ingredients = request.form.getlist('ingredient-field[]')
        directions = request.form.getlist('step-field[]')
        category = request.form.get('category')
        
        dishImageURL = request.form.get('dishImageURL')
        author = current_user.email
        # datetime sets the current date and time
        d = datetime.now()


        col_recipe.update_one({"recipe_id": recipe_id}, {"$set" : { "recipe_title":recipe_title, "description":description, "ingredients":ingredients, "directions":directions, "dishImageURL":dishImageURL, "category":category, "author":author, "date_added": d}})

        flash("Your recipe has been updated!", 'success')
        return redirect(url_for('recipe', recipe_id=recipe_id))
        # If its a get request the form will auto-fill the fields with the current data
    elif request.method == 'GET':
        
        form.recipe_title.data = recipe["recipe_title"]
        description =  recipe["description"]          
        dishImageURL = recipe["dishImageURL"]
    
    return render_template('update_recipe.html', about=True, recipe=recipe, form=form, legend='Update recipe')

#Route deletes the recipe from the database only if the current user is the author
@app.route("/recipe/<recipe_id>/delete",  methods=["POST"])
# @login_required
def delete_recipe(recipe_id):
    recipe = col_recipe.find_one({"recipe_id":recipe_id})
    if recipe["author"] != current_user.email:
        flash("Sorry you can't delete a recipe that you havn't created!", "danger")
        return redirect(url_for('recipe', recipe_id=recipe_id))
    col_recipe.remove({"recipe_id":recipe_id}, True)
    flash("Your recipe has been deleted!", 'success')
    return redirect(url_for('index'))

#Helper function to save image in local directory
def save_image(form_image):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_image.filename)
    image_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/images/profile-images', image_fn )
    
    #Using the PIL library to resize uploaded images
    output_size = (125, 125)
    i = Image.open(form_image)
    i.thumbnail(output_size)
    i.save(picture_path)

    return image_fn

# Account route. User can update their account details and profile imageß by submitting the update form
@app.route("/account", methods=["GET", "POST"])
# @login_required
def account():
    imageURL = url_for('static', filename="images/" + current_user.imageURL)
    email = current_user.email
    user = col_user.find_one({"email": email})
    user_filter = {"email": user["email"]}

    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.imageURL.data:
            picture_file= save_image(form.imageURL.data)
            col_user.update_one(user_filter, {"$set" : {"imageURL": picture_file}})

        
        col_user.update_one(user_filter, {"$set" : {"first_name": form.first_name.data, "last_name":form.last_name.data,  "email": user["email"]}})
        flash('Your account has been updated', 'success')
        return redirect(url_for('account'))
    # Get request auto-completes the users details
    elif request.method == "GET":
        form.first_name.data = user["first_name"]
        form.last_name.data = user["last_name"]
  
    return render_template('account.html',  form=form, user=user)

# Route deletes the current users account and removes it from the database
@app.route("/account/delete",  methods=['GET','POST'])
def delete_account():
    email = current_user.email
    user = col_user.find_one({"email": email})

    _id = user["_id"]
    logout_user()
    col_user.delete_one({"_id": _id})
    flash("Your account has been deleted!", 'success')
    return redirect(url_for('login'))

# Route is used to submit the contact form
@app.route("/contact-form", methods=["GET", "POST"])
def contact_form():
    flash("Thank you for your message, we will be in touch as soon as we can!", 'success')
    return redirect(url_for('contact'))

# 404 error page
@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404

# 500 error page
@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500