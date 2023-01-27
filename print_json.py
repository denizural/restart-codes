#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""print_json.py:
# Write a Python script that takes a JSON file as input and performs the following tasks:
# a. Prints the entire JSON file
# b. Prints the value of a specific key in the JSON file (you can choose any key)
# c. Modifies the value of a specific key in the JSON file (you can choose any key)
# d. Writes the modified JSON file to a new file
"""

import os
import pathlib
import argparse
import json
import logging

LOGGING_LEVELS = ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "NOTSET"]

# logging information
FORMAT = '%(levelname)-8s | %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)


if __name__ == "__main__":
    logging.debug("::: main code is called")