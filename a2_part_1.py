#!/usr/bin/python3

import sys
import json
import subprocess
import shlex
from collections import OrderedDict
import time
import datetime


def process_flow(f):
    # TODO: docstring
    # store our service output to use as input for the next service
    service_output = ''
    for service in flows.get(f):
        program = services.get(service)["program"]
        parameters = services.get(service)["parameters"]
        # check for special symbol '$$' in parameters
        if "$$" in parameters:
            parameters = parameters.replace("$$", service_output.decode("utf-8"))

        # handle a possible exception if the service exits with a non-zero exit code
        try:
            result = subprocess.run(
                shlex.split(
                    "%s %s" % (
                        program,
                        parameters
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

        # exit flow on non-zero return code
        if status != 0:
            return False
        continue
    return True


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
        flow_status = ""
        start_time = datetime.datetime.now()
        if process_flow(flow):
            flow_status = "successful!"
        else:
            flow_status = "failed!"
        time_taken = datetime.datetime.now() - start_time
        continue
    time.sleep(1)

sys.exit()
