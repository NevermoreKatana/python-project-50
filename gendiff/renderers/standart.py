import json
from gendiff.parser import file_type

PATH_TO_FILE1_JSON = "example_files/file1.json"
PATH_TO_FILE2_JSON = "example_files/file2.json"

PATH_TO_FILE1_YML = 'example_files/file1.yml'
PATH_TO_FILE2_YML = 'example_files/file2.yml'


def compare_values(value1, value2):
    if isinstance(value1, dict) and isinstance(value2, dict):
        return generate_diff(value1, value2)
    elif value1 == value2:
        return {'status': 'unchanged', 'value': value1}
    elif value1 != value2:
        return {'status': 'changed', 'old_value': value1, 'new_value': value2}


def generate_diff(data1, data2):
    diff = {}
    keys = set(data1.keys()) | set(data2.keys())
    for key in sorted(keys):
        if key not in data1:
            diff[key] = {'status': 'added', 'value': data2[key]}
        elif key not in data2:
            diff[key] = {'status': 'removed', 'value': data1[key]}
        else:
            value1 = data1[key]
            value2 = data2[key]
            if isinstance(value1, dict) and \
                    isinstance(value2, dict):
                diff[key] = {'status': 'nested',
                             'children': generate_diff(value1, value2)}
            else:
                comparison_result = compare_values(value1, value2)
                diff[key] = {'status': comparison_result['status'],
                             'value': comparison_result.get('value'),
                             'old_value': comparison_result.get('old_value'),
                             'new_value': comparison_result.get('new_value')}
    # print(json.dumps(diff, indent=2))
    return diff


def format_diff(diff, indent=0):
    lines = []
    indent_str = ' ' * indent
    nested_indent_str = ' ' * (indent + 4)
    for key, item in diff.items():
        status = item['status']
        if status == 'added':
            lines.append(f"{indent_str}+ {key}: {format_value(item['value'], indent)}")
        elif status == 'removed':
            lines.append(f"{indent_str}- {key}: {format_value(item['value'], indent)}")
        elif status == 'changed':
            lines.append(f"{indent_str}- {key}: {format_value(item['old_value'], indent)}")
            lines.append(f"{indent_str}+ {key}: {format_value(item['new_value'], indent)}")
        elif status == 'nested':
            lines.append(f"{indent_str}{key}:")
            nested_diff = format_diff(item['children'], indent=indent + 4)
            lines.append('\n'.join(nested_diff))
        else:
            lines.append(f"{indent_str}  {key}: {format_value(item['value'], indent)}")
    return lines


def format_value(value, indent):
    if isinstance(value, dict):
        lines = []
        for key, val in value.items():
            lines.append(f"{indent * ' '}{key}: {val}")
        return '{\n' + '\n'.join(lines) + '\n' + (indent - 2) * ' ' + '}'
    else:
        return value


def generate_diff_dict(data1, data2):
    diff = generate_diff(data1, data2)
    formatted_diff = format_diff(diff)
    formatted_diff_str = '{\n' + '\n'.join(formatted_diff) + '\n}'
    print(formatted_diff_str)
    return formatted_diff_str


def main():
    data1, data2 = file_type(PATH_TO_FILE1_JSON, PATH_TO_FILE2_JSON)
    generate_diff_dict(data1, data2)


