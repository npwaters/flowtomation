#!/usr/bin/python3

"""
returns “true” if the input is a time after (past 6pm), otherwise “false”.
Exits with non zero return code and error message (stderr) if invalid time.
"""

import sys
sys.path.append('/tmp/pycharm_project_926')

from partB import custom_classes_part_2


input_time = sys.stdin.read()
# input_time = "60/11/2018 7:32:10\n"

evening = custom_classes_part_2.Evening(input_time)
status, result_bytes = evening.get_results()

sys.stdout.buffer.write(result_bytes)
sys.exit(status)
