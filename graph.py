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
    while line and line_number <= maxlines :
        fields = line.split(',')
        sip = fields[3]
        dip = fields[6]
        if ':' in sip or ':' in dip:
            line = f.readline()
            continue
        if args.debug > 0:
            print('Sip: {}, dip: {}'.format(sip,dip))
        print('\t\"{}\" -> \"{}\";'.format(sip,dip))
        line = f.readline()
        line_number += 1

    print('}')


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
        if args.verbose > 0:
            print('File: {}'.format(args.filename))
        do(args.filename, 200)

    # Print a dot of ips relationships
