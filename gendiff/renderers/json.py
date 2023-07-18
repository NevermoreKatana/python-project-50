import json
from gendiff.parser import load_files
from gendiff.renderers.diff_finder import find_diff


def compare_values(value1, value2):
    if isinstance(value1, dict) and isinstance(value2, dict):
        return generate_diff_json(value1, value2)
    elif value1 == value2:
        return {'status': 'unchanged', 'value': value1}
    elif value1 != value2:
        return {'status': 'changed', 'old_value': value1, 'new_value': value2}


def generate_diff_json(data1, data2):
    diff_tree = find_diff(data1, data2)
    diff = format_diff_json(diff_tree)
    return diff


def format_diff_json(diff_tree):
    formatted_diff = {}
    for item in diff_tree:
        node_type = item['type']
        key = item['key']

        if node_type == 'nested':
            formatted_diff[key] = format_diff_json(item['children'])
        elif node_type == 'added':
            formatted_diff[key] = item['value']
        elif node_type == 'removed':
            formatted_diff[key] = item['value']
        elif node_type == 'changed':
            formatted_diff[key] = item['new_value']
        else:
            formatted_diff[key] = item['value']

    return formatted_diff


def generate_diff_dict_json(data1, data2):
    diff = generate_diff_json(data1, data2)
    formatted_diff = json.dumps(diff, indent=4)
    print(formatted_diff)
    return formatted_diff


def main():
    PATH_TO_FILE1_JSON = "example_files/file1.json"
    PATH_TO_FILE2_JSON = "example_files/file2.json"
    data1, data2 = load_files(PATH_TO_FILE1_JSON, PATH_TO_FILE2_JSON)
    diff = generate_diff_json(data1, data2)
    diff = json.dumps(diff, indent=2)
    print(json.dumps(diff, indent=2))
    return diff