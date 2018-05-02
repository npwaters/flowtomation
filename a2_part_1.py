#!/usr/bin/python3

import sys
import json
import subprocess
import shlex
from collections import OrderedDict


def process_flow(f):
    # TODO: docstring
    # store our service output to use as input for the next service
    service_output = ''
    for service in flows.get(f):
        result = subprocess.run(
            shlex.split(
                "%s %s" % (
                    services.get(service)["program"],
                    services.get(service)["parameters"])
            ),
            input=service_output,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        service_output = result.stdout


# TODO: handle invalid json etc per specs
configuration = json.load(
        open("test.json"),
        object_pairs_hook=OrderedDict
    )

# get the services
services = configuration.get("services")

# get the flows
flows = configuration.get("flows")


# process the flows

for flow, service_list in flows.items():
    process_flow(flow)
    continue

sys.exit()
