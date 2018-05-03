#!/usr/bin/python3

"""
returns “true” if the input is a time prior to 12pm, otherwise “false”.
Exists if invalid time.
"""

import sys
import validate_time

input_time = sys.stdin.read()
# input_time = "24/05/2018 27:04:31"
status = 0
result = ""

validated_time = validate_time.convert_datetime_string(
    input_time
)

if not validated_time:
    status = -1
else:
    if validated_time.hour < 12:
        result = "True"

result_bytes = result.encode(sys.stdout.encoding)
sys.stdout.buffer.write(bytes)
sys.exit(status)

