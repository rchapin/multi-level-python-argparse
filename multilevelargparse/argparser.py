import argparse
from abc import ABC, abstractmethod

class ArgParser(ABC):

    release_version_arg = argparse.ArgumentParser(add_help=False)
    release_version_arg.add_argument(
        '--version',
        required=True,
        type=str,
        help='Release version to be deployed')

    @staticmethod
    @abstractmethod
    def add_args(subparsers, parents=[]) -> None:
        pass
