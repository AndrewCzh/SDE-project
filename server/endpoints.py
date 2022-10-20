"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""
from http import HTTPStatus

from flask import Flask, request
from flask_restx import Resource, Api, fields
import werkzeug.exceptions as wz

import db.char_types as ctyp
import db.food_types as ftyp
import server.ingredients_generator as ig

# import db.db as db

app = Flask(__name__)
api = Api(app)

LIST = 'list'
DETAILS = 'details'
ADD = 'add'
MAIN_MENU = '/main_menu'
MAIN_MENU_NM = 'Main Menu'
HELLO = '/hello'
MESSAGE = 'message'
CHAR_TYPE_LIST = f'/character_types/{LIST}'
CHAR_TYPE_LIST_NM = 'character_types_list'
CHAR_TYPE_DETAILS = f'/character_types/{DETAILS}'
FOOD_TYPE_LIST = f'/food_types/{LIST}'
FOOD_TYPE_LIST_NM = 'food_types_list'
FOOD_TYPE_DETAILS = f'/food_types/{DETAILS}'
INGREDIENTS_GENERATOR_LIST = f'/ingredients_generator/{LIST}'
INGREDIENTS_GENERATOR_LIST_NM = 'ingredients_generator_list'
INGREDIENTS_GENERATOR_DETAIL = f'/ingredients_generator/{DETAILS}'
LOGIN = '/templates/login'
USERS_NS = 'users'
USER_LIST = f'/{USERS_NS}/{LIST}'
USER_LIST_NM = f'{USERS_NS}_list'
USER_DETAILS = f'/{USERS_NS}/{DETAILS}'
USER_ADD = f'/{USERS_NS}/{ADD}'

@api.route(HELLO)
class HelloWorld(Resource):
    """
    The purpose of the HelloWorld class is to have a simple test to see if the
    app is working at all.
    """
    def get(self):
        """
        A trivial endpoint to see if the server is running.
        It just answers with "hello world."
        """
        return {MESSAGE: 'hello world'}


@api.route(MAIN_MENU)
class MainMenu(Resource):
    """
    This will deliver our main menu.
    """
    def get(self):
        """
        Gets the main game menu.
        """
        return {MAIN_MENU_NM: {'the': 'menu'}}


@api.route(FOOD_TYPE_LIST)
class FoodTypeList(Resource):
    """
    This will get a list of food types
    """
    def get(self):
        """
        Returns a list of character types.
        """
        return {FOOD_TYPE_LIST_NM: ftyp.get_food_types()}


@api.route(f'{FOOD_TYPE_DETAILS}/<food_type>')
class FoodTypeDetails(Resource):
    """
    This will get a list of character types.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self, food_type):
        """
        Return a list of food types.
        """
        ft = ftyp.get_food_type_details(food_type)
        if ft is not None:
            return {food_type: ftyp.get_food_type_details(food_type)}
        else:
            raise wz.NotFound(f'{food_type} not found.')


@api.route(CHAR_TYPE_LIST)
class CharacterTypeList(Resource):
    """
    This will get a list of character types.
    """
    def get(self):
        """
        Returns a list of character types.
        """
        return {CHAR_TYPE_LIST_NM: ctyp.get_char_types()}


@api.route(f'{CHAR_TYPE_DETAILS}/<char_type>')
class CharacterTypeDetails(Resource):
    """
    This will get a list of character types.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self, char_type):
        """
        Returns a list of character types.
        """
        ct = ctyp.get_char_type_details(char_type)
        if ct is not None:
            return {char_type: ctyp.get_char_type_details(char_type)}
        else:
            raise wz.NotFound(f'{char_type} not found.')


@api.route(INGREDIENTS_GENERATOR_LIST)
class IngredientsGeneratorList(Resource):
    """
    This will get a list of ingredients
    """
    def get(self):
        """
        Returns a list of ingredients.
        """
        return {INGREDIENTS_GENERATOR_LIST_NM: ig.random_ingredients()}


@api.route(INGREDIENTS_GENERATOR_DETAIL)
class IngredientsGeneratorDetails(Resource):
    """
    This will get a list of ingredients
    """
    def get(self):
        """
        Returns a price
        """
        price = ig.get_ingredients_price_details()
        if price is not None:
            return {'Price': price}
        else:
            wz.NotFound('Price is not found.')


@api.route('/endpoints')
class Endpoints(Resource):
    """
    This class will serve as live, fetchable documentation of what endpoints
    are available in the system.
    """
    def get(self):
        """
        The `get()` method will return a list of available endpoints.
        """
        endpoints = ''
        # sorted(rule.rule for rule in api.app.url_map.iter_rules())
        return {"Available endpoints": endpoints}
