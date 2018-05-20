#!/usr/bin/python3

"""
returns “true” if the input is a time between 12pm and 6pm, otherwise “false”.
Exits with non zero return code and error message (stderr) if invalid time.
"""

import sys
import custom_classes

input_time = sys.stdin.read()
# input_time = "06/17/2018 10:32:10\n"

afternoon = custom_classes.Afternoon(input_time)
status, result_bytes = afternoon.get_results()

sys.stdout.buffer.write(result_bytes)
sys.exit(status)
