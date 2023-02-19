# REPSAJ | (JASPER)
An example flask rest API server, for SE Fall 2022.

To build production, type `make prod`.

To create the env for a new developer, run `make dev_env`.

We will write an API-driven restaurant business game. Players take the role of a chef in the JASPER kitchen of a designated restaurant to earn money by fulfilling customers' orders.

## Requirements

- List all available characters
- List all active characters
- Set passwords for Signup and Signin
- Describe a locale
- Allow character to move
- Allow character to act
- Allow character to talk to other characters in locale
- Allow multiple orders happen at the same time (future goal)
- Use timer to record time

## Design
- Restaurant operation game
- Customers come and order food
- Player select ingredients to cook food and gain money
- Game succeeds when reach the daily turnover, but fails when the time is up

## Process

- Customers' orders appear on top of the window.
- Chef picks corresponding ingredients for the order.
- Chef acts on potential cooking steps based on different kinds of dishes.
- Complete THE ORDER WITHIN A specified time - earn revenue for the order (if the order is completed quickly, get tips?)
- After the specified time, the order disappears.
- Reach the specified amount within the specified time to win the game.

## Dish types
- Burger
- Pizza
- Salad
- Hot dog
- Sushi

## Ingredient types
- Cheese
- Crust
- Spinach 
- Pepperoni
- Tomato 
- Pineapple
- Mushroom
- Green Peppers
- Red Peppers
- Onions
- Corn
- Rice
- Lettuce
- Beef
- Bacon
- Salmon
- Avacado
- Zucchini
- Chicken
- Broccoli
- Carrot


## Web design
- Selecting ingredients
- Cutting station
- Cooking station 
- Baking station
- Rating process     

## Technologies
- Python 3.8 or greater
- Pytest
- flask and flask-restx
- MongoDB
- flake8
- GitHub Actions
- Heroku
- React
- Github
- Pythonanywhere

## Project Timeline
- Regular meeting every week on Monday 4-5pm
- Function todo
   - basic login/enter page, logout/exit page (done)
   - randomly generates ingredients for different dishes (done)
   - basic login/enter page (done)
   - select the ingredients (done)
   - test if the game runs correctly on pythonanywhere (done)
   - fix teh problem that only log in page can be shown on pythonanywhere (done)
   - uploaded endpoints to the pythonanywhere(done)
   - collects money if finished 
   - select the cooking tool 
   - verify if ingredients and the cooking tool are correct and then customer will pay
   - check if player gain enough money
   - try to maek the frontend interface prettier

## Database
- Uploaded github and project python files to pythonanywhere
- Now can be connected to Cloud and Local in MongoDB

## Deploy to web
- Upgraded pythonanywhere to run python code in the cloud from one web app and the console for 1GB service
- set environment variables for website
- The website is now deployed to pythonanywhere: http://andrew1531.pythonanywhere.com/
