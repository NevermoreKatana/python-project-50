import yaml
import json


def read_json_file(path_to_file):
    with open(path_to_file, 'r') as file:
        return json.load(file)


def read_yml_file(path_to_file):
    with open(path_to_file, 'r') as file:
        return yaml.safe_load(file)


def load_files(path_to_file1, path_to_file2):
    if '.yml' in path_to_file1 or '.yaml' in path_to_file2:
        data1 = read_yml_file(path_to_file1)
        data2 = read_yml_file(path_to_file2)
    else:
        data1 = read_json_file(path_to_file1)
        data2 = read_json_file(path_to_file2)
    return data1, data2
