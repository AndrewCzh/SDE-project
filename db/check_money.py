
"""
This module encapsulates details about check money.
"""

money = 110
threshold = 100

def check_money():
    return money >= threshold

def get_money_types():
    return money


def get_food_type_details(food_type):
    return FOOD_TYPES.get(food_type, None)


def main():
    food_types = get_food_types()
    print(food_types)


if __name__ == '__main__':
    main()
