## Code Institute Data Centric Development Milestone Project

---

# The Foodie

![Main responsive image](https://res.cloudinary.com/gemtech-solutions/image/upload/v1621965121/The%20Foodie/responsive_k01lld.png)

The Foodie is an online platform where users can share recipes and ideas. The user can create their own personal account where they can add, edit and delete recipies at their leisure. They can also leave commments on any shared recipe on the site.

[Visit deployed website]()

## Table of Contents

---

-   [The Foodie](#the-foodie)
    -   [Table of Contents](#table-of-contents)
    -   [UI/UX](#uiux)
        -   [Project goals](#project-goals)
        -   [User Stories](#user-stories)
    -   [Design](#design)
        -   [Wireframes](#wireframes)
        -   [Colour Scheme](#colour-scheme)
        -   [Database Schema](#database-schema)
        -   [Defensive Design](#defensive-design)
    -   [Features](#features)
        -   [Existing features](#existing-features)
        -   [Future features](#future-features)

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

As an admin I would like to do all of the above plus:

-   [x] Delete all recipes

## Design

A lot of my inspiration and design ideas come from [Yummy](https://www.yummly.co.uk/), a recipe website that allows users search through thousands of recipes.

To build the website is used bootstrap 5, Fontawsome and fonts from Google Fonts.

### Wireframes

I developed my wireframes using the Figma browser based design tool. Initially I created wirframes for the [homepage](), [recipe page](), [recipe form]() and [contact page]().

### Colour Scheme

![color scheme](https://res.cloudinary.com/gemtech-solutions/image/upload/v1622023857/The%20Foodie/colour-palette_nhhq2v.png)

### Database Schema

My MongoDB database consists of 4 collections, one for each of the following:

-   Recipe
-   Post
-   User
-   Recipe_Post

The first three colllections hold data about the user. The fourth collection is a collect that joins the two collections, post and recipe. It allows us to populate each recipe with the coorect user posts.

### Defensive Design

Defensive design has been achieved by ensuring that:

-   protection against unexpected user inputs or actions.
-   maintainability - ensuring code is readable and understandable.
-   minimising/removing bugs.

## Features

### Existing features

### Future features
