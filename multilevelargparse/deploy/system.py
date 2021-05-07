import sys
from multilevelargparse.argparser import ArgParser

class System(ArgParser):

    parser = None

    def __init__(self):
        super(System, self.__init__())

    @staticmethod
    def add_args(subparsers, parents=[]):
        parent_args = parents.copy()
        parent_args.append(ArgParser.release_version_arg)
        '''
        Here we set the parents to the original list of parent arguments
        instead of the list into which we added the required version argument.
        Otherwise, there would be a conflict and when we execute CLI arguments
        that target one of the System's sub parsers it would complain that it
        did not see the \"version\" argument for the sub parser even if it was
        provided.
        '''
        System.parser = subparsers.add_parser(
            'system',
            help='Deploy system level components and configs',
            parents=parents)
        '''
        There is no overall target function for the System class so we will
        point it to a function that will print out the help and then add the
        it's sub parsers.
        '''
        System.parser.set_defaults(func=System.system)

        subparser = System.parser.add_subparsers()
        base_setup_parser = subparser.add_parser(
            'basesetup',
            help='Execute the base setup of all of the hosts in the system',
            parents=parent_args)
        base_setup_parser.set_defaults(func=System.base_setup)

        installjava_parser = subparser.add_parser(
            'installjava',
            help='Install the OpenJDK on the specified hosts',
            parents=parent_args)
        installjava_parser.set_defaults(func=System.install_java)
        installjava_parser.add_argument(
            '--openjdkversion',
            required=True,
            type=str,
            help='Version of the OpenJDK to install')

    @staticmethod
    def base_setup(args):
        print(f'Running System.base_setup, args={args}')

    @staticmethod
    def install_java(args):
        print(f'Running System.install_java, args={args}')

    @staticmethod
    def system(_args):
        '''
        As there are no specific tasks for this parser, print the help which
        will list all of the sub-choices for this branch.
        '''
        System.parser.print_help(sys.stderr)
