"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""
from http import HTTPStatus
from flask import Flask, request, jsonify
from flask_restx import Resource, Api, fields, Namespace
import werkzeug.exceptions as wz
import db.food_types as ftyp
import db.check_tool as ctool
from server.ingredients_generator import \
    get_ingredients_price_details
import db.users as usr
import db.games as gm
import server.start_game as sg
import db.ingredient_choice as ingc
# from flask import jsonify
import db.ingredients_choice as ingc

# import common.form_filler as ff
# import db.db as db

app = Flask(__name__)
api = Api(app)

USERS_NS = 'users'
GAMES_NS = 'games'
users = Namespace(USERS_NS, 'Users')
api.add_namespace(users)
games = Namespace(GAMES_NS, 'Games')
api.add_namespace(games)

LIST = 'list'
DICT = 'dict'
DETAILS = 'details'
ADD = 'add'
DELETE = 'delete'
MAIN_MENU = '/main_menu'
MAIN_MENU_NM = 'Main Menu'
HELLO = '/hello'
MESSAGE = 'message'
# CHAR_TYPE_LIST = f'/character_types/{LIST}'
# CHAR_TYPE_LIST_NM = 'character_types_list'
# CHAR_TYPE_DETAILS = f'/character_types/{DETAILS}'
# CHAR_TYPE_DICT = f'/character_types/{DICT}'
# CHAR_TYPE_DICT_NM = 'character_types_dict'
FOOD_TYPE_DICT = f'/food_types/{DICT}'
FOOD_TYPE_LIST = f'/food_types/{LIST}'
TOOL_TYPE_LIST = f'/tool_types/{LIST}'
TOOL_TYPE_LIST_NM = 'tool_types_list'
FOOD_TYPE_LIST_NM = 'food_types_list'
FOOD_TYPE_DICT_NM = 'food_types_dict'
FOOD_TYPE_DETAILS = f'/food_types/{DETAILS}'
TOOL_TYPE_DICT = f'/check_tool/{DICT}'
INGREDIENTS_GENERATOR_LIST = f'/ingredients_generator/{LIST}'
INGREDIENTS_GENERATOR_LIST_NM = 'ingredients_generator_list'
INGREDIENTS_GENERATOR_DETAILS = f'/ingredients_generator/{DETAILS}'
INGREDIENTS_GENERATOR_DETAIL_NM = 'ingredients_generator_details'
LOGIN = '/templates/login'
USER_DICT = f'/{DICT}'
USER_DICT_W_NS = f'/{USERS_NS}/{DICT}'
USER_DICT_NM = f'{USERS_NS}_{DICT}'
USER_LIST = f'/{LIST}'
USER_LIST_W_NS = f'/{USERS_NS}/{LIST}'
USER_LIST_NM = f'{USERS_NS}_{LIST}'
USER_DETAILS_W_NS = f'/{USERS_NS}/{DETAILS}'
USER_DETAILS = f'/{DETAILS}'
USER_DETAILS_NM = f'{USERS_NS}_details'
USER_COUNT = "/count"
USER_COUNT_NM = f'{USERS_NS}_count'
USER_COUNT_W_NS = f'/{USERS_NS}/count'
USER_ADD = f'/{ADD}'
USER_ADD_W_NS = f'/{USERS_NS}/{ADD}'
USER_ADD_NM = f'{USERS_NS}_{ADD}'
USER_DELETE = f'/{DELETE}'
USER_DELETE_W_NS = f'/{USERS_NS}/{DELETE}'
USER_DELETE_NM = f'{USERS_NS}_delete'
NEW_GAME = f'/Game/{ADD}'
NEW_GAME_NM = f'Game_{ADD}'
GAMES_LIST = f'/{LIST}'
GAMES_LIST_NM = f'{GAMES_NS}_{LIST}'
GAMES_LIST_W_NS = f'/{GAMES_NS}/{LIST}'


# @api.route(HELLO)
# class HelloWorld(Resource):
#     """
#     The purpose of the HelloWorld class is to have a simple test
#     to see if the app is working at all.
#     """

#     def get(self):
#         """
#         Gets the main game menu.
#         """
#         return {MESSAGE: 'hello world'}


