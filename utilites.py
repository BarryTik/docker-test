import argparse

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
        "-d", "--double",
        action="store_true",
        help=("Print twice.")
    )
    parser.add_argument(
        "-f", "--fail",
        action="store_true",
        help=("Tell the app to error out.")
    )
    args = parser.parse_args()
    return args