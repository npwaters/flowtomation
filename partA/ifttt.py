#!/usr/bin/python3

import sys
import os

content_root = "/".join(os.path.dirname(os.path.realpath(__file__))
                        .split("/")[:-1])
sys.path.insert(
    0,
    content_root
)
import json
import subprocess
import shlex
from collections import OrderedDict
import time
import datetime
import os
import enum
from partA import utilities

# def get_services_part_1():
#
#     return services


def get_command_line(
        service,
        services,
        service_output
):
    program = services.get(service)["program"]
    parameters = services.get(service)["parameters"]
    # check for special symbol '$$' in parameters
    if "$$" in parameters:
        parameters = parameters.replace("$$", service_output.decode("utf-8"))

    command_line = shlex.split(
                    '%s %s' % (
                        program,
                        parameters
                    ),
                )
    return command_line


def process_flow(f, flows, services, logger):
    # store our service output to use as input for the next service
    service_output = ''

    # check if all services listed in the flow loaded successfully
    if not utilities.flow_ready_to_run(
            services,
            flows,
            f,
            logger
    ):
        return False

    for service in flows.get(f):
        # handle a possible exception if the service exits with a non-zero exit code
        # -service file/command not found
        # -permission issue on service file
        logger.info("running service {0} ...".format(service))
        try:
            result = subprocess.run(
                get_command_line(
                    service,
                    services,
                    service_output
                ),
                input=service_output,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True
            )
            status = result.returncode
            service_output = result.stdout
        except (
                subprocess.CalledProcessError,
                FileNotFoundError,
                PermissionError
        ) as e:
            result = e
            if type(result) == FileNotFoundError:
                status = result.errno
                logger.error(result.strerror)
            if type(result) == PermissionError:
                status = result.errno
                logger.error(result.strerror)
            if type(result) == subprocess.CalledProcessError:
                status = result.returncode
                logger.error(result.stderr)

        # exit flow on non-zero return code
        if status != 0:
            return False
        continue
    return True


def main():
    # setup logging
    logger = utilities.setup_logger("CPT223 A2")

    program_configuration_file = ''
    # get the configuration file from the command line if one supplied
    try:
        program_configuration_file = sys.argv[1]
    except IndexError:
        logger.info("configuration file not supplied as argument - using default")
        program_configuration_file = "ifttt.json"

    # get the program configuration
    try:
        configuration = json.load(
            open(program_configuration_file),
            object_pairs_hook=OrderedDict
        )
        logger.info("configuration loaded!")
    except json.JSONDecodeError as e:
        error_message = "Failed to load configuration - Invalid JSON detected on/near line: {0}".format(e.lineno - 1)
        logger.critical(error_message)
        sys.exit(error_message)
    # verify the mandatory configuration fields
    if not utilities.verify_configuration(
            configuration,
            utilities.required_keys.get("program_configuration_1"),
            logger
    ):
        error_message = "Failed to load program configuration " \
                        "- configuration file missing mandatory section"
        logger.critical(error_message)
        sys.exit(error_message)

    # get the flow configuration
    flows = configuration.get("flows")
    logger.info("got the flows!")

    # get the services
    # part 1
    services = configuration.get("services")

    # process the flows
    while True:

        logger.info("waiting for next flow start time ...")
        if utilities.flow_start_time():
            logger.info("it's go time!")

            logger.info("starting flows")
            for flow, service_list in flows.items():
                logger.info("running flow: {0}".format(flow))
                flow_status = ""
                start_time = datetime.datetime.now()
                # check the status of the flow
                log_line_prefix = "flow: {0} status -".format(flow)
                if process_flow(flow, flows, services, logger):
                    flow_status = "successful!"
                    logger.info("{0} successful!".format(log_line_prefix))
                else:
                    flow_status = "failed!"
                    logger.warning("{0} failed!".format(log_line_prefix))
                time_taken = datetime.datetime.now() - start_time
                # we need to wait until at least one second has elapsed
                # so we dont run more than once if the flow run time
                # is < one second
                if time_taken.seconds < 1:
                    time.sleep(1)
                continue
        # time.sleep(1)

    sys.exit()


if __name__ == "__main__":
    main()












