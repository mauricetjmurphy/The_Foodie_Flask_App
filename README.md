## Code Institute Data Centric Development Milestone Project

---

# The Foodie

![Main responsive image](https://res.cloudinary.com/gemtech-solutions/image/upload/v1621965121/The%20Foodie/responsive_k01lld.png)

The Foodie is an online platform where users can share recipes and ideas. The user can create their own personal account where they can add, edit and delete recipies at their leisure. They can also leave commments on any shared recipe on the site.

[Visit deployed website](https://the-foodie-app.herokuapp.com)

## Table of Contents

---

- [The Foodie](#the-foodie)
  - [Table of Contents](#table-of-contents)
  - [UI/UX](#uiux)
    - [Project goals](#project-goals)
    - [User Stories](#user-stories)
  - [Design Features](#design-features)
    - [Login](#login)
    - [Registration page](#registration-page)
    - [Homepage](#homepage)
    - [About](#about)
    - [Contact](#contact)
    - [Add recipe](#add-recipe)
    - [Account](#account)
    - [Recipe](#recipe)
    - [Wireframes](#wireframes)
    - [Colour Scheme](#colour-scheme)
    - [Database Schema](#database-schema)
    - [Defensive Design](#defensive-design)
  - [Features](#features)
    - [Existing features](#existing-features)
    - [Future features](#future-features)
  - [Technologies used](#technologies-used)
  - [Deployment](#deployment)
    - [Heroku](#heroku)
  - [Testing](#testing)
    - [Usability testing](#usability-testing)
    - [Non existing endpoints](#non-existing-endpoints)
    - [Manual](#manual)
    - [Automated](#automated)
      - [Unittesting](#unittesting)
    - [Validators](#validators)
      - [1. HTML5](#1-html5)
      - [2. CSS3](#2-css3)
      - [3. JavaScript](#3-javascript)
      - [4. Browsers](#4-browsers)
      - [5. Responsivness](#5-responsivness)
      - [6. Form Validation](#6-form-validation)
  - [Performance](#performance)
    - [Lazy Loading](#lazy-loading)
  - [Credits](#credits)
    - [Code](#code)
    - [Images](#images)
  - [Acknowledgements](#acknowledgements)

---

## UI/UX

---

### Project goals

The goal of this project was to create an application that would allow users to share recipies from accross the world. The app allows the user to create an account, where they can create, read, update and delete their recipe data (CRUD). The app also allows the user to view and leave comments on any recipe uploaded to the site. It provides a platform for all the food lovers out there to share and also try new recipes.

### User Stories

As a user I would like to:

-   [x] I would like to access the application from both a desktop and mobile browsers.
-   [x] I would lik to be able to create my own personal account.
-   [x] I would like smooth and easy navigation of the application to view information.
-   [x] I want to view information about the site.
-   [x] I want to be able to contact the site administrator regarding any queries I might have.
-   [x] I want to be able to add, edit and delete my recipes.
-   [x] I want to be able to comment on any recipe on the site.
-   [x] I want to be able you update my account information.

## Design Features

A lot of my inspiration and design ideas come from [Yummy](https://www.yummly.co.uk/), a recipe website that allows users to search through thousands of recipes.

### Login

-   Login form for the user to enter their credentials and login in.
-   Submit button with hover effect.
-   New account button to take the user to the registration page.
-   Form fields are all validated by flask-WTF extension.

### Registration page

-   Registration form for te user to sign up and login.
-   Form fields are all validated by flask-WTF extension.
-   The user will have to enter a unique email addess that does not already exist in the database.

### Homepage

-   Navigation bar with links to each page.
-   Slick slide carousel that shows several featured recipes.
-   Categories section where each recipe is categorised into specific meals
-   Featured recipe section where recipes paginated and displayed.
-   Click on the recipes to navigate to the specific recipe page.

### About

-   About page contains information about the app and its history

### Contact

-   The contact page contains a contact form that the user can submit any query to.
-   The form containes field validation.
-   The pages contains a google map displaying the business location.

### Add recipe

-   Recipe form for user to submit new recipes. Form uses javascript validation.
-   Recipe will be displayed on the app once submitted.
-   Dynamic form fields allow the user to add/remove ingredient and direction input fields.

### Account

-   The account page displays the current users details.
-   Provides the user a form to update details.
-   Profile image upload.
-   Delete account button.

### Recipe

-   The recipe page displays all the recipe data.
-   User has the option to update or delete the recipe only if the recipe was created by hte user.
-   Update displays an auto-filled form. The user then can edit the data and resubmit the form.
-   Delete route will warn the user with a modal popup. If the user wishes to proceed, they can click delete again.
-   The user can also add a post to the recipe. The post submit form is at the bottom of the page.

### Wireframes

I developed my wireframes using the Figma browser based design tool. Initially I created wirframes for the login page, homepage, recipe page, add recipe page, about and contact page. Wireframes can be found in the wireframe directory.

### Colour Scheme

![color scheme](https://res.cloudinary.com/gemtech-solutions/image/upload/v1622023857/The%20Foodie/colour-palette_nhhq2v.png)

### Database Schema

My MongoDB Atlas cloud database consists of 4 collections, one for each of the following:

-   Recipe
-   Post
-   User
-   Recipe_Post

The first three colllections hold data about the user. The fourth collection is a collect that joins the two collections, post and recipe. It allows us to populate each recipe with the coorect user posts.

The database configuration is set in the config file. Its connected using a connection string provided by MongoDB Atlas. All queries to the database are done through the pymongo library. This is ititialized in the **init**.py file.

### Defensive Design

Defensive design has been achieved by ensuring that:

-   protection against unexpected user inputs or actions.
-   maintainability - ensuring code is readable and understandable.
-   minimising/removing bugs.

## Features

### Existing features

-   [x] Users can login to their accounts
-   [x] Users can register for new accounts
-   [x] Navigation bar for smooth navigation
-   [x] Sorting by category by clicking navigation links.
-   [x] Use of flash messages to inform the user of there actions and errors
-   [x] Users can add comments to any recipe
-   [x] User can edit and delete their account
-   [x] Only users with accounts can view, update and delete recipes and add comments
-   [x] User authentication using Flask-login extension
-   [x] Password hashing using Werkzeug-security
-   [x] The user has a section to contact the site admin
-   [x] Users have access to social media links
-   [x] Users can click on a dish to reveal the full recipe
-   [x] Form validation for all form fields
-   [x] The website includes a about page containing information about the site
-   [x] Pagination for the recipe pages
-   [x] Lazy loading images
-   [x] Dynamic form fields

### Future features

-   [ ] Reset password link
-   [ ] Remove posts
-   [ ] Recipe search function
-   [ ] Admin console
-   [ ] Google login
-   [ ] recipe image cropping and saving
-   [ ] Lighthouse performance improvement
-   [ ] API

## Technologies used

-   HTML 5
-   CSS 3
-   jQuery
-   Python 3
    -   Flask
    -   Jinja
    -   Werkzeug security
    -   Flask-login
    -   Flask-wtf
    -   Flask Paginate
-   MongoDB and MongoDB Compass
-   Bootstrap
-   Google fonts
-   Slick.js
-   Fonts Awesome
-   Git & GitHub
-   Heroku
-   Adobe suite
-   Cloudinary
-   Google Chrome Developer tools
-   Firefox Developer tools
-   Safari Web Inspector

## Deployment

This project can be ran locally by following the following steps:
(Steps may differ in GitPod/Windows/Linux. I used Visual Studio Code on MacOS)

Create a free account on Cloudinary.com download my media or create your own.

Visit this [repository link](https://github.com/mauricetjmurphy/The_Foodie_Flask_App.git) and click on the Clone or Download button to copy the link provided.

![clone](https://res.cloudinary.com/gemtech-solutions/image/upload/v1623260440/The%20Foodie/Screenshot_2021-06-09_at_18.40.25_jmjmf9.png)

In your IDE, open a Terminal window and change to the directory where you want to clone this [repository](https://github.com/sabinemm/recipe-site-ms3.git) and type:

for macOS:

```
$ cd /Users/user/my_project
```

for Windows:

```
$ cd C:/Users/user/my_project
```

and type:

```
$ git init
```

```
$ git clone https://github.com/mauricetjmurphy/The_Foodie_Flask_App.git
```

After pressing Enter the project will be created and cloned locally.

(Alternatively you can download the zipped file, decompress it and use your IDE of choice to access it.)

Create a free account on MongoDb and reproduce the 4 collections as described [here](#Information-Architecture).

Make sure to upgrade PIP.

```
$ pip install -U pip
```

Install all dependencies

```
$ pip3 install -r requirements.txt
```

Activate virtual environment

```
$ source venv/bin/activate
```

Create .env file with following data

```
MONGO_URI=mongodb+srv://...
SECRET_KEY=***
```

Add your .env file to .gitignore

You will then be able to run the app locally by typing `python app.py` or `flask run`.

### Heroku

Heroku was chosen as the deployment platform for this project. The steps to deploy the local app to Heroku were as follow:

In Heroku, create an app. The app must have a unique name.

Link that app to the GitHub repository by going to the "Deploy" tab in the main app menu.

In the Settings tab, add the corresponding Config Variables as present in local development:

```
MONGO_URI mongodb+srv://...
IP 0.0.0.0
SECRET_KEY = ***
```

Created "Procfile" and add the following line to the file:

```
web: python app.py
```

Click Deploy Branch in Heroku

![Deploy Branch](https://res.cloudinary.com/gemtech-solutions/image/upload/v1623260875/The%20Foodie/Screenshot_2021-06-09_at_18.47.34_iuiofr.png)

After these steps the app is live and running remotely in Heroku's servers.

## Testing

### Usability testing

Useability testing for this website was achieved by sending a live link of the site to a selected group of people and setting them a number of navigation tasks to carry out. Users reported that they could easily accomplish their tasks and navigate seemlessly through the site.

### Non existing endpoints

I have added custom 404 and 500 error pages

![Error page](https://res.cloudinary.com/gemtech-solutions/image/upload/v1622798866/The%20Foodie/404_e17smz.jpg)

### Manual

1. Register

    - Tested to submit the signup form with blank fields. Received the error "This field is required".
    - Tested to register with an incorrect email address format. Received the error "Please enter a vlaid email.

2. Login

    - Tested to submit the login form with blank fields. Received the error "This field is required".
    - Tested to submit a form with a user detail that do not exist in the database. Flash message warns the user to check username and password

3. Recipe Form

    - Tested to submit empty form and verify that no recipe has been added to any category page.
    - Tested to submit filled out form with data in all fields.
    - Tested to submit the form with empty fields. Some fields have been intenionally left open to blank data.

4. Update Recipe

    - Tested to change some data on the form and resubmit the form.
    - Tested to submit filled out form with data in all fields.
    - Tested to submit the form with empty fields. Some fields have been intenionally left open to blank data.

5. Delete Recipe

    - Tested to delete a recipe.
    - The delete button opens a modal that asks the user if they would like to delete or not.

![Main responsive image](https://res.cloudinary.com/gemtech-solutions/image/upload/v1623258547/The%20Foodie/Screenshot_2021-06-09_at_18.08.45_wdqpau.png)

6. Logout

    - Tested the logout route
    - If the user is logged out the Flask-login "@Login_required" redirects the user back to the login page and displays a flash messages to say that login is required.

### Automated

#### Unittesting

Automated testing was carried out on specific parts of the application. Python comes with a built in set of tools and libraries that can be used to test for your application.

I mainly trsted the http routes and checked for a 200 success response. I also tested for specific response data on all routes. Flask-login auth blocked the test response so I temporarily disabled the @Login_required decorators before running the tests.

All tests can be found in the test_app.py file.

### Validators

#### 1. HTML5

-   W3C HTML Validator
    -   Document checking on HTML. All warning that remain are related to the Jinja templating and cannot be avoided.

#### 2. CSS3

-   W3C CSS Validator
    -   No errors found

#### 3. JavaScript

-   JsHint Metrics

    -   There are 5 functions in this file.
    -   Function with the largest signature take 0 arguments, while the median is 0.
    -   Largest function has 6 statements in it, while the median is 3.
    -   The most complex function has a cyclomatic complexity value of 2 while the median is 1.

-   Warnings
    -   'template literal syntax' is only available in ES6 (use 'esversion: 6').

#### 4. Browsers

-   The app was tested on the four most used browsers Chrome, Safari, Internet Explorer and Firefox, according to W3Counter. The main testing was done with the Chrome DevTools.

#### 5. Responsivness

-   Responsive design was factored in during the design of the app. This was achieved with a combination of Bootstrap, CSS Grid, CSS Flexbox and media queries. The media queries changed the screen layout as the screen size changed.

#### 6. Form Validation

All form fields in this projct are validated using flask wtf form validators. Any form field not using WTF validation, will contain the HTML ‘required’ property for validation. By catching invalid data on the client-side, the user can fix it straight away.

## Performance

I user the chrome browsers Lighthouse tool to check performance. There were several areas which needed improvement. These are areas that would require future improvement.

### Lazy Loading

I have use the new html "loading=lazy" attribute throughout the app. The loading attribute specifies whether a browser should load an image immediately or to defer loading of off-screen images until for example the user scrolls near them.

## Credits

### Code

-   Stack Overflow
-   W3Schools
-   MDN Web Docs

### Images

-   Pexels
-   Unsplash
-   Stocksnap

## Acknowledgements

This app was built using the Flask Framework. I would like to give a big thanks to the creator of Flask and all the Flask community that help developer like myself become better ones.

I would also like to thank the stack overflow community that helped me to solve the issues that I faced throughout this project.

Finally, I would like to thank all the Youtube contributors, providing endless amounts of educational content. Particularly Corey Shafer for his amazimg in depth video tutorials on the Flask Framework.
