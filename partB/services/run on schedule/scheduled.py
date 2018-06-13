#!/usr/bin/python3

import sys
import json
import os

content_root = "/".join(os.path.dirname(os.path.realpath(__file__))
                        .split("/")[:-3])
sys.path.insert(
    0,
    content_root
)

from partB import custom_classes_part_2

data = {
    "data": "06/06/2018 10:32:10"
}

data_as_stdout = json.dumps(data)
schedule = custom_classes_part_2.CustomSchedule(5, "M", data_as_stdout)
sys.exit()
