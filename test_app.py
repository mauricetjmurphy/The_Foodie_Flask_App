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

    def test_index_content(self):
        #  This test checks if "Featured Categories" is in the response data that we get from the index route
        tester = app.test_client(self)
        response = tester.get('/index', content_type='html/text')
        self.assertTrue(b"Featured Categories" in response.data)

    def test_about(self):
        # This test checks the about page for a HTTP 200 OK response 
        tester = app.test_client(self)
        response = tester.get('/about', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_about_content(self):
        #  This test checks if "About Us" is in the response data that we get from the index route
        tester = app.test_client(self)
        response = tester.get('/about', content_type='html/text')
        self.assertTrue(b"About Us" in response.data)

    def test_contact(self):
        # This test checks the contact page for a HTTP 200 OK response 
        tester = app.test_client(self)
        response = tester.get('/contact', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_contact_content(self):
        # This test checks if "Get In Touch" is in the response data that we get from the index route
        tester = app.test_client(self)
        response = tester.get('/contact', content_type='html/text')
        self.assertTrue(b"Get In Touch" in response.data)

    def test_add_recipe(self):
        # This test checks the add recipe page for a HTTP 200 OK response 
        tester = app.test_client(self)
        response = tester.get('/recipe/new', content_type='html/text')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()