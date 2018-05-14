import logging
import sys
import os
import json
from collections import OrderedDict


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
        config_file
):
    # TODO: verify config file (JSON) format
    service = json.load(
        open(
            config_file
        ),
        object_pairs_hook=OrderedDict
    )
    services[service.get("name")] = service
