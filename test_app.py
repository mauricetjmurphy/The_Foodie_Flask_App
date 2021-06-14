import unittest
from app import app
from dotenv import load_dotenv

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
        #  This test checks if "About Us" is in the response data that we get from the about route
        tester = app.test_client(self)
        response = tester.get('/about', content_type='html/text')
        self.assertTrue(b"About Us" in response.data)

    def test_contact(self):
        # This test checks the contact page for a HTTP 200 OK response 
        tester = app.test_client(self)
        response = tester.get('/contact', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_contact_content(self):
        # This test checks if "Get In Touch" is in the response data that we get from the contact route
        tester = app.test_client(self)
        response = tester.get('/contact', content_type='html/text')
        self.assertTrue(b"Get In Touch" in response.data)

    def test_add_recipe(self):
        # This test checks the add recipe page for a HTTP 200 OK response 
        tester = app.test_client(self)
        response = tester.get('/recipe/new', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_add_recipe_content(self):
        # This test checks if "Add a new recipe" is in the response data that we get from the add recipe route
        tester = app.test_client(self)
        response = tester.get('/recipe/new', content_type='html/text')
        self.assertTrue(b"Add a new recipe" in response.data)

    def test_account(self):
        # This test checks the account page for a HTTP 200 OK response 
        tester = app.test_client(self) 
        response = tester.get('/account', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_account_content(self):
        # This test checks if "Update Details" is in the response data that we get from the account route
        tester = app.test_client(self)
        response = tester.get('/account', content_type='html/text')
        self.assertTrue(b"Update Details" in response.data)

    def test_recipe(self):
        # This test checks the recipe page for a HTTP 200 OK response 
        tester = app.test_client(self)
        response = tester.get('/recipe/1', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_recipe_content(self):
        # This test checks if "Chicken Tikka Masala" is in the response data that we get from the recipe route
        tester = app.test_client(self)
        response = tester.get('/recipe/1', content_type='html/text')
        self.assertTrue(b"Chicken Tikka Masala" in response.data)

    def test_recipe_update(self):
        # This test checks the update recipe page for a HTTP 200 OK response 
        tester = app.test_client(self)
        response = tester.get('/recipe/1/update', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_recipe_update_content(self):
        # This test checks if "Update recipe" is in the response data that we get from the recipe update route
        tester = app.test_client(self)
        response = tester.get('/recipe/1/update', content_type='html/text')
        self.assertTrue(b"Update recipe" in response.data)

if __name__ == '__main__':
    unittest.main()