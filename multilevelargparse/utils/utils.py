import sys
from multilevelargparse.argparser import ArgParser
from multilevelargparse.utils.dns import Dns

class Utils(ArgParser):
    '''
    Class that encapsulates deployment of the entire system.
    '''
    parser = None

    def __init__(self):
        super(Utils, self.__init__())

    @staticmethod
    def add_args(subparsers, parents=[]):
        Utils.parser = subparsers.add_parser(
            'utils',
            help='Various utility programs. Type \"utils --help\" for more details',
            parents=parents)
        '''
        There is no overall target function for the Utils class so we will
        point it to a function that will print out the help and then add the
        it's sub parsers.
        '''
        Utils.parser.set_defaults(func=Utils.utils)

        subparser = Utils.parser.add_subparsers()
        Dns.add_args(subparser, parents)

    @staticmethod
    def utils(_args):
        '''
        As there are no specific tasks for this parser, print the help which
        will list all of the sub-choices for this branch.
        '''
        Utils.parser.print_help(sys.stderr)
