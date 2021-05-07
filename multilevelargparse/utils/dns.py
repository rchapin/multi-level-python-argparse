import argparse
import sys
from multilevelargparse.argparser import ArgParser

class Dns(ArgParser):

    parser = None

    def __init__(self):
        super(Dns, self.__init__())

    @staticmethod
    def add_args(subparsers, parents=[]):
        Dns.parser = subparsers.add_parser(
            'dns',
            help='DNS utilities',
            parents=parents)
        '''
        There is no overall target function for the Dns class so we will
        point it to a function that will print out the help and then add the
        sub parsers.
        '''
        Dns.parser.set_defaults(func=Dns.dns)

        # Add a common argument that all dns functions will use
        dnsthing_args = parents.copy()
        hostname_arg = argparse.ArgumentParser(add_help=False)
        hostname_arg.add_argument(
            '--hostname',
            required=True,
            type=str,
            help='Hostname against which dnsthing will be exectuted')
        dnsthing_args.append(hostname_arg)

        sub_parser = Dns.parser.add_subparsers()

        dnsthing1_parser = sub_parser.add_parser(
            'dnsthing1',
            help='Do the dns1 thing',
            parents=dnsthing_args)
        dnsthing1_parser.set_defaults(func=Dns.dnsthing_1)

        dnsthing1_parser = sub_parser.add_parser(
            'dnsthing2',
            help='Do the dns2 thing',
            parents=dnsthing_args)
        dnsthing1_parser.set_defaults(func=Dns.dnsthing_2)

    @staticmethod
    def dns(_args):
        '''
        As there are no overall function for this parser, print the help which
        will list all of the sub-choices for this branch.
        '''
        Dns.parser.print_help(sys.stderr)

    @staticmethod
    def dnsthing_1(args):
        print(f'Running Dns.dnsthing_1, args={args}')

    @staticmethod
    def dnsthing_2(args):
        print(f'Running Dns.dnsthing_2, args={args}')

