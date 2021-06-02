import unittest
from flask_testing import TestCase
from flask import Flask, g
from app import app, db, mongo
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from app.models import User, Recipe, Post, RecipePost
from flask_login import login_user, current_user, logout_user, login_required
from flask import  session, render_template, url_for, request, json, Response, flash, redirect, session, abort
from dotenv import load_dotenv
import os

load_dotenv()


"""Before running the tests please ensure the @login_required decorator is disabled"""

class TestCase(unittest.TestCase):

    def test_index(self):
        # This test checks the index page for a HTTP 200 OK response
        tester = app.test_client(self)
        response = tester.get('/index', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    



if __name__ == '__main__':
    unittest.main()