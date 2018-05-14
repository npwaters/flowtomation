import logging
import sys
import os
import json
from collections import OrderedDict
import time
import datetime


def setup_logger(
        name,
        log_level="INFO"
):
    level = logging.getLevelName(log_level)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    log_file_name = "a2.log"
    fh = logging.FileHandler(
        filename=log_file_name
    )
    fh.setLevel(level)
    formatter = logging.Formatter(
        '%(asctime)s: %(levelname)s: %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p'
    )
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger


def check_file_modified(
        file_name,
        file_information,
        logger
):
    """

    :param logger:
    :param file_name:
    :param file_information:
    :return:
    """

    result = ''
    file_info = os.stat(file_name)
    file_current_modified_time = file_info.st_mtime
    # TODO: do we need this check?

    if not file_information.get(file_name):
        file_information[file_name] = {}
        file_information.get(file_name)["file_last_modified"] = file_current_modified_time
        logger.info("no modified information found - first run")
        logger.info("last modified time created for file: {0}".format(file_name))
        return True
    else:
        file_last_modified_time = file_information.get(file_name)["file_last_modified"]

    if file_last_modified_time < file_current_modified_time:
        file_information.get(file_name)["file_last_modified"] = file_current_modified_time
        logger.info("last modified time updated for file: {0}".format(file_name))
        return True
    else:
        logger.info("no changes detected since last run for file: {0}".format(file_name))
        return False


def load_service(
        services,
        service_name,
        config_file,
        logger
):
    # TODO: verify config file (JSON) format
    try:
        service = json.load(
            open(
                config_file
            ),
            object_pairs_hook=OrderedDict
        )
        services[service.get("name")] = service
    except json.JSONDecodeError as e:
        error_message = "Failed to load configuration - Invalid JSON detected on line: {0}".format(e.lineno - 1)
        logger.warning(error_message)
        # remove the service if it is already installed
        if service_name in services:
            del services[service_name]
        return False
    else:
        return True


def flow_ready_to_run(
        services,
        flows,
        flow,
        logger
):
    flow_ready = True
    missing_services = []
    logger.info("checking availability of services configured in flow: {0}".format(flow))
    for service in flows.get(flow):
        if not services.get(service):
            logger.error("service: {0} - does not exist!".format(service))
            missing_services.append(service)
            flow_ready = False
    if not flow_ready:
        logger.warning("flow: {0} - will be skipped due to missing service(s):".format(flow))
        for m in missing_services:
            logger.info(" - {0}".format(m))
        return False
    else:
        logger.info("flow: {0} - is ready to run".format(flow))
        return True


def flow_start_time():

    second = None

    while second != 0:
        second = datetime.datetime.now().second
        time.sleep(1)
    return True
