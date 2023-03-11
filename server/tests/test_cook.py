import sys
from bson.json_util import loads

sys.path.append("..")
import server.cook as ck

# Test function with a wrong tool name
def test_wrong_tool():
    check_tool("measuring_cups", "potato masher")