@api.route(MAIN_MENU)
class MainMenu(Resource):
    """
    This will deliver our main menu.
    """

    def get(self):
        """
        This is our main menu
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
    This will get a dict of food types
    """

    def get(self):
        """
        Returns a list of tool types.
        """
        return {'Data': ctool.get_tool_types_dict(),
                'Type': 'Data',
                'Title': 'Tool Types'}


@api.route(TOOL_TYPE_LIST)
class ToolTypeList(Resource):
    """
    This will get a list of cook tool types
    """
    def get(self):
        """
        Returns a list of tool types.
        """
        return {TOOL_TYPE_LIST_NM: ftyp.get_tool_types()}


@api.route(FOOD_TYPE_DICT)
class FoodTypeDict(Resource):
    """
    This will get a list of food types
    """

    def get(self):
        """
        Returns a dict of ingredient types.
        """
        return {'Data': ftyp.get_food_type_dict(),
                'Type': 'Data',
                'Title': 'Food Types'}


@api.route(FOOD_TYPE_LIST)
class FoodTypeList(Resource):
    """
    This will get a dict of ingredient types
    """

    def get(self):
        """
        Returns a list of food types.
        """
        return {FOOD_TYPE_LIST_NM: ftyp.get_food_types()}


@api.route(f'{FOOD_TYPE_DETAILS}/<food_type>')
class FoodTypeDetails(Resource):
    """
    This will get a list of details of ingredient types.
    """

    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self, food_type):
        """
        Return a list of food types.
        """
        print(self)
        ft = ftyp.get_food_type_details(food_type)
        if ft is not None:
            return {food_type: ftyp.get_food_type_details(food_type)}
        else:
            raise wz.NotFound(f'{food_type} not found.')


# @api.route(CHAR_TYPE_LIST)
# class CharacterTypeList(Resource):
#     """
#     This will get a list of character types.
#     """
#     def get(self):
#         """
#         Returns a list of character types.
#         """
#         return {CHAR_TYPE_LIST_NM: ctyp.get_char_types()}
# @api.route(CHAR_TYPE_DICT)
# class CharacterTypeDict(Resource):
#     """
#     This will get a list of character types.
#     """
#     def get(self):
#         """
#         Returns a list of character types.
#         """
#         return {'Data': ctyp.get_char_type_dict(),
#                 'Type': 'Data',
#                 'Title': 'Character Types'}


# @api.route(f'{CHAR_TYPE_DETAILS}/<char_type>')
# class CharacterTypeDetails(Resource):
#     """
#     This will get a list of character types.
#     """
#     @api.response(HTTPStatus.OK, 'Success')
#     @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
#     def get(self, char_type):
#         """
#         Returns a list of character types.
#         """
#         ct = ctyp.get_char_type_details(char_type)
#         if ct is not None:
#             return {char_type: ctyp.get_char_type_details(char_type)}
#         else:
#             raise wz.NotFound(f'{char_type} not found.')


# @api.route(INGREDIENTS_GENERATOR_LIST)
# class IngredientsGeneratorList(Resource):
#     """
#     This will get a list of ingredients
#     """
#     def get(self):
#         """
#         Returns a list of ingredients.
#         """
#         return {INGREDIENTS_GENERATOR_LIST_NM: random_ingredients()}


@api.route(INGREDIENTS_GENERATOR_DETAILS)
class IngredientsGeneratorDetails(Resource):
    """
    This will get the price of an ingredient
    """
    def get(self):
        """
        Returns a price
        """
        ingredients = get_ingredients_price_details()
        if ingredients is not None:
            return {INGREDIENTS_GENERATOR_DETAIL_NM: ingredients}
        else:
            wz.NotFound('Ingredients details is not found.')


@users.route(USER_DICT)
class UserDict(Resource):
    """
    This will get a list of the current users.
    """
    def get(self):
        """
        Returns a list of current users.
        """
        return {USER_DICT_NM: usr.get_users_dict()}
        # return {'Data': usr.get_users_dict(),
        #         'Type': 'Data',
        #         'Title': 'List Users'}


