#!/usr/bin/python3

"""
negates the input - True to False, False to True.
Exits with non zero return code and error message (stderr) if not one of those values.
"""

import sys


# input_string = sys.stdin.read()
input_string = ""
result = ""

if not input_string:
    result = "True"

result_bytes = result.encode(sys.stdout.encoding)
sys.stdout.write(result_bytes)


