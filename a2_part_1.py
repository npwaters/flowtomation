#!/usr/bin/python3

import sys
import json
import subprocess
import shlex
from collections import OrderedDict
import time
import datetime
import os
import enum

# ------------------------------------------------------------------------------
# part 2

class Direction(enum.Enum):
    INBOUND = "input"
    OUTBOUND = "output"


def verify_service_data_format(
        service,
        services,
        service_data,
        direction
):
    """
    -service input will be the output of the preceding service in the flow
    -input will be in the form of a JSON formatted string
    :return:
    """
    # get the data type
    required_data_type = services.get(service)\
        .get(direction)\
        .get("type")

    # get the required format, if one exists

    return

# def get_configuration_part_2(
#         service,
#         service
# ):
#     pass
#
def get_services_part_2():
    # search recursively for config.json files in 'services' directory
    result = ''
    services = {}
    for root, dirs, files in os.walk("services"):
        for file in files:
            if file == "config.json":
                result = "found!"
                service = json.load(
                    open(
                        os.path.join(root, file)
                    ),
                    object_pairs_hook=OrderedDict
                )
                services[service.get("name")] = service
        continue
    return services

# # ------------------------------------------------------------------------------
#
#
# def get_services_part_1():
#
#     return services


def get_configuration_part_1(
        service,
        services,
        service_output
):
    program = services.get(service)["program"]
    parameters = services.get(service)["parameters"]
    # check for special symbol '$$' in parameters
    if "$$" in parameters:
        parameters = parameters.replace("$$", service_output.decode("utf-8"))
    # part 2 only
    # check if the service uses a custom python script
    path = ''
    if "./" in program:
        program = program[2:]
        path = "%s/%s/" % (
            "services",
            # escape any spaces so shlex doesnt split the directory name
            " ".join(["%s\\" % line for line in service.split()])
        )

    command_line = shlex.split(
                    '%s%s %s' % (
                        path,
                        program,
                        parameters
                    ),
                )
    return command_line


def process_flow(f, flows, services):
    # TODO: docstring
    # store our service output to use as input for the next service
    service_output = ''
    for service in flows.get(f):
        # part 2 only
        # verify service input i.e. 'service_output'
        verify_service_data_format(
            service,
            services,
            service_output,
            Direction.INBOUND.value
        )

        # handle a possible exception if the service exits with a non-zero exit code
        try:
            result = subprocess.run(
                get_configuration_part_1(
                    service,
                    services,
                    service_output
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




def main():
    # get the program configuration
    # TODO: handle invalid json etc per specs
    configuration = json.load(
        open("test.json"),
        object_pairs_hook=OrderedDict
    )
    # get the flow configuration
    flows = configuration.get("flows")

    # get the services
    # part 1
    # services = configuration.get("services")

    # part 2
    services = get_services_part_2()


    # process the flows

    while True:
        for flow, service_list in flows.items():
            flow_status = ""
            start_time = datetime.datetime.now()
            if process_flow(flow, flows, services):
                flow_status = "successful!"
            else:
                flow_status = "failed!"
            time_taken = datetime.datetime.now() - start_time
            continue
        time.sleep(1)

    sys.exit()



if __name__ == "__main__":
    main()












