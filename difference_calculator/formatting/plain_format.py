def compare_values(value1, value2):
    if isinstance(value1, dict) and isinstance(value2, dict):
        return generate_diff(value1, value2)
    elif value1 == value2:
        return {'status': 'unchanged', 'value': value1}
    else:
        return {'status': 'changed', 'old_value': value1, 'new_value': value2}


def generate_diff(data1, data2, path=''):
    diff = []
    keys = set(data1.keys()) | set(data2.keys())
    for key in sorted(keys):
        current_path = f"{path}.{key}" if path else key
        if key not in data1:
            diff.append({
                'path': current_path,
                'status': 'added',
                'value': data2[key]
            })
        elif key not in data2:
            diff.append({
                'path': current_path,
                'status': 'removed',
                'value': data1[key]
            })
        else:
            value1 = data1[key]
            value2 = data2[key]
            if isinstance(value1, dict) and isinstance(value2, dict):
                sub_diff = generate_diff(value1, value2, current_path)
                diff.extend(sub_diff)
            else:
                comparison_result = compare_values(value1, value2)
                diff.append({
                    'path': current_path,
                    **comparison_result
                })
    return diff


def format_diff_plain(diff):
    lines = []
    for item in diff:
        path = item['path']
        status = item['status']
        if status == 'added':
            value = format_value(item['value'])
            lines.append(f"Property '{path}' was added with value: {value}")
        elif status == 'removed':
            lines.append(f"Property '{path}' was removed")
        elif status == 'changed':
            old_value = format_value(item['old_value'])
            new_value = format_value(item['new_value'])
            lines.append(f"Property '{path}' was updated."
                         f" From {old_value} to {new_value}")
    return lines


def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return "null"
    else:
        return str(value)


def generate_diff_plain(data1, data2):
    diff = generate_diff(data1, data2)
    diff_string = '\n'.join(format_diff_plain(diff))
    print(diff_string)
    return diff_string
