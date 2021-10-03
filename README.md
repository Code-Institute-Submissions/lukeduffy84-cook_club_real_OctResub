![Imgur](https://imgur.com/ktzc6jU.jpg)

# Cook Club: The Online Cookbook


In a world with rapidly changing culinary tastes and diets, this project was created with the goal of making it easy to share original and healthy recipes online. This website was developed for the target audience of amateur chefs who are able to use the platform to share their creative side in the kitchen.
 **Click [here](https://cook-club.herokuapp.com/) to view the deployed site**


# UX

## User Goals

### Non-registered Users

- Allows guest user to search recipe database using search bar available under the navbar.
- Allows guest user to visit 'All Recipes' section and examine all recipes uploaded so far to the database by clicking on the  'all recipes' button on the navbar.
- Allows guest user to hover over an image of a recipe to see display of recipe title.
- Allows guest user to click on the image of a recipe and subsequently be brought to the full recipe page, which will display more information about the recipe including the ingredients and instructins for that particular recipe.
- Allows guest user to see the 'about us' section, which gives a quick general history and overview of 'Cook Club' while providing a convient 'Sign Up' button that directs guest user to registration page.
- Allows guest user to click on the 'login/register' button in the navbar and be brought to the registration page where they can sign up for a Cook CLub account. 

### Logged In Users
- Allows click on the 'Log In / Register" button where they will be subsequently be brought to the registration page, where they will be given the option to 'login' if they are already a member of the site.
- Allows logged in users to add their own recipes by clicking on the 'Add recipes' button within the navbar. On clicking the button, they will be taken to a page where they will be presented with five seperate input fields that allows users to upload a Recipe Name, Image URL, Required Ingredients, Cooking Instructions and finally select a radio button option for which meal the recipe in question pertains to.
- Allows logged in users to check which recipes they have uploaded to Cook Club by clicking on the 'My Recipes' button within the navbar. On clicking the button, they will be taken to a seperate page where they will be presented photos of each of the recipes they've uploaded and the option to visit each recipe page individually. 
- Allows logged in users to edit and delete the recipes they've uploaded through the 'edit' and 'delete' buttons at the bottom of their own recipes. 
- Allows logged in users to sign out of their profile on Cook Club by clicking on the 'Log Out' button within the navbar.


# Design 

## Color Scheme

For my website I used the 'Canva' Pallete generator service to ensure a minimailistic, yet eye-catching and bright color scheme for my website.

![Imgur](https://imgur.com/mDp6Qip.jpg)

## Data Schema 

I used MongoDB for the backend of this project, with the details of the schema and data types show below:
![Imgur](https://imgur.com/tdLFbkr.jpg)


## Wireframes
### Home Page
![Home Page](https://imgur.com/1zFfsZR.png)
### All Recipes Page
![All Recipes page](https://imgur.com/8gKrdRN.png)
### Register Page
![Register Page](https://imgur.com/MRRNYR9.png)
### Upload Recipe Page
![Upload Recipe Page](https://imgur.com/0wKGM3H.png)
### View Recipe Page
![View Recipe Page](https://imgur.com/8ZDxI8Q.png)


## Technoliges Used

<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />

<img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />

<img src="https://img.shields.io/badge/CSS-239120?style=for-the-badge&logo=css3&logoColor=white" />

<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />

<img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E" />

<img src="https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white" />

<img src="https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white" />

<img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white" />



# Testing and Deployment 

## Code Validators

[![W3C HTML Validator](https://img.shields.io/badge/HTML%20Validator-W3C%20HTML%20Validator-red)](https://validator.w3.org/) 
[![W3C CSS Validator](https://img.shields.io/badge/CSS%20Validator-W3C%20CSS%20Validator-darkred)](https://jigsaw.w3.org/css-validator/) 
[![Pep8 Online](https://img.shields.io/badge/Python%20Validator-PEP8%20online-white)](http://pep8online.com/) 

## Database







## Features Testing 

### Accessing Recipes
- Click on 'All Recipes' button on Navbar
- Does it bring you to correct page?
- Hover over image of recipe to display each recipe title
- click on recipe image
- Does it bring you to correct page for corresponding recipe?

### Registering 
- Click on 'Log In / Register' button on Navbar
- Does it render the registration inputs?
- Submit details
- Does it bring you login page to thus login in with new account details?
- Does it allow login with the newly created account details?

### Logging In 
- Click on 'Log In / Register' button on Navbar
- Click on 'Already a member? Login' button at bottom of Registration page
- Does it bring you to login input form?
- After inputting profile username and password, does it render correct corresponding account?
- Does the navbar change to include the Cook Club 'add recipes', 'my recipes' and 'log out' buttons?

### Adding a Recipe
- Click on 'Add Recipes' button on Navbar
- Does website render correct form?
- On clicking 'submit' button, does website bring user back to home page to view newly added recipe?
- Does it render image correctly when recipe is added?
- When clicking on image, does it retrieve correct inputted recipe details?

### Editing a Recipe 
- Click on 'My Recipes' button on Navbar or click on an image of recipe user has already uploaded from their own account
- Does 'Edit' button appear at the bottom of the page?
- After clicking button, is the 'Edit Recipe' page rendered correctly with already inputted details rendering also?
- After editing text/images, are requested changes correctly made to recipe data after clicking the 'submit' button?

### Deleting a Recipe 
- Click on 'My Recipes' button on Navbar or click on an image of recipe user has already uploaded from their own account
- Does 'Delete' button appear at the bottom of the page?
- After clicking button, is user returned correctly the 'My Recipes' page?
- Has seleted recipe been correctly removed from 'all recipes' and 'my recipes' database?


### Searching for a Recipe 
- Input desired recipe keyword into search box on Cook Club webpage
- Does correspinding recipe option render correctly?
- If keyword is uncorresponding to recipe in database, does no recipe show up in results?

### Logging Out 
- Click on 'Log Out' button on Navbar as an already logged in user
- Does website return user to login webpage?
- Does Navbar change to 'Non-logged in' variant with corresponding buttons?

## Deployment

- This project has been stored on Github and is built from 
a master branch by one author at the following link: https://github.com/lukeduffy84/cook_club_real 
- This project has been deployed on Heroku under the following URL: (https://cook-club.herokuapp.com/) 

### Deploy Local Copy 
1. Navigate to main page of repository on Github (https://github.com/lukeduffy84/cook_club_real)

2. Clone the repository by first clicking on the 'Code' button followed by the 'Clone with HTTPS' option

3. Open Git Bash, type 'git clone' and then paste the repository URL copied earlier 
    https://github.com/lukeduffy84/cook_club_real

4. Press Enter 

5. Store Enviroment Variables 
- Create .gitignore file in the root directory of the project and subsequently add the env.py file to the .gitignore
- The env.py file will contain the following environment variables 
 - MONGODB URI 
 - MONGODB PASSWORD 
 - Security Key 
 - Port 5000 
 - IP (0.0.0.0)

### Heroku Deployment 
1. Create a Heroku account 
2. Navigate to to sites repository on Heroku website 
3. Create New App
4. Choose a region 
5. Deploy on Github using Github Connect and URL
6. Click Connect App
7. Click build App 
8. Click on 'Deploy branch' and enable 'Automatic Deploys'





## Media 
- This project has used photos and recipe details from the BBC Food website, which can be found at the following URL: https://www.bbc.co.uk/food 

## Credits and Acknowledgements 
- I would like to say thank you to my mentor Oluwaseun Owonikoko, who has been of immense help and kindness during my coding journey so far.
- I would like the Code Institute tutors, who have shown great patience in assisting me with my many, many questions.
- I would also like to say thanks the code institute studentcare team who have been really helpful in helping me manage the balance of coding with my ongoing University studies
