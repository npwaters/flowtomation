#!/usr/bin/python3

"""
returns “true” if the input is a time prior to 12pm, otherwise “false”.
Exists if invalid time.
"""

import sys
import validate_time

# input_time = sys.stdin.read()
input_time = "35/05/2018 27:04:31"
status = 0
result = ""

validated_time = validate_time.convert_datetime_string(
    input_time
)

if not validated_time:
    # provide an error message to stderr,
    # return code will be 1, and
    # a CalledProcessError exception will be raised
    status = "Invalid time given!"
else:
    if validated_time.hour < 12:
        result = "True"

result_bytes = result.encode(sys.stdout.encoding)
sys.stdout.buffer.write(result_bytes)
sys.exit(status)

