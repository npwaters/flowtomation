#!/usr/bin/python3

import sys
import os
# sys.path.append('/tmp/pycharm_project_926')
content_root = "/".join(os.path.dirname(os.path.realpath(__file__))
                        .split("/")[:-3])

# content_root = os.path.dirname(os.path.realpath(__file__))
# print("***content root = {0}*****".format(content_root))
sys.path.insert(
    0,
    content_root
)
python_path = sys.path
# for path in python_path:
#     print(path)

import test_package.target_module


print("hello world!")
sys.exit()
