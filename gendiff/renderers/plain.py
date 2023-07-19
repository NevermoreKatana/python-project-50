import json
from gendiff.renderers.diff_finder import find_diff


def generate_diff_plain(data1, data2, path=""):
    diff_tree = find_diff(data1, data2)
    diff = format_diff_plain(diff_tree)
    return diff


def format_diff_plain(diff_tree, path=""):
    lines = []
    for item in diff_tree:
        node_type = item['type']
        key = item['key']

        if node_type == 'nested':
            nested_diff = format_diff_plain(item['children'], f"{path}{key}.")
            lines.append(nested_diff)
        elif node_type == 'added':
            value = format_value(item['value'])
            lines.append(f"Property '{path}{key}' "
                         f"was added with value: {value}")
        elif node_type == 'removed':
            value = format_value(item['value'])
            lines.append(f"Property '{path}{key}' was removed")
        elif node_type == 'changed':
            old_value = format_value(item['old_value'])
            new_value = format_value(item['new_value'])
            lines.append(f"Property '{path}{key}' was updated. "
                         f"From {old_value} to {new_value}")

    return "\n".join(lines)


def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return json.dumps(value)


def gendiff_plain(data1, data2):
    diff = generate_diff_plain(data1, data2)
    print(diff)
    return diff
