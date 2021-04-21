# **Air Town**

## **Introduction**

Welcome to my third project, part of the Code Institute Full Stack Development Course.

Air Town is a project based around the love of Sneakers and to give Users space where they can post about Sneakers they currently own or are interested in buying.

Growing up one of the sports that captivated me was basketball, and I grew up falling in love with the Sneaker culture. The sneaker trend at one point was the symbol of hip-hop and its separation from the mainstream.

Having started learning programming with no experience in August last year, I have tried to make each of my projects represent something I feel passionate about and love.

Air Town is a full-stack site that will allow users to manage a common dataset. Users will be able to sign up and log in and take advantage of the features of the site.
The core requirements of this project were to show my understanding of Python, the Flask framework, and using MongoDB as my database.

[Link to the live depolyed Project](https://air-town.herokuapp.com/)

Thank you for visiting Air Town.

---

## **UXD - User Experience Design**

Using Jason James Garrett's, “The Elements of User-Experience”, the planning and development throughout was constantly based on the user experience. The 5 planes used to plan and develop the project are as follows,
- The Stratergy Plane
- The Scope Plane
- The Structure Plane
- The Skeleton Plane
- The Surface Plane

Details of each phase related to the project can be found below.

---

## **The Stratergy Plane**

The Stratergy Plane consists of doing reasearch to understand the use for the project and what users would like to see in the project.

### **User Stories and Creator Goals**

*First-time User goals :*

- As a first time user, I would like some introduction to the project on the home page.
- As a first time user, I would like to see some content related to the topic of the project.
- As a first time user, I would like to see a contrast between images/text/color to make pages more appealing.

*Returning User goals :*

- As a returning user, I would like to be able to sign up and create an account on the website.
- As a returning user, I would like to share my posts and view other posts.
- As a returning user, I would like to be able to edit my posts, to correct any errors or amend the posts to my liking.
- As a returning user, I would like to be able to delete my posts, ideally with some form of confirmation to protect me from missclicks.
- As a returning user, I would like to be able to search posts, and filter for those that I want.

*Creator Goals :*

- As a Creator, I want fans of sneakers to have a platform to share their love for sneakers.
- As a creator, I want to give people an insight into the sneaker culture and the brands.
- As a Creator, I want to use images to help bring the project to life.

User Goals were generated from the research of some forums sites and talking with friends to understand what they would like from the project.

---

## **The Scope Plane**

Often when planning and developing a project, it can be easy to get ahead of ourselves with all the features we would like to implement. 

This hurdle for me during development was my lack of knowledge working with Python and Flask. I tried to focus the development of the project into two separate phases. 

*Phase 1*

- Landing page with a project introduction, and short introduction to the other sections of the project.
- A couple of pages relating to the popular sneaker brands.
- Forum page allowing users to view posts, search for posts, signed in users can edit and delete posts made by them. 
- Sign up page for users to create an account, Sign out page for users to be able to sign out after a session. 
- Account page will allow users to be bale to view their posts, users should be allowed to edit and delete their posts from the account page. 
- Posts will have the Username and a date/time at the top, allowing posts to be sorted by the lastest post at the top. 

*Phase 2*

- Additional interactive features to help pages feel less static. 
- Users will be allowed to upload images to their posts, with files directly from their computer. 
- Account page will have options for users to be able to change their username and password.
- Pagination so that the posts on the page are limited. 

Phase 1 will act as the project's minimal viable product, offering users simple CRUD functions. While still meeting the goals for first-time and regular users. 

Phase 2 will build further on the project adding features that will further provide user functionality and improve the user experience.


## Database Structure

 [Link to Diagram of Database Structure](https://github.com/Harry-Leepz/Project-Airtown/blob/master/documentation/airtown-tables.pdf)

### Users
```
{
    "_id": {
        "$oid": "60746ec8dfc15759510dfa4e"
    },
    "username": "user_username",
    "firstname": "user_firstname",
    "lastname": "user_lastname",
    "password": "user_password"
}
```

### Posts
```
{
    "_id": {
        "$oid": "60746f74dfc15759510dfa4f"
    },
    "post_author": "Username",
    "post_date": "17 April 2021 - 21:20:17",
    "post_title": "Check me Out",
    "category_name": "Humble Brag",
    "post_content": "Hey, This is my test post!",
    "image": ""
}
```

### Post Categories
```
{
    "_id": {
        "$oid": "60746fd7dfc15759510dfa51"
    },
    "category_name": "Humble Brag"
}
{
    "_id": {
        "$oid": "60746feedfc15759510dfa52"
    },
    "category_name": "Simple Review"
}
{
    "_id": {
        "$oid": "60747003dfc15759510dfa53"
    },
    "category_name": "Honest Opinion"
}
```