import json
import sys
from collections import OrderedDict


result = ''

try:
    configuration = json.load(
                open("test.json"),
                object_pairs_hook=OrderedDict
            )
except json.JSONDecodeError as e:
    # check if there are blank lines between reported line and issue
    # target_file = e.doc.rea
    result = e
    pass



sys.exit()
