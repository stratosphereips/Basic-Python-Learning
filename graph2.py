#!/usr/bin/env python3.6 -u
# Copyright?
# Author: xxxxx xx@asdf.com

import argparse

__version__ = '0.1'


def do(filename, maxlines):
    """
    Do function does ...
    Param 1:
    """
    f = open(filename)
    line = f.readline()
    # Avoid the header
    line = f.readline()
    print('digraph graphname {')
    line_number = 0
    prev_dip = ''
    while line and line_number <= maxlines :
        fields = line.split(',')
        dip = fields[6]
        if ':' in dip:
            line = f.readline()
            continue
        if args.debug > 0:
            print('Prev_dip: {}, dip: {}'.format(prev_dip,dip))
        if prev_dip:
            print('\t\"{}\" -> \"{}\";'.format(prev_dip,dip))
        prev_dip = dip
        line = f.readline()
        line_number += 1

    print('}')



####################
# Main
####################
if __name__ == '__main__':  
    # Parse the parameters
    parser = argparse.ArgumentParser(description="Program xxx version {}. Author: xxx".format(__version__), usage='%(prog)s -n <screen_name> [options]')
    parser.add_argument('-v', '--verbose', help='Amount of verbosity. This shows more info about the results.', action='store', default=0, required=False, type=int)
    parser.add_argument('-d', '--debug', help='Amount of debugging. This shows inner information about the flows.', action='store', default=0, required=False, type=int)
    parser.add_argument('-f', '--filename', help='File.', action='store', required=False)
    parser.add_argument('-m', '--maxlines', help='Max lines to process.', action='store', type=int, default=200, required=False)
    args = parser.parse_args()

    if args.filename:
        if args.verbose > 0:
            print('File: {}'.format(args.filename))
        do(args.filename, args.maxlines)

    # Print a dot of ips relationships
