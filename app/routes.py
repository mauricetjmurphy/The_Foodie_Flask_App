from flask import render_template, url_for
from app import app

# Decorators (app routes)
@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')