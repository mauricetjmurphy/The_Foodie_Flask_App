from flask import render_template, url_for
from app import app

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

    return render_template('login.html', about=True)


@app.route("/recipe/new", methods=["GET", "POST"])

def new_recipe():

    return render_template('new_recipe.html', about=True)

@app.route("/account", methods=["GET", "POST"])

def account():

    return render_template('account.html', about=True)


@app.route("/category")

def category():

    return render_template('account.html', about=True)