#!/usr/bin/python3

"""
returns “true” if the input is a time prior to 12pm, otherwise “false”.
Exists if invalid time.
"""

# TODO: create 'time_of_day_service' class and sub class for 'morning' etc
import sys
import custom_classes
# import validate_time

input_time = sys.stdin.read()
# input_time = "06/15/2018 14:32:10\n"

morning = custom_classes.Morning(input_time)
status, result_bytes = morning.get_results()

# status = 0
# result = ""
#
# validated_time = validate_time.convert_datetime_string(
#     input_time
# )
#
# if not validated_time:
#     # provide an error message to stderr,
#     # return code will be 1, and
#     # a CalledProcessError exception will be raised
#     status = "Invalid time given!"
# else:
#     if validated_time.hour < 12:
#         result = "True"
#
# result_bytes = result.encode(sys.stdout.encoding)
sys.stdout.buffer.write(result_bytes)
sys.exit(status)

