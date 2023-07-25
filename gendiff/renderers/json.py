import json
from gendiff.diff_finder import find_diff


def generate_diff_json(data1, data2):
    diff_tree = find_diff(data1, data2)
    diff = json.dumps(diff_tree, indent=2)
    return diff
