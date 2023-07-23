import argparse


def get_parser():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument("first_file", metavar='<file_path1>')
    parser.add_argument("second_file", metavar='<file_path2>')
    parser.add_argument('-f', '--format', help="set format of output",
                        default='stylish')

    return parser
