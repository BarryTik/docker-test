import argparse
import subprocess

def get_args():
    """
    :return args: Namespace object containing the command line arguments
    """
    parser = argparse.ArgumentParser("CABINET")

    # Required positional arguments
    parser.add_argument(
        "input",
        help=("Input used by app.")
    )
    parser.add_argument(
        "-l", "--list-dir",
        action="store_true",
        help=("Perform an ls on the input directory.")
    )
    parser.add_argument(
        "-f", "--fail",
        action="store_true",
        help=("Tell the app to error out.")
    )
    args = parser.parse_args()
    return args

def print_ls(dir):
    cmd = ['ls', dir]
    subprocess.check_call(cmd)