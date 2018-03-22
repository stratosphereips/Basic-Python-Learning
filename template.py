#!/usr/bin/env python3.6 -u
# Copyright?
# Author: xxxxx xx@asdf.com

import argparse

__version__ = '0.1'


def do():
    """
    Do function does ...
    Param 1:
    """
    pass



####################
# Main
####################
if __name__ == '__main__':  
    # Parse the parameters
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description="Program xxx version {}. Author: xxx".format(__version__), usage='%(prog)s -n <screen_name> [options]')
    parser.add_argument('-v', '--verbose', help='Amount of verbosity. This shows more info about the results.', action='store', default=0, required=False, type=int)
    parser.add_argument('-d', '--debug', help='Amount of debugging. This shows inner information about the flows.', action='store', default=0, required=False, type=int)
    parser.add_argument('-f', '--filename', help='File.', action='store', required=False)
    args = parser.parse_args()

    if args.filename:
        print('File: {}'.format(args.filename))

    # Print a dot of ips relationships
