import yaml
import json


def pars(path_to_file1, path_to_file2):
    if '.yml' in path_to_file1 or '.yaml' in path_to_file2:
        with open(path_to_file1) as file1:
            with open(path_to_file2) as file2:
                data1 = yaml.safe_load(file1)
                data2 = yaml.safe_load(file2)
        return data1, data2

    with open(path_to_file1) as file1:
        with open(path_to_file2) as file2:
            data1 = json.load(file1)
            data2 = json.load(file2)
    return data1, data2
