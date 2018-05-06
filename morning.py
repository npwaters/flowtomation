#!/usr/bin/python3

"""
returns “true” if the input is a time prior to 12pm, otherwise “false”.
Exists if invalid time.
"""

# TODO: create 'time_of_day_service' class and sub class for 'morning' etc
import sys
import custom_classes

input_time = sys.stdin.read()
# input_time = "06/15/2018 14:32:10\n"

morning = custom_classes.Morning(input_time)
status, result_bytes = morning.get_results()

sys.stdout.buffer.write(result_bytes)
sys.exit(status)

