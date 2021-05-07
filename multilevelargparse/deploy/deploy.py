import sys
from multilevelargparse.argparser import ArgParser
from multilevelargparse.deploy.complete_stack import CompleteStack
from multilevelargparse.deploy.myappone import MyAppOne
from multilevelargparse.deploy.myapptwo import MyAppTwo
from multilevelargparse.deploy.system import System

class Deploy(ArgParser):
    '''
    Class that encapsulates the deployment of a fictitious system.
    '''
    parser = None

    def __init__(self):
        super(Deploy, self.__init__())

    @staticmethod
    def add_args(subparsers, parents=[]):
        Deploy.parser = subparsers.add_parser(
            'deploy',
            help=(
                'Deploys system level components, applications, and configs '
                'type \"deploy --help\" for more details'),
            parents=parents)
        '''
        There is no overall target function for the Deploy class so we will
        point it to a function that will print out the help and then add the
        sub parsers.
        '''
        Deploy.parser.set_defaults(func=Deploy.deploy)

        subparser = Deploy.parser.add_subparsers()
        CompleteStack.add_args(subparser, parents)
        MyAppOne.add_args(subparser, parents)
        MyAppTwo.add_args(subparser, parents)
        System.add_args(subparser, parents)

    @staticmethod
    def deploy(_args):
        '''
        As there are no specific tasks for this parser, print the help which
        will list all of the sub-choices for this branch.
        '''
        Deploy.parser.print_help(sys.stderr)
