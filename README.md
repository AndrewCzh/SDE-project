# REPSAJ | (JASPER)
An example flask rest API server, for SE Fall 2022.

To build production, type `make prod`.

To create the env for a new developer, run `make dev_env`.

We will write an API-driven restaurant business game. Players take the role of a chef in the JASPER kitchen of a designated restaurant to earn money by fulfilling customers' orders.

## Requirements

- List all available characters
- List all active characters
- Signup
- Signin
- Describe a locale
- Allow character to move
- Allow character to act
- Allow character to talk to other characters in locale

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
- Pizza sauce
- Fresh dough
- Thin crust

## Web design
- Selecting ingredients
- Cutting station
- Cooking station 
- Baking station     

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

## Project Timeline
- Regular meeting every week on Thursdays
- Database inserts of dishes and ingredients are due on October 1st

