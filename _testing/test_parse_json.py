import sys
import json
import datetime


# json_file = json.load(open("test.json"))
# message = {
#     "data": [
#         1,
#         2,
#         3,
#     ]
# }

message = {
    "data": True
}

json_message = json.dumps(message)
data = json.loads(
    json_message
).get("data")
sys.exit()
