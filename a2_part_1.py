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

for service_name, service_details in services.items():
    result = subprocess.run(
        shlex.split(
            "%s %s" % (service_details["program"], service_details["parameters"])
        ),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    continue

sys.exit()
