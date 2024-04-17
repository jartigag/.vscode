#!/usr/bin/env python3
"""
Script to foo with blah and get bluh as output.
"""

import argparse
import configparser
import logging
import json, os, sys
import traceback

from datetime import datetime, timedelta
from time import time, sleep

# getting config
config_file = "sample_script.snippet.conf"
config      = configparser.ConfigParser()
config.read(config_file)

# settings
# basic
NAME        = "SAMPLE"
__author__  = "@name"
__version__ = '0.1.0'
__date__    = '2000-12-31'

## default options
CONFIG_VAR  = config.get("sample", "CONFIG_VAR")

syslog_logger   = config.get("syslog", "syslog_enable")
syslog_facility = config.get("syslog", "syslog_facility")
syslog_priority = config.get("syslog", "syslog_priority")

log_path = config.get("paths", "logpath")
tmp_path = config.get("paths", "tmppath")

log_file  = config.get("files", "logfile")
logfile   = log_path + log_file


#### Argparser
def cmdArguments(argv=None):
    """ Main entry point of the app """
    # check if argv isn't empty
    if not argv:
        argv = sys.argv

    parse = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)

    # basic options
    parse.add_argument("-V", "--version", dest="version",
                       action="store_true", help="Show version number and exit.")
    parse.add_argument("-v", "--verbose", dest="verbose",
                       action="store_true", help="Increase output verbosity")
    parse.add_argument("-q", "--quiet", dest="quiet",
                       action="store_true", help="Don't show anything on screen.")

    # main options
    main = parse.add_argument_group("Main", "Main options.")
    # TODO: add arguments like --sample:
    # main.add_argument("-S", "--sample", dest="sample", default=config_file, help="A sample argument.")

    try:
        if hasattr(parse, "parse_known_args"):
            (args, arg) = parse.parse_known_args(argv)
        else:
            parse.parse_args(argv)
    except SystemExit:
        raise SystemExit(0)

    for i in range(len(argv)):
        if args.version:
            print("%s\nVersion: %s\nAuthor: %s" %
                  (NAME, __version__, __author__))
            raise SystemExit

    # TODO: check args here:
    # if type(args.sample) != None:
    #    parse.error("Sample error.")

    return args


#### Utils

## read file
def read_txt_file(filename):
    data = ""
    with open(filename, 'r') as f:
        data = f.read()
    return data


## create file
def check_file_exists(filename):
    if not os.path.isfile(filename):
        open(filename, "w").close()


## write to file
def write_txt_file(filename, data):
    with open(filename, "w") as f:
        f.write(data)


# TODO: write functions here


#### Main

def run():
    """ Main entry point of the app """

    ## get start time
    apiStart = time()

    ## start process
    logger.info("Starting process...")

    # TODO: call all the main features from here,
    #       as they should be written as functions

    ## get final time
    apiEnd = time()

    ## calculate scan total time
    ctime = apiEnd - apiStart
    logger.info("Process complete in %s seconds" % (ctime))


if __name__ == "__main__":
    try:
        ## check arguments
        args = cmdArguments()
    except Exception as e:
        print(e)

    try:
        result = 0

        ## create logger
        logger = logging.getLogger(NAME)
        logging.basicConfig(filename=logfile) #TO-DO: args.quiet, syslog_logger, syslog_facility)
        level  = logging.INFO if not args.verbose else logging.DEBUG
        logger.setLevel(level)

        ## and run application
        run()
    except SystemExit as e:
        result = e
        pass
    except KeyboardInterrupt:
        pass
    except Exception as e:
        logger.critical(e)
        logger.critical(traceback.format_exc())
    except RuntimeError as e:
        logger.critical(e)
        logger.critical(traceback.format_exc())
