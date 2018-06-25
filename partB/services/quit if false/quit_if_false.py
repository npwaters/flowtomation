#!/usr/bin/python3

"""
Exits with non zero return code and error message (stderr) if input is False.
"""

import sys
import json


input_string = sys.stdin.read()
# input_string = "Hello World!"
status = 0

if not json.loads(input_string).get("data"):
    status = "The input is False"

sys.exit(status)

