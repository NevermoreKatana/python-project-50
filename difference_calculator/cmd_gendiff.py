import argparse


def cmd_gendiff():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument("first_file", metavar='first_file')
    parser.add_argument("second_file", metavar='second_file')
    parser.add_argument('-f', '--format', help="set format of output",
                        default=None)

    args = parser.parse_args()
    return args.first_file, args.second_file, args.format
