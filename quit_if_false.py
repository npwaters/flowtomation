#!/usr/bin/python3

"""
Exits with non zero return code and error message (stderr) if input is false.
"""

import sys


input_string = sys.stdin.read()
# input_string = "Hello World!"
status = 0

if not input_string:
    status = "The input is false"

sys.exit(status)

