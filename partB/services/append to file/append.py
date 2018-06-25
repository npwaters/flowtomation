#!/usr/bin/python3

import sys
import json

input_string = sys.stdin.read()
string_to_append = json.loads(input_string).get("data")
with open(sys.argv[1], 'a') as output_file:
    output_file.write("{0}\n".format(string_to_append))

sys.exit()
