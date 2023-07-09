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


def format_diff(diff):
    lines = []
    for key, item in diff.items():
        status = item['status']
        if status == 'added':
            lines.append(f"+ {key}: {item['value']}")
        elif status == 'removed':
            lines.append(f"- {key}: {item['value']}")
        elif status == 'changed':
            lines.append(f"- {key}: {item['old_value']}")
            lines.append(f"+ {key}: {item['new_value']}")
        elif status == 'nested':
            nested_diff = format_diff(item['children'])
            lines.append(f"{key}:")
            lines.extend(['  ' + line for line in nested_diff])
        else:
            lines.append(f"  {key}: {item['value']}")
    return lines


def generate_diff_dict(data1, data2):
    diff = generate_diff(data1, data2)
    formatted_diff = format_diff(diff)
    formatted_diff_str = '\n'.join(formatted_diff)
    print(formatted_diff_str)
    return formatted_diff_str


def main():
    data1, data2 = file_type(PATH_TO_FILE1_JSON, PATH_TO_FILE2_JSON)
    generate_diff_dict(data1, data2)



def main():
    data1, data2 = file_type(PATH_TO_FILE1_JSON, PATH_TO_FILE2_JSON)
    generate_diff_dict(data1, data2)
