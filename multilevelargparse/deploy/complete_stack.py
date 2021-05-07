from multilevelargparse.argparser import ArgParser
from multilevelargparse.deploy.myappone import MyAppOne
from multilevelargparse.deploy.myapptwo import MyAppTwo

class CompleteStack(ArgParser):

    def __init__(self):
        super(CompleteStack, self.__init__())

    @staticmethod
    def add_args(subparsers, parents=[]):
        parent_args = parents.copy()
        parent_args.append(ArgParser.release_version_arg)
        parser = subparsers.add_parser(
            'complete-stack',
            help='Deploy the complete application stack',
            parents=parent_args)
        parser.set_defaults(func=CompleteStack.deploy)

    @staticmethod
    def deploy(args):
        '''
        Call each of the deployment targets for all of the applications in the
        stack.
        '''
        print(f'From CompleteStack.deploy, deploying the whole thing, args={args}')
        MyAppOne.deploy(args)
        MyAppTwo.deploy(args)
