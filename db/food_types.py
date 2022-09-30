
"""
This module encapsulates details about food type.
"""

TUNA = 'Tuna'
AVOCADO = 'Avocado'
SALMON = 'Salmon'


FOOD_TYPES = {TUNA: {'price': 1},
              AVOCADO: {'price': 1},
              SALMON: {'price': 1}, }


def get_food_types():
    return list(FOOD_TYPES.keys())


def get_food_type_details(food_type):
    return FOOD_TYPES.get(food_type, None)


def main():
    food_types = get_food_types()
    print(food_types)


if __name__ == '__main__':
    main()
