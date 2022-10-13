
"""
This module encapsulates details about food type.
"""

OVEN = 'Oven'
GRILL = 'Grill'
RICE_COOKER = 'Rice_cooker'


TOOL_TYPES = {OVEN: {'price': 1},
              GRILL: {'price': 1},
              RICE_COOKER: {'price': 1}, }


def get_tool_types():
    return list(TOOL_TYPES.keys())


def get_tool_type_details(tool_type):
    return TOOL_TYPES.get(tool_type, None)


def main():
    tool_types = get_tool_types()
    print(tool_types)


if __name__ == '__main__':
    main()
