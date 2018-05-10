import sys
import numbers
import json
import datetime


def test_boolean(data):
    if data == "True" or data == "False":
        return True
    else:
        return False


supported_data_types = {
    "number": numbers.Number,
    "string": str,
    "dictionary": dict,
    "array": list,
    "boolean": bool,
    "time": datetime.datetime
}

my_object = [1, 2, ]

message = {
    "data": "06/11/2018 10:32:10\n"
}

json_message = json.dumps(message)
data = json.loads(
    json_message
).get("data")

result = isinstance(
    data,
    supported_data_types.get("time")
)
sys.exit()