@users.route(USER_LIST)
class UserList(Resource):
    """
    This will get a list of the current users.
    """
    def get(self):
        """
        Returns a list of current users.
        """
        return {USER_LIST_NM: usr.get_users()}


@users.route(USER_COUNT)
class UserCount(Resource):
    """
    This will get the number of the users
    """
    def get(self):
        """
        Returns a total number of users count
        """
        return {USER_COUNT_NM: usr.count_user()}


# @api.route(USER_DETAILS_W_NS)
# class UserDetails(Resource):
#     """
#     This will get a user's detail
#     """
#     def get(self):
#         """
#         Returns a user's detail
#         """
#         return {USER_DETAILS_NM: usr.get_user_details(usr.TEST_UID)}


@users.route(f'{USER_DETAILS}/<uid>')
class UserDetails(Resource):
    """
    This will get a user's detail
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self, uid):
        """
        Returns a user's detail
        """
        user_det = usr.get_user_details(uid)
        if user_det is None:
            raise wz.NotFound(f'{uid} not found.')
        return {USER_DETAILS_NM: user_det}


@games.route(GAMES_LIST)
class GameList(Resource):
    """
    This will get a list of the current games.
    """
    def get(self):
        """
        Returns a list of current games.
        """
        return {GAMES_LIST_NM: gm.get_games()}


user_fields_add = api.model('NewUser', {
    usr.NAME: fields.String,
    usr.PASSWORD: fields.String,
    # usr.EMAIL: fields.String,
    # usr.FULL_NAME: fields.String,
})

user_fields_del = api.model('DeleteUser', {
    usr.UID: fields.String,
    # usr.EMAIL: fields.String,
    # usr.FULL_NAME: fields.String,
})

start_fields_add = api.model('StartNewGame', {
    sg.UID: fields.String,
    sg.GID: fields.String,
})


@users.route(USER_ADD)
class AddUser(Resource):
    """
    Add a user.
    """
    @api.expect(user_fields_add)
    def post(self):
        """
        Add a user.
        """
        name = request.json[usr.NAME]
        password = request.json[usr.PASSWORD]
        del request.json[usr.NAME]
        uid = usr.add_user(name, password)
        return {USER_ADD_NM: uid}
        # usr.add_user(name, request.json)


@users.route(USER_DELETE)
class DeleteUser(Resource):
    """
    Delete a user.
    """
    @api.expect(user_fields_del)
    def delete(self):
        """
        Delete a user.
        """
        uid = request.json[usr.UID]
        ret = usr.del_user(uid)
        return {USER_DELETE_NM: ret}


@api.route(NEW_GAME)
class StartGame(Resource):
    """
    Start game for a user
    """
    @api.expect(start_fields_add)
    def post(self):
        uid = request.json[sg.UID]
        gid = request.json[sg.GID]
        data_ls, oid, game_id = sg.start_game(uid, gid)
        return {NEW_GAME_NM: game_id}


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


# HATEOAS
# Global game state
current_order = 'BURGER'
ingredients = ['lettuce', 'tomato', 'onion']
tools = ['Grill', 'RickCooker', 'Oven']


@api.route('/findorder')
class FindOrder(Resource):
    def get(self):
        """
        Find the current order, check if there is an active order
        """
        # global current_order, ingredients, tools
        # Check if there is an active order
        if current_order:
            print("enter1")
            # Example response with HATEOAS links
            response = {
                'message': f'Current order: {current_order}',
                '_links': [
                    {
                        'rel': 'IngredientsGeneratorList',
                        'href': f'/{INGREDIENTS_GENERATOR_LIST}',
                        'method': 'POST',
                        'description': 'Select an ingredient for the order'
                    },
                ]
            }
        return jsonify(response)


@api.route('/ingredient_choice')
class FindIngredient(Resource):
    def get(self):


            # Example response with HATEOAS links
        response = {
            'message': 'see the new generated order with the dish type and ingredients',
            '_links': [
                {
                    "order_id": "current_order",
                    'ingredients': 'Select ingredients for the order',
                    "total_price": "depends on how many correct ingredients player select",
                    'description': 'Your order has been received and will be ready for pickup'
                },
            ]
        }
        return jsonify(response)