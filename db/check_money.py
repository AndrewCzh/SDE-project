
"""
This module encapsulates details about check money.
"""

money = 110
threshold = 100


def check_money():
    return money >= threshold


def get_money_types():
    return money


def main():
    ret = check_money()


if __name__ == '__main__':
    main()
