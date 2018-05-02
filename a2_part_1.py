#!/usr/bin/python3

import sys
import json
import subprocess
import shlex
from collections import OrderedDict

# TODO: handle invalid json etc per specs
configuration = json.load(
        open("test.json"),
        object_pairs_hook=OrderedDict
    )

# execute the services
services = configuration.get("services")

# store our service output to use as input for the next service
service_output = ''

for service_name, service_details in services.items():
    result = subprocess.run(
        shlex.split(
            "%s %s" % (service_details["program"], service_details["parameters"])
        ),
        input=service_output,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    service_output = result.stdout
    continue

sys.exit()
