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
import db.check_tool as ctool
import server.ingredients_generator as ig
import db.users as usr
from flask import Flask, jsonify, request

# import db.db as db

app = Flask(__name__)
api = Api(app)

LIST = 'list'
DICT = 'dict'
DETAILS = 'details'
ADD = 'add'
DELETE = 'delete'
MAIN_MENU = '/main_menu'
MAIN_MENU_NM = 'Main Menu'
HELLO = '/hello'
MESSAGE = 'message'
CHAR_TYPE_LIST = f'/character_types/{LIST}'
CHAR_TYPE_LIST_NM = 'character_types_list'
CHAR_TYPE_DETAILS = f'/character_types/{DETAILS}'
CHAR_TYPE_DICT = f'/character_types/{DICT}'
CHAR_TYPE_DICT_NM = 'character_types_dict'
FOOD_TYPE_DICT = f'/food_types/{DICT}'
FOOD_TYPE_LIST = f'/food_types/{LIST}'
TOOL_TYPE_LIST = f'/tool_types/{LIST}'
FOOD_TYPE_DICT = f'/food_types/{DICT}'
TOOL_TYPE_LIST_NM = 'tool_types_list'
FOOD_TYPE_LIST_NM = 'food_types_list'
FOOD_TYPE_DICT_NM = 'food_types_dict'
FOOD_TYPE_DETAILS = f'/food_types/{DETAILS}'
TOOL_TYPE_DICT = f'/check_tool/{DICT}'
INGREDIENTS_GENERATOR_LIST = f'/ingredients_generator/{LIST}'
INGREDIENTS_GENERATOR_LIST_NM = 'ingredients_generator_list'
INGREDIENTS_GENERATOR_DETAIL = f'/ingredients_generator/{DETAILS}'
LOGIN = '/templates/login'
USERS_NS = 'users'
USER_DICT = f'/{USERS_NS}/{DICT}'
USER_LIST = f'/{USERS_NS}/{LIST}'
USER_LIST_NM = f'{USERS_NS}_list'
USER_DETAILS = f'/{USERS_NS}/{DETAILS}'
USER_ADD = f'/{USERS_NS}/{ADD}'
USER_DELETE = f'/{USERS_NS}/{DELETE}'

@api.route(HELLO)
class HelloWorld(Resource):
    """
    The purpose of the HelloWorld class is to have a simple test to see if the
    app is working at all.
    """

    def get(self):
        """
        Gets the main game menu.
        """
        return {MESSAGE: 'hello world'}


@api.route(MAIN_MENU)
class MainMenu(Resource):
    """
    This will deliver our main menu.
    """

    def get(self):
        """
        A
        """
        return {'Title': MAIN_MENU_NM,
                'Default': 0,
                'Choices': {
                    '1': {'url': f'/{USER_DICT}',
                          'method': 'get', 'text': 'List Users'},
                    '2': {'url': f'/{FOOD_TYPE_DICT}',
                          'method': 'get', 'text': 'List Food Types'},
                    '3': {'url': f'/{TOOL_TYPE_DICT}',
                          'method': 'get', 'text': 'List Tools'},
                    'X': {'text': 'Exit'},
                }}


@api.route(TOOL_TYPE_DICT)
class ToolTypeDict(Resource):
    """
    This will get a list of food types
    """

    def get(self):
        """
        Returns a list of character types.
        """
        return {'Data': ctool.get_tool_types_dict(),
                'Type': 'Data',
                'Title': 'Tool Types'}


@api.route(FOOD_TYPE_DICT)
class FoodTypeDict(Resource):
    """
    This will get a list of food types
    """

    def get(self):
        """
        Returns a list of character types.
        """
        return {'Data': ftyp.get_food_type_dict(),
                'Type': 'Data',
                'Title': 'Food Types'}


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
   
@api.route(TOOL_TYPE_LIST)
class ToolTypeList(Resource):
    """
    This will get a list of cook tool types
    """

    def get(self):
        """
        Returns a list of character types.
        """
        return {TOOL_TYPE_LIST_NM: ftyp.get_tool_types()}


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


@api.route(CHAR_TYPE_DICT)
class CharacterTypeDict(Resource):
    """
    This will get a list of character types.
    """
    def get(self):
        """
        Returns a list of character types.
        """
        return {'Data': ctyp.get_char_type_dict(),
                'Type': 'Data',
                'Title': 'Character Types'}


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


@api.route(USER_DICT)
class UserDict(Resource):
    """
    This will get a list of currrent users.
    """
    def get(self):
        """
        Returns a list of current users.
        """
        return {'Data': usr.get_users_dict(),
                'Type': 'Data',
                'Title': 'List Users'}


@api.route(USER_LIST)
class UserList(Resource):
    """
    This will get a list of currrent users.
    """
    def get(self):
        """
        Returns a list of current users.
        """
        return {USER_LIST_NM: usr.get_users()}


# user_fields = api.model('NewUser', {
#     usr.NAME: fields.String,
#     usr.EMAIL: fields.String,
#     usr.FULL_NAME: fields.String,
# })
user_fields = api.model('NewUser', {
    usr.NAME: fields.String,
    # usr.EMAIL: fields.String,
    # usr.FULL_NAME: fields.String,
})


@api.route(USER_ADD)
class AddUser(Resource):
    """
    Add a user.
    """
    @api.expect(user_fields)
    def post(self):
        """
        Add a user.
        """
        print(f'{request.json=}')
        name = request.json[usr.NAME]
        del request.json[usr.NAME]
        uid = usr.add_user(name)
        return uid
        # usr.add_user(name, request.json)


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
