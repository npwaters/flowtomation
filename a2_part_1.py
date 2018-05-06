#!/usr/bin/python3

import sys
import json
import subprocess
import shlex
from collections import OrderedDict
import time


def process_flow(f):
    # TODO: docstring
    # store our service output to use as input for the next service
    service_output = ''
    for service in flows.get(f):
        # handle a possible exception if the service exits with a non-zero exit code
        try:
            result = subprocess.run(
                shlex.split(
                    "%s %s" % (
                        services.get(service)["program"],
                        services.get(service)["parameters"]
                    )
                ),
                input=service_output,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True
            )
            service_output = result.stdout
        except subprocess.CalledProcessError as e:
            result = e
            pass
        # return error code if stderr
        status = result.returncode
        continue


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

while True:
    for flow, service_list in flows.items():
        process_flow(flow)
        continue
    time.sleep(1)

sys.exit()
