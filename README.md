# Air Town

## Introduction

Welcome to my third project, part of the Code Institute Full Stack Development Course.

Air Town is a project-based around the love of Sneakers and to give Users space where they can post about Sneakers they currently own or are interested in buying.

Growing up one of the sports that captivated me was basketball, and I grew up falling in love with the Sneaker culture. The sneaker trend at one point was the symbol of hip-hop and its separation from the mainstream.

Having started learning programming with no experience in August last year, I have tried to make each of my projects represent something I feel passionate about and love.

Air Town is a full-stack site that will allow users to manage a common dataset. Users will be able to sign up and login and take advantage of the features of the site.

Thank you for visiting Air Town.


## User Stories

First-time User goals :

- As a first time user, I would like some introduction to the project on the home page.
- As a first time user, I would like to see some content related to the topic of the project.
- I would like to see a contrast between images/text/color to make pages more appealing.

Returning User goals :
- As a returning user, I would like to be able to sign up and create an account on the website.
- As a returning user, I would like to share my posts and view other posts.
- As a returning user, I would like to be able to edit my posts, to correct any errors or amend the posts to my liking.
- As a returning user, I would to be able to delete my posts, ideally with some form of confirmation to protect me from missclicks.

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