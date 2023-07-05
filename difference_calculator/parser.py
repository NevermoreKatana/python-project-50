import yaml
import json
import argparse


def file_type(path_to_file1, path_to_file2):
    with open(path_to_file1) as file1:
        with open(path_to_file2) as file2:
            if '.yml' in path_to_file1 or '.yaml' in path_to_file2:
                data1 = yaml.safe_load(file1)
                data2 = yaml.safe_load(file2)
                return data1, data2
            data1 = json.load(file1)
            data2 = json.load(file2)
        return data1, data2


def cmd_gendiff():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument("first_file", metavar='<file_path1>')
    parser.add_argument("second_file", metavar='<file_path2>')
    parser.add_argument('-f', '--format', help="set format of output",
                        default=None)

    args = parser.parse_args()
    return args.first_file, args.second_file, args.format
