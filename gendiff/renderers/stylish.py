import json
from gendiff.parser import load_files
from gendiff.renderers.diff_finder import find_diff


def generate_diff_stylish(data1, data2):
    diff_tree = find_diff(data1, data2)
    diff = format_diff_stylish(diff_tree)
    return diff


def format_diff_stylish(diff_tree, indent="  "):
    lines = ["{"]
    lines.extend(format_diff_items(diff_tree, indent))
    lines.append("}")
    return "\n".join(lines)


def format_diff_items(diff_tree, indent="  "):
    lines = []
    node_type_format = {
        'nested': lambda k, v: f"{indent}  {k}: {{\n{v}\n{indent}  }}",
        'added': lambda k, v: f"{indent}+ {k}: {v}",
        'removed': lambda k, v: f"{indent}- {k}: {v}",
        'changed': lambda k, old_v, new_v: f"{indent}- {k}:"
                                           f" {old_v}\n{indent}+ {k}: {new_v}",
        'unchanged': lambda k, v: f"{indent}  {k}: {v}",
    }

    for item in diff_tree:
        node_type = item['type']
        key = item['key']
        value = item.get('value')

        if node_type in ('added', 'removed', 'unchanged'):
            value = format_value(value, indent + '  ')
            lines.append(node_type_format[node_type](key, value))
        elif node_type == 'changed':
            old_value = format_value(item['old_value'], indent + '  ')
            new_value = format_value(item['new_value'], indent + '  ')
            lines.append(node_type_format[node_type](key, old_value, new_value))
        elif node_type == 'nested':
            nested_diff = format_diff_items(item['children'], indent + '    ')
            lines.append(node_type_format[node_type](key, nested_diff))

    return lines


def format_value(value, indent="  "):
    if isinstance(value, dict):
        lines = [f"{indent}    {k}: {format_value(v, indent + '    ')}"
                 for k, v in value.items()]
        return "{\n" + "\n".join(lines) + f"\n{indent}}}"
    else:
        return json.dumps(value, ensure_ascii=False).strip('"')


def main():
    PATH_TO_FILE1_JSON = "example_files/file1.yml"
    PATH_TO_FILE2_JSON = "example_files/file2.yml"
    data1, data2 = load_files(PATH_TO_FILE1_JSON, PATH_TO_FILE2_JSON)
    diff = generate_diff_stylish(data1, data2)
    print(diff)
