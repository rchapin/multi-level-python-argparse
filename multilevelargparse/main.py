import argparse
import os
import sys
from multilevelargparse.deploy.deploy import Deploy
from multilevelargparse.utils.utils import Utils

def parse_args():
    top_parser = argparse.ArgumentParser()

    '''
    Add an example set of common, top-level arguments.

    We MUST set add_help=False on this parser so that there is no conflict
    with other parsers that define a help.
    '''
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument(
        '--tracelevel',
        choices=('error', 'warn', 'info', 'debug'),
        default='info',
        help='Python trace logging level. Default: info')
    common.add_argument(
        '--log-dir',
        default=os.getenv('LOG_DIR', '/var/tmp'),
        help='Logging directory')

    '''
    Create a sub parser into which we will add all of our top level branches
    and/or targets.
    '''
    subparsers = top_parser.add_subparsers()
    Deploy.add_args(subparsers, [common])
    Utils.add_args(subparsers, [common])

    # If the user has not provided any arguments at all, print the help.
    if len(sys.argv) == 1:
        top_parser.print_help(sys.stderr)
        sys.exit(1)

    return top_parser.parse_args(), top_parser

def main():
    args, parser = parse_args()
    '''
    If the user has selected a branch in the tree for which there is no
    defined function print the help.
    '''
    if 'func' not in args:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args.func(args)

###########################################################
# MAIN
###########################################################

if __name__ == '__main__':
    main()
