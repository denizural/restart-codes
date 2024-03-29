#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""print_json.py:
# Write a Python script that takes a JSON file as input and performs the following tasks:
# a. Prints the entire JSON file
# b. Prints the value of a specific key in the JSON file (you can choose any key)
# c. Modifies the value of a specific key in the JSON file (you can choose any key)
# d. Writes the modified JSON file to a new file

(Bonus) Create a GitHub repository and upload your code to it. Include a README file that explains how to run your code and what it does.

Submission:
Submit the Python script as a .py file
Submit the link to your GitHub repository.
"""

# import os
import sys
import pathlib
import argparse
import json
import logging
import copy

LOGGING_LEVELS = ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "NOTSET"]


def parse_command_line_args():
    prog_name = pathlib.Path(sys.argv[0]).name

    # command line argument parser
    parser = argparse.ArgumentParser(
        prog=prog_name,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "-f",
        "--file",
        type=str,
        required=True,
        help="path to metadata csv file",
        default=None,
    )

    # choices=LOGGING_LEVELS
    parser.add_argument(
        "-l", "--logging", type=str, help="logging level", default="DEBUG"
    )

    cmd_args = parser.parse_args()
    return cmd_args


def check_command_line_args(cmd_args):
    # check if the file exists
    file_path = pathlib.Path(cmd_args.file)
    if not file_path.is_file():
        err_msg = f"{cmd_args.file} is not a valid file or it does not exist"
        raise ValueError(err_msg)

    # Check if the command line arguments are valid
    if cmd_args.logging not in LOGGING_LEVELS:
        err_msg = f"{cmd_args.logging} is not a valid logging level"
        raise ValueError(err_msg)

    return True


def read_json_file(json_fpath):
    try:
        with open(json_fpath, "rt") as jfile:
            data = json.load(jfile)
            logging.debug(f"successfully read the json file: {json_fpath}")
            return data
    except Exception as err:
        logging.critical(f"ERROR reading the json file: {err}")


if __name__ == "__main__":
    cmd_args = parse_command_line_args()
    check_command_line_args(cmd_args)

    # logging information
    FORMAT = "%(levelname)-8s | %(message)s"
    logging.basicConfig(format=FORMAT, level=cmd_args.logging)

    logging.debug("::: main code is called")
    logging.debug(cmd_args)

    # read the JSON file
    json_data = read_json_file(cmd_args.file)
    
    # back up original file
    json_data_backup = copy.deepcopy(json_data)
    
    # not the best way of updating the value. Use dpath module
    original_value = json_data_backup['quiz']['sport']['q1']['options'][0]
    json_data['quiz']['sport']['q1']['options'][0] = "Hertha Berlin"
    new_value = json_data['quiz']['sport']['q1']['options'][0]
    logging.warning(f"Path that is changing is: ['quiz']['sport']['q1']['options'][0]")
    logging.warning(f"The original value was: {original_value}")
    logging.warning(f"The updated value is: {new_value}")
    
    with open("updated_json_file.json", "wt") as jfile:
        json_object = json.dumps(json_data, indent=4)
        jfile.write(json_object)
        
    
