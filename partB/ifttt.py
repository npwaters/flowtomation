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
import enum
from partB import utilities
from partB import validate_time


class Direction(enum.Enum):
    INBOUND = "input"
    OUTBOUND = "output"


def verify_service_data_format(
        service,
        services,
        service_data,
        direction,
        logger
):
    """
    -service input will be the output of the preceding service in the flow
    -input will be in the form of a JSON formatted string
    :return:
    """
    # get the data type
    data_type_configuration = services.get(service)\
        .get(direction)
    required_data_type = data_type_configuration.get("type")
    required_data_format = None
    # get the required format, if one exists
    if "format" in data_type_configuration:
        required_data_format = data_type_configuration.get("format")
    # verify a data type is configured and it is supported
    if not required_data_type:
        logger.warning("service: {0} - does not have an {1} data type configured"
                    .format(service, direction))
        return False
    elif required_data_type not in utilities.supported_data_types:
        logger.error("service: {0} - unsupported data type!"
                     .format(service, direction))
        return False

    # get the data payload
    # service_data = service_data.decode("utf-8")
    try:
        json_message = json.loads(service_data.decode("utf-8"))
    except json.JSONDecodeError as e:
        logger.error("service: {0} - invalid JSON message provided!".format(service))
        return False

    # verify if the message contains the correct 'data' field
    data = json_message.get("data")
    if data is None:
        logger.error("service: {0} - JSON message does not contain the expected 'data' field"
                     .format(service))
        return False

    # we now have the service input/output data
    # the data type we have needs to be 'tested' against the configured data type
    if required_data_type != "time":
        result = isinstance(
            data,
            utilities.supported_data_types.get(required_data_type)
        )
        if not result:
            logger.error("{0} data type does not match required data type"
                         .format(direction))
    else:
        if not required_data_format:
            result = validate_time.convert_datetime_string_part2(data, logger)
        else:
            result = validate_time.convert_datetime_string_part2(data, logger, required_data_format)
    return result


def get_services(
        services,
        file_information,
        logger
):
    # search recursively for config.json files in 'services' directory
    result = ''
    get_failed = False
    for root, dirs, files in os.walk("services"):
        for file in files:
            if file == "config.json":
                # check if file information exists or the config has ben modified
                # service name is the parent directory name
                config_file_path = os.path.join(root, file)
                if utilities.check_file_modified(
                    config_file_path,
                    file_information,
                    logger
                ):
                    # load the service
                    service_directory_name = os.path.basename(root)
                    log_line_prefix = "service in directory: {0} -".format(service_directory_name)
                    # verify if valid JSON via 'load_service'
                    service = utilities.load_service(
                        # services,
                        # service_directory_name,
                        config_file_path,
                        logger
                    )
                    if service:
                        logger.info("{0} passed JSON validation!".format(log_line_prefix))

                    else:
                        logger.error("{0} failed JSON validation!".format(log_line_prefix))
                        return False
                    # verify configuration
                    # configuration = services.get(service_directory_name)
                    # if not configuration:
                    #     logger.error("directory name and service name for service {0} do not match"
                    #                  .format(service_directory_name))
                    #     return False

                    if utilities.verify_configuration(
                            service,
                            utilities.required_keys.get("service_configuration"),
                            logger
                    ):
                        logger.info("{0} passed configuration verification!".format(log_line_prefix))
                        # load the service into running configuration
                        # TODO: issue loading service with same name?
                        service_name = service.get("name")
                        if service_name not in services:
                            services[service_name] = service
                        else:
                            logger.error("service with the same exists in the running configuration")
                            get_failed = True

                    else:
                        logger.error("{0} failed configuration verification".format(log_line_prefix))
                        # remove the service from running configuration
                        # remove the service if it is already installed

                        if service.get("name") in services:
                            del services[service.get("name")]
                        # del services[service_directory_name]
                        get_failed = True
        continue
    if get_failed:
        return False
    return True

# # ------------------------------------------------------------------------------
#
#
# def get_services_part_1():
#
#     return services


def get_command_line(
        service,
        services,
        service_output
):
    program = services.get(service).get("program")
    parameters = services.get(service).get("parameters")
    # check for special symbol '$$' in parameters
    if parameters and "$$" in parameters:
        parameters = parameters.replace("$$", service_output)
    # check if the service uses a custom python script
    path = ''
    if "./" in program:
        program = program[2:]
        path = "%s/%s/" % (
            "services",
            # escape any spaces so shlex doesnt split the directory name
            " ".join(["%s\\" % line for line in service.split()])
        )

    if parameters:
        command_line = shlex.split(
                    '%s%s %s' % (
                        path,
                        program,
                        parameters
                    ),
                )
    else:
        command_line = shlex.split(
            '%s%s' % (
                path,
                program,
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
        # verify service input i.e. 'service_output'
        if service_output and not verify_service_data_format(
            service,
            services,
            service_output,
            Direction.INBOUND.value,
            logger
        ):
            logger.error("service: {0} - failed input data type verification"
                         .format(service))
            return False

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
            if service_output and not verify_service_data_format(
                service,
                services,
                service_output,
                Direction.OUTBOUND.value,
                logger
            ):
                logger.error("service: {0} - failed output data type verification!"
                             .format(service))
                return False
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

    flow_configuration_file = ''
    # get the configuration file from the command line if one supplied
    try:
        flow_configuration_file = sys.argv[1]
    except IndexError:
        logger.info("configuration file not supplied as argument - using default")
        flow_configuration_file = "ifttt.json"

    # get the program configuration
    # get the services
    services = {}
    file_information = {}

    # process the flows
    while True:
        logger.info("waiting for next flow start time ...")
        if utilities.flow_start_time():
            logger.info("it's go time!")
            # update/check the flow configuration file modified time
            modified = utilities.check_file_modified(
                flow_configuration_file,
                file_information,
                logger
            )
            if modified:
                # load the flow configuration
                try:
                    configuration = json.load(
                        open(flow_configuration_file),
                        object_pairs_hook=OrderedDict
                    )
                    logger.info("configuration loaded!")
                except json.JSONDecodeError as e:
                    error_message = "Failed to load program configuration " \
                                    "- Invalid JSON detected on/near line: {0}"\
                        .format(e.lineno - 1)
                    logger.critical(error_message)
                    sys.exit(error_message)

                # verify the mandatory configuration fields
                if not utilities.verify_configuration(
                    configuration,
                    utilities.required_keys.get("program_configuration_2"),
                    logger
                ):
                    error_message = "Failed to load program configuration " \
                                    "- configuration file missing mandatory section"
                    logger.critical(error_message)
                    sys.exit(error_message)

                # get the flow configuration
                flows = configuration.get("flows")
                logger.info("got the flows!")
            # update/check the service configuration files modified time
            # and load any new/updated service configurations
            if get_services(
                services,
                file_information,
                logger
            ):
                logger.info("got the services!")
            else:
                logger.warning("Error encountered getting services - please review the service configurations")
                # sys.exit("Error encountered loading services - see log file for details")

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

    sys.exit()


if __name__ == "__main__":
    main()












