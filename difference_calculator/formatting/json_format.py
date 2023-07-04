import json


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
            if isinstance(value1, dict) and isinstance(value2, dict):
                diff[key] = {'status': 'nested',
                             'children': generate_diff(value1, value2)}
            else:
                comparison_result = compare_values(value1, value2)
                diff[key] = {'status': comparison_result['status'],
                             'value': comparison_result.get('value'),
                             'old_value': comparison_result.get('old_value'),
                             'new_value': comparison_result.get('new_value')}
    return diff


def format_diff(diff):
    formatted_diff = {}
    for key, item in diff.items():
        status = item['status']
        if status == 'added':
            formatted_diff[key] = item['value']
        elif status == 'removed':
            formatted_diff[key] = item['value']
        elif status == 'changed':
            formatted_diff[key] = item['new_value']
        elif status == 'nested':
            formatted_diff[key] = format_diff(item['children'])
        else:
            formatted_diff[key] = item['value']
    return formatted_diff


def generate_diff_dict_json(file_path1, file_path2):
    diff = generate_diff(file_path1, file_path2)
    formatted_diff = format_diff(diff)
    formatted_diff = json.dumps(formatted_diff, indent=2)
    print(formatted_diff)
    return formatted_diff
