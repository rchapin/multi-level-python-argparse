from multilevelargparse.argparser import ArgParser

class MyAppOne(ArgParser):

    def __init__(self):
        super(MyAppOne, self.__init__())

    @staticmethod
    def add_args(subparsers, parents=[]):
        parents_list = parents.copy()
        parents_list.append(ArgParser.release_version_arg)
        parser = subparsers.add_parser(
            'myappone',
            help='Deploy the MyAppOne app and/or configs',
            parents=parents_list)
        # Given no other sub-commands run the full deploy for the app.
        parser.set_defaults(func=MyAppOne.deploy)

        sub_parser = parser.add_subparsers()

        '''
        Add the sub parsers for each of the sub functions for the MyAppOne
        class.
        '''
        configs_parser = sub_parser.add_parser(
            'configs',
            help='Deploy the MyAppOne configuration files',
            parents=parents_list)
        configs_parser.set_defaults(func=MyAppOne.configs)

        setup_parser = sub_parser.add_parser(
            'setup',
            help='Execute the setup routine for the MyAppOne application',
            parents=parents_list)
        setup_parser.add_argument(
            '--selinux',
            required=False,
            type=bool,
            default=False,
            help='Whether or not to deploy selinux configs during setup')
        setup_parser.set_defaults(func=MyAppOne.setup)

    @staticmethod
    def deploy(args):
        print(f'Running MyAppOne.deploy, args={args}')
        MyAppOne.deploy_app(args)
        MyAppOne.configs(args)

    @staticmethod
    def deploy_app(args):
        print(f'Running MyAppOne.deploy_app, args={args}')

    @staticmethod
    def setup(args):
        print(f'Running MyAppOne.setup, args={args}')

    @staticmethod
    def configs(args):
        print(f'Running MyAppOne.configs, args={args}')
