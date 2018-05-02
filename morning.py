#!/usr/bin/python3

"""
returns “true” if the input is a time prior to 12pm, otherwise “false”.
Exists if invalid time.
"""

import sys
import datetime

# input_time = sys.stdin.read()
input_time = "24/05/2018 12:04:31"
status = ''

try:
    validated_time = datetime.datetime.strptime(
        input_time,
        "%d/%m/%Y %H:%M:%S"
    )
except ValueError:
    # exit with status code
    status = "failed!"
    pass
else:
    status = "success!"


sys.exit()

